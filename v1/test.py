# import necessary modules
import discord
import os
import threading
import keyboard
import time


client = discord.Client()
    


def da_loop():
    a = 1
    key = ''
    string1 = ''
    while a == 1:
        if keyboard.is_pressed('q'):
            key = 'q'
        if keyboard.is_pressed('w'):
            key = 'w'
        if keyboard.is_pressed('e'):
            key = 'e'
        if keyboard.is_pressed('r'):
            key = 'r'
        if keyboard.is_pressed('t'):
            key = 't'
        if keyboard.is_pressed('y'):
            key = 'y'
        if keyboard.is_pressed('u'):
            key = 'u'
        if keyboard.is_pressed('i'):
            key = 'i'
        if keyboard.is_pressed('o'):
            key = 'o'
        if keyboard.is_pressed('p'):
            key = 'p'
        if keyboard.is_pressed('a'):
            key = 'a'
        if keyboard.is_pressed('s'):
            key = 's'
        if keyboard.is_pressed('d'):
            key = 'd'
        if keyboard.is_pressed('f'):
            key = 'f'
        if keyboard.is_pressed('g'):
            key = 'g'
        if keyboard.is_pressed('h'):
            key = 'h'
        if keyboard.is_pressed('j'):
            key = 'j'
        if keyboard.is_pressed('k'):
            key = 'k'
        if keyboard.is_pressed('l'):
            key = 'l'
        if keyboard.is_pressed('z'):
            key = 'z'
        if keyboard.is_pressed('x'):
            key = 'x'
        if keyboard.is_pressed('c'):
            key = 'c'
        if keyboard.is_pressed('v'):
            key = 'v'
        if keyboard.is_pressed('b'):
            key = 'b'
        if keyboard.is_pressed('n'):
            key = 'n'
        if keyboard.is_pressed('m'):
            key = 'm'
        if keyboard.is_pressed('.'):
            key = '.'
        if keyboard.is_pressed(','):
            key = ','
        if keyboard.is_pressed('1'):
            key = '1'
        if keyboard.is_pressed('2'):
            key = '2'
        if keyboard.is_pressed('3'):
            key = '3'
        if keyboard.is_pressed('4'):
            key = '4'
        if keyboard.is_pressed('5'):
            key = '5'
        if keyboard.is_pressed('6'):
            key = '6'
        if keyboard.is_pressed('7'):
            key = '7'
        if keyboard.is_pressed('8'):
            key = '8'
        if keyboard.is_pressed('9'):
            key = '9'
        if keyboard.is_pressed('0'):
            key = '0'
        if keyboard.is_pressed('"'):
            key = '"'
        if keyboard.is_pressed(' '):
            key = ' '
            #add rest of keys
        string1 = string1 + key
        key = ''
        if not string1 == '':
            print(string1) # change this so that it records keystorkes at the same speed but them clears messages 3 times a second
        #string1 = ''
        time.sleep(0.05) #if someone presses ins make it stop
        
#-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def replay():
    global msg_replay
    msg_rep = input("-")
#t1.start() #make join when press ins

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
    # if the user is the client user itself, ignore the message
    msg_rep = input("-") #rest of the script wont laod untill you replay so new messages cant be loaded, multithread
    await message.channel.send(msg_rep) 
    print('{}:{}--Me:"{}"'.format(server, channel, msg_rep))# fundimentily rework how this thing works with gui in mind
    time.sleep(5)
    os.system('cls')

t1 = threading.Thread(target=da_loop, args=())
t2 = threading.Thread(target=replay, args=())
    
client.run("your account authentication token")
