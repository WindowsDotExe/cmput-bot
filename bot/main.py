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
    Format: >send (arguments)
    '''
    await ctx.send(f'{arg}\n*Author: {ctx.message.author.name}*')
    await ctx.message.delete()

@bot.command()
async def due(ctx):
    '''
    Displays all assignments/labs/etc. due in the given week.
    '''
    await ctx.send("**Here's what's due this week:**\n - Post-test 7: Doubly-Linked Lists (Wednesday March 9 @ 11:55 PM Edmonton time)\n - Lab 7 (Saturday March 12 @ 11:59 PM Edmonton time)\n")
    await ctx.message.delete()

if __name__ == "__main__":
    bot.run(TOKEN)
