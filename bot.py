import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

async def on_member_remove(member):
    print(f'{member} has left the server')

# Credentials
load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))
