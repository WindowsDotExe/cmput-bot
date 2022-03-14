import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = '>')
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))
    print(f'Logged in as {bot.user.name}({bot.user.id})')

@bot.command()
async def ping(ctx):
    '''
    Self explanatory much?
    '''
    await ctx.send('pong!')

@bot.command()
async def say(ctx, *, arg):
    '''
    Send a message from the bot account.
    Format: >say (arguments)
    '''
    await ctx.send(f'{arg}\n*Author: {ctx.message.author.name}*')
    await ctx.message.delete()

@bot.command()
async def due(ctx):
    '''
    Displays all assignments/labs/etc. due in the given week.
    '''
    await ctx.send("**__Here's what's due this week:__**\n - Post-test 8: Search-Recursion-Sorting (Thursday March 17 @ 11:55 PM Edmonton time)\n - Lab 8 (Saturday March 19 @ 11:59 PM Edmonton time)\n\n Due soon:\n - Assignment 3: AbacoStack Game (Friday April 1 @ 11:55 PM Edmonton time)")
    await ctx.message.delete()

if __name__ == "__main__":
    bot.run(TOKEN)
