import discord
from discord.ext import commands
import datetime

#initializing bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>', description="my bot",intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("pov")

@bot.command()
async def sum(ctx, n1:int, n2:int):
    await ctx.send(n1 + n2)

@bot.command()
async def stats (ctx):
    embed = discord.Embed(title =f"{ctx.guild.name}", description = "hola soy el gato de Miga", timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)
    
#event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=">commands"))
    print ("my bot is ready")
bot.run(token)
    
