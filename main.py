import discord
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


"""THE KNIGHT BOT"""

# Client/bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', case_insensitive=True, intents=intents, Intents=discord.Intents.all)
frameinfo = getframeinfo(currentframe())
traceback = True
id_s = bot.get_guild(608966488136876032)
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load in stuff
os.chdir(dir_path)
bot.remove_command('help')
bot.load_extension("casino")  # use name of python file here
bot.load_extension("commands")  # use name of python file here
bot.load_extension("vc_commands")  # use name of python file here
bot.load_extension("discord_events")  # use name of python file here
bot.load_extension("mod_command")  # use name of python file here

print("Online")
bot.run('TOKEN')
