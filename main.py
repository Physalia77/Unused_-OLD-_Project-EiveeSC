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
from discord.utils import find
import os.path
import module
import youtube_dl
from discord.ext.commands import MissingPermissions
import time
import threading

"""THE KNIGHT BOT"""

# Client/bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', case_insensitive=True, intents=intents, Intents=discord.Intents.all)
frameinfo = getframeinfo(currentframe())
traceback = True
id_s = bot.get_guild(608966488136876032)
dir_path = os.path.dirname(os.path.realpath(__file__))
bot.remove_command('help')
extensions = ['casino', 'commands', 'vc_commands', 'discord_events', 'mod_command']

# Load in stuff
os.chdir(dir_path)


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

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print(f'{format(extension)} cannot be loaded. [{format(error)}]')

    print("Online")
    bot.run('OTAyNjA2MzM2NzgzNjgzNTg1.YXg3qA.WXmaMdQUEVXYQnhBQMGz5dO4c6U')