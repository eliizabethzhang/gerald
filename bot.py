import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient




client = commands.Bot(command_prefix='.')
intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)



@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')



cluster = MongoClient(os.getenv('MONGO_URL'))
db = cluster["UserData"]
collection = db["UserData"]

# Credentials
load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))