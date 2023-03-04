import discord
from discord.ext import commands

#initializing bot
bot = commands.Bot(command_prefix='>', description="my bot")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    

bot.run("MTA4MTYxODg3ODYwMzQ2NDcyNA.GcIJ5T.3A-r9HZDPdUXF0wQ3SdAZL-HX0mkTVaxGMHhfI")
    
