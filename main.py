import datetime
from datetime import datetime
import self as self
from discord.ext import commands, tasks
from discord.ext.commands import bot
import tracemalloc
import random
import asyncio
import json
import discord.utils
import os
import pytz
import aiocron
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from inspect import currentframe, getframeinfo
import sys
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from discord.utils import find, get
import os.path
import module
import youtube_dl
from discord.ext.commands import MissingPermissions
import time
import threading
from itertools import cycle

"""Project: Eive-SC/(Source Code)"""

# Client/bot
intents = discord.Intents.default()
intents.members = True


def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents, Intents=discord.Intents.all)
frameinfo = getframeinfo(currentframe())
traceback = True
id_s = bot.get_guild(608966488136876032)
dir_path = os.path.dirname(os.path.realpath(__file__))
bot.remove_command('help')
extensions = ['casino', 'commands', 'vc_commands', 'discord_events', 'mod_command']

# Load in stuff
os.chdir(dir_path)


@bot.command(name="help2", description="Returns all commands available")
async def help2(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    helptext = "`"
    for command in bot.commands:
        helptext += f"{prefixes[str(ctx.guild.id)]} {command}\n"
    helptext += "`"
    await ctx.send(helptext)


@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print(f'loaded. {format(extension)}')
    except Exception as error:
        print(f'{format(extension)} cannot be loaded. [{format(error)}]')


@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print(f'Unloaded. {format(extension)}')
    except Exception as error:
        print(f'{format(extension)} cannot be unloaded. [{format(error)}]')


"""
total_members_count = len(bot.users)

status = [f"Member count: {total_members_count}", "Defualt help command: ?help",
          f"{self.bot.user.name} is in {len(bot.guilds)} servers!"]


async def change_status():
    await bot.wait.until_ready
    msgs = cycle(status)

    while not bot.is_bot:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep()
"""









if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print(f'{format(extension)} cannot be loaded. [{format(error)}]')

    commands_list = [c.name for c in bot.commands]
    print(f'\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print(f'\nCommand List: {commands_list}')

    """bot.loop.create_task((change_status()))"""
    bot.run('')
