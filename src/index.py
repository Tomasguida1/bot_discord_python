import discord
from discord.ext import commands

#initializing bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>', description="my bot",intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    

bot.run(TOKEN)
    
