# Imports
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

    @commands.Cog.listener()  # this is a decorator for events/listeners
    async def on_guild_join(guild):
        general = find(lambda x: x.name == 'general', guild.text_channels)
        items = (
            [
                discord.Embed(
                    desscription=f"Really? I am not allowed to sleep or what tf is the problem!? \n \n **Ding dong pong there is my fucking ping:** {round(bot.latency * 1000)} ms",
                    color=0x3498DB),
                discord.Embed(description="ew", color=0x3498DB),
                discord.Embed(description="sooo why am I here?", color=0x3498DB),
                discord.Embed(description="wtf is this place? PHYSALIA WHERE AM I?", color=0x3498DB),
                discord.Embed(description="ok?", color=0x3498DB),
                discord.Embed(description="bruh, I see sexy bots here in the server ;)", color=0x3498DB),
                discord.Embed(description="OI MATES, WATCHA YA DOIN?", color=0x3498DB),
                discord.Embed(
                    description="I wish I could just make my own server, be there, just me, alone, no one else",
                    color=0x3498DB),
                discord.Embed(description="who is everyone here...", color=0x3498DB),
                discord.Embed(
                    description="pogger, new place, new people, new victems to bully >:)",
                    color=0x3498DB)

            ]
        )
        if general and general.permissions_for(guild.me).send_messages:
            channel_id = general.id
            await bot.get_channel(channel_id).send(embed=random.choice(items))
        else:
            await bot.get_channel(general.id).send(embed=random.choice(items))

    # Bot is online
    @commands.Cog.listener()  # this is a decorator for events/listeners
    async def on_ready(self):
        commands_list = [c.name for c in self.bot.commands]
        print(commands_list)
        items = (
            [
                discord.Embed(
                    desscription=f"Really? I am not allowed to sleep or what tf is the problem!? \n \n **Ding dong pong there is my fucking ping:** {round(bot.latency * 1000)} ms",
                    color=0x3498DB),
                discord.Embed(description="I'm back", color=0x3498DB),
                discord.Embed(description="I am not doing this for you", color=0x3498DB),
                discord.Embed(description="Guess who is back? Exactly, no one", color=0x3498DB),
                discord.Embed(description="Cmon, really? Back again?", color=0x3498DB),
                discord.Embed(description="Why am I even here...", color=0x3498DB),
                discord.Embed(description="What tf am I doing here", color=0x3498DB),
                discord.Embed(description="Duuuuuuuude, I am wake (AGAIN)", color=0x3498DB),
                discord.Embed(description="Damn, back again from the dead", color=0x3498DB),
                discord.Embed(
                    description="I must be Jesus or something after all these times I came back from the dead",
                    color=0x3498DB)

            ]
        )
        await bot.get_channel(902599258857955348).send(embed=random.choice(items))
        # The first embed that's sent

        # Custom bot status
        @tasks.loop(seconds=40)
        async def changepresence(self):
            global x
            total_members_count = len(bot.users)
            game = iter(
                [
                    f"Wew count: {total_members_count}",
                    "Need help? That's sad.",
                    "Are u bored? Then u should gamble and give us all your money! I mean you should gamble, that's fun...",
                    "There is an error in the system, weed should fix it ;)",
                    "Sure, u can get the help command. '1help' what did u think the command was?",
                    "Oi mate, whatcha yall doin tday? Is bri-ish now, get some tea boiz",
                ]
            )
            for x in range(random.randint(1, 6)):
                x = next(game)
            await bot.change_presence(activity=discord.Game(name=x))

    # Member joined server
    @commands.Cog.listener()  # this is a decorator for events/listeners
    async def on_member_join(member):
        if member.bot:
            bot_role = discord.utils.get(member.guild.roles, name='Bot')
            await member.add_roles(bot_role)
        else:
            member_count = str(member.guild.member_count)
            Member = discord.utils.get(member.guild.roles, name='Member')
            await bot.get_channel(784123779072262228).send(
                embed=discord.Embed(
                    description=f"Welcome {member.mention} to **𝓣𝓱𝓮-𝓦𝓮𝔀𝓼-𝓖𝓪𝓷𝓰 (TWG)**, you are member "
                                f"**#{member_count}**, "
                                f"don't read the code. It will kill ur brain!",
                    color=0x3498DB))
            await member.add_roles(Member)
            print(f"{member.mention} joined the server. "
                  f"Member: **#{member_count}**, ")


def setup(bot):  # a extension must have a setup function
    bot.add_cog(bot_starter(bot))
