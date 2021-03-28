import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
import random

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
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command(aliases=['ccreate'])
async def classescreate(ctx, *, rest):
    await ctx.send(f"Created the class {rest}")

@client.command(aliases=['cdelete'])
async def classesdelete(ctx, *, rest):
    await ctx.send(f"Deleted the class {rest}")

@client.command(aliases=['tadd'])
async def taskadd(ctx, classnum, *, rest):
    await ctx.send(f'added the task {rest} to class number {classnum}')

@client.command(aliases=['tdel'])
async def taskdelete(ctx, classnum, *, rest):
    await ctx.send(f'deleted the task {rest} from class number {classnum}')

@client.command(aliases=['tlist'])
async def tasklist(ctx, classnum):
    await ctx.send(f'Your tasks for class {classnum} are: \nAction Plan Deadline: 3/31/2021\nEssay/Discussion Deadline: 4/1/2021')

@client.command(aliases=['clist'])
async def classeslist(ctx):
    await ctx.send(f'Your classes are:\n CLyerly 2A Differential Equations\n COgren 4B APES')
# Credentials
load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))
