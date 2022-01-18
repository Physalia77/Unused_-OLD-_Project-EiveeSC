# Imports
from main import *

"""
Voice-Chat commands
"""


class main(commands.Cog):
    def init(self, Bot):
        pass

    # Joins VC
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"Please, may {ctx.author} join a voice channel for me to direct to!")

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    # The bot leave's
    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    # The bot plays the music
    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_commands.stop()
        FFMPEG_OPTIONS = {'before_option': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay-max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['format'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    # Pause
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("It has been done!")

    # Resume
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("It has been done!")


def setup(bot):
    bot.add_cog(main(bot))
