from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("Welcome")
label1 = Label(window,text="Welcome to demo on Tkinter",font=("arial",14,"bold"),fg='blue',bg='#FFFFFF').pack()
#label1.grid(row=1,column=0)
#label1.pack(fill=BOTH,pady=5,padx=5)
#label1.place(x=10,y=10)
window.mainloop()
