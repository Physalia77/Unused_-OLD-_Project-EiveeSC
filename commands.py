from main import *

"""
All commands for The Knight Bot
"""


class c_cog(commands.Cog):
    def init(self, Bot):
        pass

    # Commands
    # Setup command
    @commands.command(aliases=["setup"])
    async def setup1(self, ctx):
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
    async def quote(self, ctx, *, text):
        await bot.get_channel()

    # Member count command
    @commands.command()
    async def members(self, ctx):
        id_s = bot.get_guild(764500927808798781)
        await ctx.send(f"# of Members: {id_s.member_count}")

    # test with buttons

    # Help command
    @commands.command()  # Help command, command list
    async def help(self, ctx, htype=None):
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
        elif htype == "casino":
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
            await ctx.send(embed=help_gamble)

    #   Server Information
    @commands.command(aliases=["server"])
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        server_id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        member_count = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=0x007011
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner:", value=owner, inline=True)
        embed.add_field(name="Server ID:", value=server_id, inline=True)
        embed.add_field(name="Region:", value=region, inline=True)
        embed.add_field(name="Member Count:", value=member_count, inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/776904474458980364/785904953868550194/RoseCliff_'
                'Test_3.png')

        await ctx.send(embed=embed)
        print(f'{ctx.message.author} said - "!server"')

    @commands.command()
    async def time(self, ctx, *, clock: str = None):
        if clock is None:
            await ctx.send("You must give a clock time")


def setup(bot):
    bot.add_cog(c_cog(bot))
