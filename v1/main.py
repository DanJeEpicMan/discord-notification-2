from discord.ext import commands
prefix = "."
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("online")

@bot.event
async def on_message(message):
    if message.guild.id == 933546446202994699:
        print("yes")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run("your account authentication token")

'''
@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command(pass_context=True)
async def getguild(ctx):
    id = ctx.message.guild.id
    print(id)
'''