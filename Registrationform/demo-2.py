from tkinter import *
from tkinter import messagebox
from functions import *
from PIL import Image, ImageTk

#Creating a Window
window=Tk()
window.resizable(width=FALSE,height=FALSE)
window.geometry("700x900")
window.title("Registration Form")

#Variables declaration

fn = StringVar()
ln = StringVar()
dob = StringVar()
op = StringVar()
cy = StringVar()
list = ["Bengaluru","Zurich","Bay Area","Mumbai"]

var_c1 = StringVar()
var_c2 = StringVar()
var_c3 = StringVar()
var_r = StringVar()

# Controller
def printDetails():
    a = textfield1.get()
    b = textfield2.get()
    c = textfield3.get()
    d = textfield4.get()
    e = cy.get()
    f = var_r.get()
    messagebox.showinfo("Welcome","Welcome !! You have succesfully registered")


    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)


#Setting image using PIL
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
label7 = Label(window,text="Programming Language ",font=("arial",14,"bold"))
label7.place(x=50,y=650)
label8 = Label(window,text="Gender",font=("arial",14,"bold"))
label8.place(x=50,y=700)

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

#CheckBoxes

c1 = Checkbutton(window,text="Java",variable=var_c1,font=("arial",14,"bold"))
c1.place(x=300,y=650)
c2 = Checkbutton(window,text="C/C++",variable=var_c2,font=("arial",14,"bold"))
c2.place(x=400,y=650)
c3 = Checkbutton(window,text="Python",variable=var_c3,font=("arial",14,"bold"))
c3.place(x=500,y=650)
#RadioBoxes

r1=Radiobutton(window,text="Male",variable=var_r,value="Male",font=("arial",14,"bold"))
r1.place(x=300,y=700)
r2=Radiobutton(window,text="Female",variable=var_r,value="Female",font=("arial",14,"bold"))
r2.place(x=400,y=700)

#Creating buttons
button1 = Button(window,text="Submit",relief=RAISED,font=("arial",14,"bold"),command=printDetails,bg="#FF0000")
button1.place(x=100,y=800)
button2 = Button(window,text="Quit",relief=RAISED,font=("arial",14,"bold"),command=quit,bg="#FF0000")
button2.place(x=300,y=800)

#Creating Menu

menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File",menu=subm1, font=("arial",12,"bold"))
subm1.add_command(label="Exit",font=("arial",12,"bold"),command=quit)

subm2 = Menu(menu)
menu.add_cascade(label="Option",menu=subm2,font=("arial",12,"bold"))
subm2.add_command(label="About",font=("arial",12,"bold"),command=about)

#Creating a Login button

loginb = Button(window,text="Login",font=("arial",14,"bold"),relief=RAISED,bg="#FF0000",command=newWindow)
loginb.place(x=500,y=800)


window.mainloop()

