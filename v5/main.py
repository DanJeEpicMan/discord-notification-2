import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import asyncio
import time
from discord.ext import commands
from PyQt5.QtWidgets import QPushButton
import keyboard
import pyautogui
import os

typed_msg = ''

os.system('color 84')
os.system('title Discord 2')

for _ in range(7):
    pyautogui.hotkey("ctrl", "shift", "-")

import win32gui
import win32con
hwnd = win32gui.GetForegroundWindow()#          xpos ypos width hight importance
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,2168,1068,400,300,0)

# import necessary modules
from tkinter import *

import threading
import discord
def gui():
    global typed_msg
    #typed_msg = ''
    class MainWindow(qtw.QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Discord 2")

            self.setLayout(qtw.QHBoxLayout())

            #self.label_1 = QLabel("transparent ", self)
            my_entry = qtw.QLineEdit()
            my_entry.setObjectName("name_field")
            my_entry.setText("")
            self.layout().addWidget(my_entry)

            my_button = QPushButton(">", clicked = lambda: press_it())
            self.layout().addWidget(my_button)

            self.show()

            def press_it():
                typed_msg = f'{my_entry.text()}'
                #print(typed_msg)
                my_entry.setText("")
                respond(typed_msg)



    app = qtw.QApplication([])
    mw = MainWindow()


    app.exec_()


    

     #ok so like use my_label = qtw.QLabel(homo) to change what label says instead of variables

t1 = threading.Thread(target=gui, args=())
t1.start()
pyautogui.moveTo(1016, 445, 0.1)
time.sleep(.5)
pyautogui.leftClick()
time.sleep(.5)
hwnd = win32gui.GetForegroundWindow()#          xpos ypos width hight importance
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,2168,1360,400,100,0)
os.system('cls')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def key_binds():
    while 1:
        if keyboard.is_pressed('Ins') == True:
            pyautogui.hotkey("alt", "tab")

        if keyboard.is_pressed('Del') == True:
            os.system('cls')

        if keyboard.is_pressed('End') == True:
            pyautogui.moveTo(2476, 1415, 0.1)
            time.sleep(.2)
            pyautogui.leftClick()

        if keyboard.is_pressed('Home') == True:
            pyautogui.moveTo(1200, 600, 0.1)
            time.sleep(.2)
            pyautogui.leftClick()


t2 = threading.Thread(target=key_binds, args=())
#t2.start()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
bot = commands.Bot('')


@bot.event
async def on_message(message):  # this event is called when a message is sent by anyone
        global content, user, channel, server

                # this is the string text message of the Message
        content = message.content
            # this is the sender of the Message
        user = message.author
                # this is the channel of there the message is sent
        channel = message.channel

        server = message.guild
                
        if user == bot.user:
            return
                

        fin_msg = '{}:{}--{}:"{}"'.format(server, channel, user, content)
        print(fin_msg)



def respond(typed_msg):
    if not typed_msg == '':
        print(typed_msg)
        bot.loop.create_task(channel.send(typed_msg))
                


bot.run("your account authentication token") # make it so that pressing ins- does alt-tab and so that end sends msg and so deleat clears it 




'''@client.event
async def on_message(message):  # this event is called when a message is sent by anyone
        global content, user, channel, server

                # this is the string text message of the Message
        content = message.content
            # this is the sender of the Message
        user = message.author
                # this is the channel of there the message is sent
        channel = message.channel

        server = message.guild
                
        if user == client.user:
            return
                

        fin_msg = '{}:{}--{}:"{}"'.format(server, channel, user, content)
        print(fin_msg)'''


# multithread both prosseses

'''    try:
        n_msg = test()
        print(n_msg)
    except:
        n_msg = ''
        print(n_msg)

    if not n_msg == "":
        await channel.send(n_msg)
        n_msg = ""
    
'''


'''
from tkinter import *

root = Tk()
#root.geometry("300x300")
root.title("Discord 2")

root.wm_attributes('-transparentcolor', root['bg'])
root.wm_attributes('-transparentcolor', 'black')

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    Output.insert(END, 'Correct')
     
l = Label()
inputtxt = Text(root, height = 1,
                width = 50,
                fg='#FFFFFF',
                bg = "grey")
 
Output = Text(root, height = 20,
              width = 45,
              fg='grey',
              font=("Bold", 12),
              bg = "black")
 
Display = Button(root, height = 1,
                 width = 56,
                 text ="Send",
                 bg = "dark grey",
                 command = lambda:Take_input())
 
#l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()
'''