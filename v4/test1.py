# import necessary modules
from tkinter import *

import threading
import discord
def gui(fin_msg, *args):

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
    Output.insert(END, fin_msg)
    mainloop()



client = discord.Client()

@client.event
async def on_message(message):  # this event is called when a message is sent by anyone

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
    print(fin_msg)

    t1 = threading.Thread(target=gui, args=(fin_msg))
    t1.start()
    
#t1 = threading.Thread(target=gui, args=())
#t2 = threading.Thread(target=discord, args=())

#t1.start()
#t2.start()

client.run("your account authentication token")
# multithread both prosseses
