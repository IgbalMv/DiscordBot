import discord
import json
from discord.ext import commands


file = open('config.json', 'r')
config = json.load(file)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = True
intents.presences = True



bot = commands.Bot(intents=intents,command_prefix = config['prefix'])

@bot.event
async def on_ready():
    print('Bot online')

@bot.command(name = 'ping')
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention}pong')

@bot.command(name = 'hi')
async def hi(ctx: commands.context):
    await ctx.send(f'{ctx.author.mention}', embed = discord.Embed(description= "Hello, good to see you", colour= 0xFF0909))





bot.run(config['token'])