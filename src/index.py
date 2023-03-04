import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

#initializing bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>', description="my bot",intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def sum(ctx, n1:int, n2:int):
    await ctx.send(n1 + n2)

@bot.command()
async def stats (ctx):
    embed = discord.Embed(title =f"{ctx.guild.name}", description = "hola soy el gato de Miga"
                          , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name ="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name = "Server owner", value=f"{ctx.guild.owner}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)

@bot.command()
async def commands(ctx):
    ayuda = discord.Embed(title ="Comandos"
                          , description = ">ping = returns pong \n >stats = returns server stats \n >sum n1 n2 = returns the result of n1 + n2 \n >yt (video name) = returns the results of a youtube search"
                          , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    await ctx.send(embed=ayuda)
    
@bot.command()
async def yt(ctx,*,search):
    query = parse.urlencode({'search_query':search})
    html_content = request.urlopen("http://www.youtube.com/results?" + query)
    search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print (search_results)
    await ctx.send ("http://www.youtube.com/watch?v=" + search_results[0])
    await ctx.send ("http://www.youtube.com/watch?v=" + search_results[1])
    await ctx.send ("http://www.youtube.com/watch?v=" + search_results[2])
    await ctx.send ("http://www.youtube.com/watch?v=" + search_results[3])
    await ctx.send ("http://www.youtube.com/watch?v=" + search_results[4])
#event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=">commands"))
    print ("my bot is ready")
bot.run(token)
    
