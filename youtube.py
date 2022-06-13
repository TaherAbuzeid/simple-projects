from distutils.cmd import Command
from tkinter import *
from pytube import YouTube
import os

a = Tk()
a.geometry("700x700")
a.config(bg="black")
a.title("OWN VIDEO DOWNLOADER")

Label(a,text="Youtube", font=("Arial",29,"bold"), bg="light pink").pack()
Label(a,text = "Vido Downloder" , font = ("Arail",29 , "bold"), bg="light pink").pack()

link = StringVar()
Label(a,text = "Enter the link" , font=("Arial" , 24 , "bold")).place(x=20,y=150)

E_link = Entry(a, width=35 , font=31 , textvariable=link , bd=5).place(x = 250, y= 150)

def fun1():

    try:


        url = YouTube(str(link.get()))
        v = url.streams.first()
        v.download()
  
        Label(a,text = "DOWNLOAD complated !!",font = ("Arial",26, "bold"), bg= "yellow").place(x= 150,y= 450)
        Label(a,text="Check your folder", font=("Arial",26 ,"bold"), bg="yellow",).place(x = 200 , y=550)
    except:
        Label(a,text="Error" , font=("Arial",29 , "bold") , bg="red" ).place(x = 250 , y = 200)


Button(a, text="DOWNLOAD", font=("Arial",26,"bold"), bg="light green", command=fun1).place(x=200, y=300)






a.mainloop()
