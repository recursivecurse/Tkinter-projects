from tkinter import *
from tkinter import messagebox
from Game import *
from PIL import Image, ImageTk
from Imagesize import *
from functions import *


window = Tk()
window.geometry("400x500")
window.title("Tic Tac Toe")
window.resizable(width=FALSE,height=FALSE)

#Creating variables

name = StringVar()
symbol = StringVar()

#Creating play function

def play():
    p1name = entry1.get()
    sym    =  entry2.get()
    TickTacToe(p1name,sym)

def Quit():
    exit()




img = Image.open('/home/adityamishra/Desktop/Tkinter/Tkinter-projects/Tic-Tac-Toe/tic.png')
resize(img)
img_resized = Image.open("/home/adityamishra/Desktop/Tkinter/Tkinter-projects/Tic-Tac-Toe/tic_resized.png")
photo = ImageTk.PhotoImage(img_resized)
label0 = Label(window, image=photo)
label0.place(x=90, y=50)

#Creating Label

label1 = Label(window,text="Player name",font=("arial",14,"bold"))
label1.place(x=40,y=300)
label2 = Label(window,text="Symbol(XorO) ",font=("arial",14,"bold"))
label2.place(x=40,y=350)

#Creating Entry Fields

entry1 = Entry(window,textvariable= name)
entry1.config(font=("arial",12,"bold"),width=20)
entry1.place(x=200,y=300)
entry2 = Entry(window,textvariable= symbol)
entry2.config(font=("arial",12,"bold"),width=20)
entry2.place(x=200,y=350)

#Creating Play button

but1 = Button(window,text="Play",relief=RAISED,bg="#FF0000",font=("arial",14,"bold"),command=play)
but1.place(x=100,y=400)
but2 = Button(window,text="Quit",relief=RAISED,bg="#FF0000",font=("arial",14,"bold"),command=Quit)
but2.place(x=200,y=400)
window.mainloop()
