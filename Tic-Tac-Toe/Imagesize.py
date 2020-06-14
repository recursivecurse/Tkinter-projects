from tkinter import *
from PIL import Image, ImageTk
import math

def resize(img):
    #img = Image.open("/home/adityamishra/Desktop/Tkinter/Tkinter-projects/Tic-Tac-Toe/tic.png")
    x,y = img.size
    x2,y2 = math.floor(x-300),math.floor(y-300)
    img =  img.resize((x2,y2),Image.ANTIALIAS)
    img.save("/home/adityamishra/Desktop/Tkinter/Tkinter-projects/Tic-Tac-Toe/tic_resized.png",quality=95)

