import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = '!')
playerCollection = {}
activeUsers = []
handCollection = {}
deck = []
inPlay = False

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def starter(ctx):
    if ctx.message.author.id in playerCollection:
        await ctx.send(f'Fuck you')
    else:
        playerCollection[ctx.message.author.id] = 500
        await ctx.send(f'{ctx.message.author.name} now starts with {playerCollection.get(ctx.message.author.id)}')

@client.command()
async def play(ctx):
    if ctx.message.author.id in playerCollection and len(activeUsers) < 10:
        activeUsers.append(ctx.message.author.id)
        await ctx.send(f"Next Game You'll be Dealt In")

@client.command()
async def ready(ctx):
    if ctx.message.author.id in playerCollection:
        inPlay = True
        deck = ["1♠","1♥","1♦","1♣", "2♠","2♥","2♦","2♣", "3♠","3♥","3♦","3♣", "4♠","4♥","4♦","4♣", "5♠","5♥","5♦","5♣", "6♠","6♥","6♦","6♣", "7♠","7♥","7♦","7♣",
        "8♠","8♥","8♦","8♣", "9♠","9♥","9♦","9♣", "10♠","10♥","10♦","10♣", "11♠","11♥","11♦","11♣", "12♠","12♥","12♦","12♣", "13♠","13♥","13♦","13♣",]
        random.shuffle(deck)
        for key in activeUsers:
            handCollection[key] = [deck.pop(0), deck.pop(0)]
            user = client.get_user(key)
            if handCollection[key][0]
            await user.send(str(handCollection[key][0]) + "        " + str(handCollection[key][1]))
        await ctx.send(f'Hands Dealt')
        for key in activeUsers:
            await ctx.send(f'{client.get_user(key).name}; Check, Bet, or Fold?')

@client.command()
async def bet(ctx, arg):
    if type(int(arg)) == int:
        playerCollection[ctx.message.author.id] -= int(arg)
        await ctx.send(f'{ctx.message.author.name} has bet {arg}')
    else:
        await ctx.send(f'shite')

@client.command()
async def check(ctx):
    if type(int(arg)) == int:
        playerCollection[ctx.message.author.id] -= int(arg)
        await ctx.send(f'{ctx.message.author.name} has bet {arg}')
    else:
        await ctx.send(f'shite')

@client.command()
async def call(ctx):
    if type(int(arg)) == int:
        playerCollection[ctx.message.author.id] -= int(arg)
        await ctx.send(f'{ctx.message.author.name} has bet {arg}')
    else:
        await ctx.send(f'shite')


@client.command()
async def raise_stakes(ctx):
    if type(int(arg)) == int:
        playerCollection[ctx.message.author.id] -= int(arg)
        await ctx.send(f'{ctx.message.author.name} has bet {arg}')
    else:
        await ctx.send(f'shite')

@client.command()
async def fold(ctx):
    if type(int(arg)) == int:
        playerCollection[ctx.message.author.id] -= int(arg)
        await ctx.send(f'{ctx.message.author.name} has bet {arg}')
    else:
        await ctx.send(f'shite')



@client.command()
async def gift(ctx, arg, arg2):
    if type(int(arg)) == int:
        playerCollection[ctx.message.author.id] -= int(arg)
        await ctx.send(f'{ctx.message.author.name} has bet {arg}')
    else:
        await ctx.send(f'shite')

@client.command()
async def wealth(ctx):
    if ctx.message.author.id in playerCollection:
        await ctx.send(f'{ctx.message.author.name} has {playerCollection.get(ctx.message.author.id)}')


client.run('Mzg0MjQzNjc3NjI4NzI3MzA3.Whpszw.3KIs6UMx_tFbT9hJfTC070XrU7I')