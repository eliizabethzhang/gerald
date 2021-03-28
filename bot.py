import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Bot is ready')

client.run('ODI1NDY2NTYwOTQwMjEyMjk0.YF-VpA.4WS5sr83o-Qm2vmnY9VLF3DnyjU')
