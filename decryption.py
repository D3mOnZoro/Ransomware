from ast import Break
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64decode
import getpass
import os,string
from tkinter import messagebox
import tkgui
from encryption import encrypted_file

files_decrypted=0

count=1

class Recover:
    def __init__(self,file_name,key,no_encrypted):
        self.file_name=file_name
        self.key=key
        self.no_encrypted=no_encrypted
    
    def decrypted_file(self):
        global count, files_decrypted
        print(count)
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
                print(files_decrypted,"is decrypted files")
                
            except(ValueError,KeyError):
                if count <2:
                  print("wrong password")
                  messagebox.showerror("ERROR","Wrong Key!!! Enter the valid key ") 
                  count +=1

    def winclose(self):
        if (self.no_encrypted == files_decrypted):
            tkgui.win.destroy()
            
            
            