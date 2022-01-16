from main import *

"""
All commands for The Knight Bot
"""


# Commands
# Setup command
@commands.command(aliases=["setup"])
async def setup1(ctx):
    guild = ctx.guild
    server_id = ctx.message.guild.id
    for guild in bot.guilds:
        if discord.utils.get(guild.text_channels, name="bot-chat"):
            def v0():
                channel = discord.utils.get(ctx.guild.channels, name="bot-chat")
                bot_chat_id = channel.id
                print(f"ID for channel #Quote {bot_chat_id}")

            print(f'Channel #bot-chat´already exist in server, server ID: {server_id}')
            await ctx.send("There is already a channel in this server with the name 'bot-chat'")
            v0()
        else:
            create_channel = await guild.create_text_channel('bot-chat')
            print(create_channel.id)

        if discord.utils.get(guild.text_channels, name="quotes"):
            def v1():
                channel = discord.utils.get(ctx.guild.channels, name="quotes")
                quote_id = channel.id
                print(f"ID for channel #Quote {quote_id}")

            await ctx.send("There is already a channel in this server with the name 'quotes'")
            print(f'Channel #quotes already exist in server, server ID: {server_id}')
            v1()
        else:
            q_channel = await guild.create_text_channel('quotes')
            print(q_channel.id)

# The quote command
@commands.command(aliases=["q"])
async def quote(ctx, *, text):
    await bot.get_channel()

# Member count command
@commands.command()
async def members(ctx):
    id_s = bot.get_guild(764500927808798781)
    await ctx.send(f"# of Members: {id_s.member_count}")

# Check bot's ping
@commands.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** {round(bot.latency * 1000)}ms ')

# test with buttons
"""
@commands.command()
async def test(ctx):
    # Make a row of buttons
    row_of_buttons = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Green button",
            custom_id="green"
        ),
        Button(
            style=ButtonStyle.red,
            label="Red button",
            custom_id="red"
        )
    )
    # Send a message with buttons
    msg = await ctx.send(
        "This message has buttons!",
        components=[row_of_buttons]
    )

    # Wait for someone to click on them
    def check(inter):
        return inter.message.id == msg.id

    inter = await ctx.wait_for_button_click(check)
    # Send what you received
    button_text = inter.clicked_button.label
    await inter.reply(f"Button: {button_text}")
"""
"""
def seconds_until(hours, minutes):
    given_time = datetime.time(hours, minutes)
    now = datetime.datetime.now()
    future_exec = datetime.datetime.combine(now, given_time)
    if (future_exec - now).days < 0:  # If we are past the execution, it will take place tomorrow
        future_exec = datetime.datetime.combine(now + datetime.timedelta(days=1), given_time)  # days always >= 0

    return (future_exec - now).total_seconds()

slash = InteractionClient(bot)

@commands.command()
async def p(ctx, chour=None, cminut=None):
    if chour is None:
        await ctx.send("You must give hour and minute in a 24 hour clock time")
    elif cminut is None:
        await ctx.send("You must give hour and minute in a 24 hour clock time")
    else:
        @tasks.loop(seconds=5)
        async def for_ever_reminder():
            while True:
                await asyncio.sleep(
                    seconds_until(chour, cminut))  # Will stay here until your clock says {chour}{cminut}
                channel = bot.get_channel(897483967480074250)
                await channel.send(f"{ctx.message.author.mention}")
                await asyncio.sleep(
                    60)  # Practical solution to ensure that the print isn't spammed as long as it is 11:58

        scheduler = AsyncIOScheduler()
        scheduler.add_job(for_ever_reminder, CronTrigger(hour=chour, minute=cminut, second="0", ))
        scheduler.start()
        await ctx.send("**{0.user}".format(bot) + f"** will remind {chour}:{cminut}")

@commands.command()
async def pi(ctx, chour=None, cminute=None):
    if chour is None:
        await ctx.send("You must give hour and minute in a 24 hour clock time")
    elif cminute is None:
        await ctx.send("You must give hour and minute in a 24 hour clock time")
    else:
        async def for_ever_reminder():
            scheduler = AsyncIOScheduler()
            scheduler.add_job(for_ever_reminder, CronTrigger(hour=chour, minute=cminute, second="0", ))
            scheduler.start()

            @tasks.loop(minutes=cminute + chour * 60)
            async def start():
                while True:
                    await asyncio.sleep(
                        seconds_until(chour, cminute))  # Will stay here until your clock says {chour}{cminut}
                    channel = bot.get_channel(897483967480074250)
                    await channel.send(f"{ctx.message.author.mention}")
                    await asyncio.sleep(
                        60)  # Practical solution to ensure that the print isn't spammed as long as it is 11:58

            await ctx.send(f"Wew bot will remind {chour}:{cminute}")
"""

# Help command
@commands.command()  # Help command, command list
async def help(ctx, htype=None):
    if htype is None:
        help0 = discord.Embed(title=f"Help page:",
                              description=f"Im sorry u need help.",
                              color=discord.Color.purple())
        help1 = discord.Embed(title=f"Help page:",
                              description=f"Welcome to the help page, be specific with what you need help with by using one of the folders command below.",
                              color=discord.Color.purple())
        help1.add_field(name="Help with gamble", value="``?help gamble``")
        help1.add_field(name="Unknown", value="``Unknown``")
        help1.add_field(name="Unknown", value="``Unknown``")
        help1.add_field(name="Unknown", value="``Unknown``")
        help1.add_field(name="Unknown", value="``Unknown``")
        help1.add_field(name="Unknown", value="``Unknown``")
        help1.timestamp = datetime.utcnow()
        help1.set_footer(text='\u200b')
        message = await ctx.send(embed=help0)

        await asyncio.sleep(3)
        await message.edit(embed=help1)
    elif htype == "gamble":
        help_gamble = discord.Embed(title=f"Gamble help section",
                                    description=f"In TWG we got a our own gamble system with custom commands and prizes!",
                                    color=discord.Color.purple())
        help_gamble.add_field(name="Check bank:", value="``?balance``")
        help_gamble.add_field(name="Gamble stats:", value="``?statistics``")
        help_gamble.add_field(name="Transfer coins to user:", value=f"``?transfer``")
        help_gamble.add_field(name="Play slot machines:", value="``?slot <bet>``")
        help_gamble.add_field(name="Play dice gamble:", value="``?dice <dice number> <bet>``")
        help_gamble.add_field(name="Move coins to bank:", value="``?deposit <amount>``")
        help_gamble.add_field(name="Move coins to wallet:", value="``?withdraw <amount>``")
        help_gamble.add_field(name="Unknown:", value="``Unknown``")
        help_gamble.add_field(name="Unknown:", value="``Unknown``")


def setup(bot):
    bot.add_command(help)
    bot.add_command(setup1)
    bot.add_command(quote)
    """    
    bot.add_command(pi)
    bot.add_command(p)
    """
    bot.add_command(ping)
    bot.add_command(members)
    """
    bot.add_command(test)
    """
