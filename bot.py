import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Bot is ready')

#Credentials
load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))
