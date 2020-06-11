from tkinter import *
from PIL import Image, ImageTk

window=Tk()
window.geometry("700x900")
window.title("Registration Form")

#Variables declaration

fn = StringVar()
ln = StringVar()
dob = StringVar()
op = StringVar()
cy = StringVar()
list = ["Bengaluru","Zurich","Bay Area","Mumbai"]

#Functions are defined as follows

def printt():
    print("The button is pressed")

def quit():
    exit()

image = Image.open("/home/adityamishra/Desktop/icon.png")
photo = ImageTk.PhotoImage(image)
label0 = Label(window,image=photo)
label0.pack(pady=20)

#Labels are defined as follows
label1 = Label(window,text="REGISTRATION FORM",font=("arial",14,"bold"),fg="blue",bg="#FFFFFF",relief="solid")
label1.pack(fill=BOTH,pady=10,padx=10)
label2 = Label(window,text="First Name",font=("arial",14,"bold"))
label2.place(x=50,y=400)
label3 = Label(window,text="Last name",font=("arial",14,"bold"))
label3.place(x=50,y=450)
label4 = Label(window,text="Date Of Birth",font=("arial",14,"bold"))
label4.place(x=50,y=500)
label5 = Label(window,text="Occupation ",font=("arial",14,"bold"))
label5.place(x=50,y=550)
label6 = Label(window,text="City",font=("arial",14,"bold"))
label6.place(x=50,y=600)

#The Text field corresponding to the Labels are defined as follows

textfield1 = Entry(window,textvariable=fn)
textfield1.config(width=30,font=("arial",14,"bold"))
textfield1.place(x=300,y=400)
textfield2 = Entry(window,textvariable=ln)
textfield2.config(width=30,font=("arial",14,"bold"))
textfield2.place(x=300,y=450)
textfield3 = Entry(window,textvariable=dob)
textfield3.config(width=30,font=("arial",14,"bold"))
textfield3.place(x=300,y=500)
textfield4 = Entry(window,textvariable=op)
textfield4.config(width=30,font=("arial",14,"bold"))
textfield4.place(x=300,y=550)

droplist = OptionMenu(window,cy,*list)
cy.set("Select City")
droplist.config(width=20,font=("arial",14,"bold"))
droplist.place(x=300,y=600)


button1 = Button(window,text="Submit",relief=RAISED,font=("arial",14,"bold"))
button1.place(x=150,y=700)
button2 = Button(window,text="Quit",relief=RAISED,font=("arial",14,"bold"),command=quit)
button2.place(x=450,y=700)
window.mainloop()

