import discord,random,ast,re,datetime
from asyncio import sleep
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='s!')
token = "DISCORD_BOT_TOKEN"

admin = [418812526470365214, 446996726335799297]

@bot.event
async def on_reaction_add(reaction, user):
    if user.id in admin:
        message = reaction.message:
        await message.add_reaction(f"{reaction}")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')




bot.run(token, bot=False)
