from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#Functions are defined as follows

def printt():
    pass

def quit():
    exit()

def about():
    messagebox.showinfo("Demo","This is just a demo for menu buttons")

def newWindow():

    nwindow = Tk()
    nwindow.geometry("300x200")
    nwindow.title("Welcome to the login page")
    nwindow.resizable(width=FALSE,height=FALSE)

    l1 = Label(nwindow,text="Registration Completed",font=("arial",14,"bold"),relief=SOLID)
    l1.pack()

    #Creating a Button

    but1 = Button(nwindow,text = "Demo",font=("arial",12,"bold"),command=about)
    but1.place(x=120,y=100)


    nwindow.mainloop()

