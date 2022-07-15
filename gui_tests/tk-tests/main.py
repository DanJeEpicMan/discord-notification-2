# import necessary modules
from tkinter import *

import threading
import discord

root = Tk()
    #root.geometry("300x300")
root.title("Discord 2")

root.wm_attributes('-transparentcolor', root['bg'])
root.wm_attributes('-transparentcolor', 'black')

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
        
l = Label()
inputtxt = Text(root, height = 1,
                    width = 50,
                    fg='#FFFFFF',
                    bg = "grey")
    

Display = Button(root, height = 1,
                    width = 56,
                    text ="Send",
                    bg = "dark grey",
                    command = lambda:Take_input())
    
    #l.pack()
inputtxt.pack()
Display.pack()
mainloop()