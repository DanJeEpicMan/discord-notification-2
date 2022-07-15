import discord
#import gui



def discord_def(x):

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
    


    client.run("your account authentication token")

discord_def(1)