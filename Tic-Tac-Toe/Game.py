from tkinter import *
from tkinter import messagebox
from functions import *


class TickTacToe:

    def __init__(self,p1,sym1):
        root = Tk()
        root.geometry("500x500")
        root.title("Tic-Tac-Toe")

        # Creating Variables
        self.player1 = 1
        self.player2 = 0
        self.p1 = p1
        if sym1 == 'X':
            self.sym1 = 'X'
            self.sym2 = 'O'
        else:
            self.sym1 = 'O'
            self.sym2 = 'X'

        #Creating functions

        def Player1Win():
            win = False

            if self.sym1 == but1["text"] and self.sym1 == but2["text"] and self.sym1 == but3["text"]:
                win = True
                player = self.player1
            if self.sym1 == but4["text"] and self.sym1 == but5["text"] and self.sym1 == but6["text"]:
                win = True
                player = self.player1
            if self.sym1 == but7["text"] and self.sym1 == but8["text"] and self.sym1 == but9["text"]:
                win = True
                player = self.player1
            if self.sym1 == but1["text"] and self.sym1 == but4["text"] and self.sym1 == but7["text"]:
                win = True
                player = self.player1
            if self.sym1 == but2["text"] and self.sym1 == but5["text"] and self.sym1 == but8["text"]:
                win = True
                player = self.player1
            if self.sym1 == but3["text"] and self.sym1 == but6["text"] and self.sym1 == but9["text"]:
                win = True
                player = self.player1
            if self.sym1 == but1["text"] and self.sym1 == but5["text"] and self.sym1 == but9["text"]:
                win = True
                player = self.player1
            if self.sym1 == but3["text"] and self.sym1 == but5["text"] and self.sym1 == but7["text"]:
                win = True
                player = self.player1

            #For player 2

            if self.sym2 == but1["text"] and self.sym2 == but2["text"] and self.sym2 == but3["text"]:
                win = True
                player = self.player2
            if self.sym2 == but4["text"] and self.sym2 == but5["text"] and self.sym2 == but6["text"]:
                win = True
                player = self.player2

            if self.sym2 == but7["text"] and self.sym2 == but8["text"] and self.sym2 == but9["text"]:
                win = True
                player = self.player2
            if self.sym2 == but1["text"] and self.sym2 == but4["text"] and self.sym2 == but7["text"]:
                win = True
                player = self.player2
            if self.sym2 == but2["text"] and self.sym2 == but5["text"] and self.sym2 == but8["text"]:
                win = True
                player = self.player2
            if self.sym2 == but3["text"] and self.sym2 == but6["text"] and self.sym2 == but9["text"]:
                win = True
                player = self.player2
            if self.sym2 == but1["text"] and self.sym2 == but5["text"] and self.sym2 == but9["text"]:
                win = True
                player = self.player2
            if self.sym2 == but3["text"] and self.sym2 == but5["text"] and self.sym2 == but7["text"]:
                win = True
                player = self.player2

            if(win == True and player == self.player1):
                messagebox.showinfo("Game Over","Congratulations "+self.p1+" has Won")
            if(win == True and player == self.player2):
                messagebox.showinfo("Game Over","Congratulations Player 2 has Won")






        def changePlayer():
            t = self.player1
            self.player1 = self.player2
            self.player2 = t

        def PlayerInfo():
            if(self.player1):
                label1.config(text=self.p1+" turn")
            else:
                label1.config(text="Player 2 turn")

        def PBut1():
            root.bell()
            if self.player1 == 1:
                but1.configure(text=self.sym1,font=("arial",14,"bold"))
                but1.configure(state="disabled")
                changePlayer()
            else:
                but1.configure(text=self.sym2,font=("arial",14,"bold"))
                but1.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()


        def PBut2():
            root.bell()
            if self.player1 == 1:
                but2.configure(text=self.sym1,font=("arial",14,"bold"))
                but2.configure(state="disabled")
                changePlayer()
            else:
                but2.configure(text=self.sym2,font=("arial",14,"bold"))
                but2.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()

        def PBut3():
            root.bell()
            if self.player1 == 1:
                but3.configure(text=self.sym1,font=("arial",14,"bold"))
                but3.configure(state="disabled")
                changePlayer()
            else:
                but3.configure(text=self.sym2,font=("arial",14,"bold"))
                but3.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()



        def PBut4():
            root.bell()
            if self.player1 == 1:
                but4.configure(text=self.sym1,font=("arial",14,"bold"))
                but4.configure(state="disabled")
                changePlayer()
            else:
                but4.configure(text=self.sym2,font=("arial",14,"bold"))
                but4.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()

        def PBut5():
            root.bell()
            if self.player1 == 1:
                but5.configure(text=self.sym1,font=("arial",14,"bold"))
                but5.configure(state="disabled")
                changePlayer()
            else:
                but5.configure(text=self.sym2,font=("arial",14,"bold"))
                but5.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()

        def PBut6():
            root.bell()
            if self.player1 == 1:
                but6.configure(text=self.sym1,font=("arial",14,"bold"))
                but6.configure(state="disabled")
                changePlayer()
            else:
                but6.configure(text=self.sym2,font=("arial",14,"bold"))
                but6.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()

        def PBut7():
            root.bell()
            if self.player1 == 1:
                but7.configure(text=self.sym1,font=("arial",14,"bold"))
                but7.configure(state="disabled")
                changePlayer()
            else:
                but7.configure(text=self.sym2,font=("arial",14,"bold"))
                but7.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()

        def PBut8():
            root.bell()
            if self.player1 == 1:
                but8.configure(text=self.sym1,font=("arial",14,"bold"))
                but8.configure(state="disabled")
                changePlayer()
            else:
                but8.configure(text=self.sym2,font=("arial",14,"bold"))
                but8.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()

        def PBut9():
            root.bell()
            if self.player1 == 1:
                but9.configure(text=self.sym1,font=("arial",14,"bold"))
                but9.configure(state="disabled")
                changePlayer()
            else:
                but9.configure(text=self.sym2,font=("arial",14,"bold"))
                but9.configure(state="disabled")
                changePlayer()
            PlayerInfo()
            Player1Win()


            #Creating Labels

        labeln = Label(root,text=p1 + " has chosen "+ sym1,font=("arial",14,"bold"))
        labeln.place(x=140,y=50)
        label1 = Label(root,text=self.p1+" turn ",font=("arial",14,"bold"))
        label1.place(x=140,y=100)

        #Creating Buttons
        but1 = Button(root,text="",height=5,width=5,command=PBut1,font=("arial",14,"bold"))
        but1.place(x=120,y=170)
        but2 = Button(root, text="", height=5, width=5,command=PBut2,font=("arial",14,"bold"))
        but2.place(x=200, y=170)
        but3 = Button(root, text="", height=5, width=5,command=PBut3,font=("arial",14,"bold"))
        but3.place(x=280, y=170)
        but4 = Button(root, text="", height=5, width=5,command=PBut4,font=("arial",14,"bold"))
        but4.place(x=120, y=260)
        but5 = Button(root, text="", height=5, width=5,command=PBut5,font=("arial",14,"bold"))
        but5.place(x=200, y=260)
        but6 = Button(root, text="", height=5, width=5,command=PBut6,font=("arial",14,"bold"))
        but6.place(x=280, y=260)
        but7 = Button(root, text="", height=5, width=5,command=PBut7,font=("arial",14,"bold"))
        but7.place(x=120, y=350)
        but8 = Button(root, text="", height=5, width=5,command=PBut8,font=("arial",14,"bold"))
        but8.place(x=200, y=350)
        but9 = Button(root, text="", height=5, width=5,command=PBut9,font=("arial",14,"bold"))
        but9.place(x=280, y=350)


        root.mainloop()
