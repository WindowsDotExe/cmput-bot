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
    await ctx.send('pong!')

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

if __name__ == "__main__":
    bot.run(TOKEN)
