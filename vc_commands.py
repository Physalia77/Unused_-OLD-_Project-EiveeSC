# Imports
from main import *

"""
Voice-Chat commands
"""


class vc_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    # Joins VC
    @commands.command()
    async def join(ctx):
        if ctx.author.voice is None:
            await ctx.send(f"Please, may {ctx.author} join a voice channel for me to direct to!")

        voice_channel = ctx.author.voice.channel
        if ctx.voice_commands is None:
            await voice_channel.connect()
        else:
            await ctx.voice_commands.move_to(voice_channel)

    # The bot leave's
    @commands.command()
    async def leave(ctx):
        await ctx.voice_commands.disconnect()

    # The bot plays the music
    @commands.command()
    async def play(ctx, url):
        ctx.voice_commands.stop()
        FFMPEG_OPTIONS = {'before_option': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay-max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_commands

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['format'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    # Pause
    @commands.command()
    async def pause(ctx):
        await ctx.voice_commands.pause()
        await ctx.send("It has been done!")

    # Resume
    @commands.command()
    async def resume(ctx):
        await ctx.voice_commands.resume()
        await ctx.send("It has been done!")


def setup(bot: commands.Bot):
    bot.add_cog(vc_c(bot))
