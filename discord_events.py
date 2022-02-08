# Imports
import sqlite3

from main import *

"""
BOT JOINS SERVER/AUTO MESSAGES
(NO COMMANDS)
"""
bot.get_cog('bot_all_commands')


# Bot joins server/auto msg


class bot_starter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None
        self.user = None

    @commands.Cog.listener()  # this is a decorator for events/listeners
    async def on_guild_join(self, guild):
        print(
            f"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n \n{self.bot.user.name} joined *{guild.name}* \n   Server ID: {guild.id} \n   Amount of members: {len(guild.members)}")

        with open('../json/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '?'

        with open('../json/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        join_bed = discord.Embed(title="\n",
                                 description=f"Hi everyone, I'm **{self.bot.user.name}** I hope you all are going to be pleased with my service, "
                                             f"if you have any questions you can use the command `?help` or if you got something to "
                                             f"report/suggest you can then tell my developers Physalia77 and ScreamsinMeow about it on github.",
                                 color=0x3457db)
        join_bed.set_author(name=self.bot.user.name,
                            icon_url=self.bot.user.avatar_url)
        join_bed.set_footer(text=
                            "\n OBS: THIS IS NOT A FINISH PROJECT, AND MANY THINGS CAN AND WILL BE CHANGED LIKE COMMANDS, BOT NAME, PROFILE PICTURE AND MORE", )

        await guild.text_channels[0].send(embed=join_bed)

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member, message, guild):
        members = message.guild.members  # also works with ctx.guild.members
        bot_role = discord.utils.get(member.guild.roles, name='Bot')
        for member in members:
            if member.bot:
                if get(ctx.guild.roles, name="Bot"):
                    await member.add_roles(bot_role)
                else:
                    role = await ctx.guild.create_role(name="Bot", permissions=discord.Permissions(8),
                                                       colour=discord.Colour(0xff0000))
                    bot_role = discord.utils.get(member.guild.roles, name='Bot')
                    await member.add_roles(bot_role)

            else:
                member_count = str(member.guild.member_count)
                await guild.text_channels[0].send(
                    embed=discord.Embed(
                        description=f"Welcome {member.mention} to **{guild.name}**, you are member "
                                    f"**#{member_count}**, ",
                        color=0x3457db))
                print(f"{member.mention} joined the server. "
                      f"Member: **#{member_count}**, ")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('../json/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('../json/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    # Bot is online
    @commands.Cog.listener()  # this is a decorator for events/listeners
    async def on_ready(self):
        # The first embed that's sent
        print(
            f'\n{datetime.now()}: \nBot logged in as {self.bot.user.name} \n   ID: {self.bot.user.id}\n   Discord.py Version: {discord.__version__} \n Servers: {len(self.bot.guilds)} \n Users: {len(bot.users)}')
        print()

    # Member joined server


def setup(bot):  # a extension must have a setup function
    bot.add_cog(bot_starter(bot))
