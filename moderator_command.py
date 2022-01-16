# Moderator commands
from main import *


# Moderator commands
# Kick
@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
@commands.has_role('Staff')
async def kick(ctx, member: discord.Member = None, *, reason=None):
    Staff = discord.utils.get(ctx.guild.roles, name='Staff')
    Owner = discord.utils.get(ctx.guild.roles, name='Chairperson')

    if member == None:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f'**{ctx.message.author}**, please mention somebody to kick.', color=0xFFC200))

    if member == ctx.message.author:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"**{ctx.message.author}**, you cannot kick yourself, silly.", color=0xFFC200))

    if member.bot:
        if Owner in member.roles:
            log_channel = bot.get_channel(902599258857955348)
            await member.kick()
            log = discord.Embed(
                description='User **' + member.display_name + f'** has been kicked. \n **Reason:** {reason}',
                color=0xf30000)
            await ctx.send(embed=log)
            await log_channel.send(embed=log)
        else:
            return await ctx.message.channel.send(
                embed=discord.Embed(
                    description=f"You can not kick **" + format(member) + "** bots.".format(member), color=0xFFC200))

    if Staff in member.roles:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"**{ctx.message.author}**, you can't kick another staff member. :warning:",
                color=0xFFC200))

    if member.dm_channel is None:
        await member.create_dm()
    await member.dm_channel.send(
        embed=discord.Embed(description=f'You have been kicked from **{ctx.guild}** by **{ctx.message.author}**. \n '
                                        f'**Reason:** {reason} ', color=0xf30000))
    log_channel = bot.get_channel(902599258857955348)
    await member.kick()
    log = discord.Embed(description='User **' + member.display_name + f'** has been kicked by **{ctx.message.author}**'
                                                                      f'. \n **Reason:** {reason}',
                        color=0xf30000)
    await ctx.send(embed=log)
    await log_channel.send(embed=log)
    print('User **' + member.display_name + f'** has been kicked by **{ctx.message.author}**. \n **Reason:** {reason}')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        error_kick = discord.Embed(description="You don't have permission to ban members:exclamation:", color=0xFFC200)
        await ctx.message.channel.send(embed=error_kick)


# Ban
@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
@commands.has_role('Staff')
async def ban(ctx, member: discord.Member = None, *, reason=None):
    Staff = discord.utils.get(ctx.guild.roles, name='Staff')

    if member == None:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f'**{ctx.message.author}**, please mention somebody to ban.', color=0xFFC200))

    if member == ctx.message.author:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"**{ctx.message.author}**, you cannot ban yourself, silly.", color=0xFFC200))

    if member.bot:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"You can not ban **" + format(member) + "** because the member is a bot.".format(member),
                color=0xFFC200))

    if Staff in member.roles:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"**{ctx.message.author}**, you can't ban another staff member. :warning:", color=0xFFC200))

    if member.dm_channel is None:
        await member.create_dm()
    await member.dm_channel.send(embed=discord.Embed(
        description=f"You have been banned from **{ctx.guild}** by **{ctx.message.author}** \n **Reason:** {reason} ",
        color=0xf30000))

    await member.ban(reason=reason)
    ban_log = discord.Embed(description=f'User **' + member.display_name + f'** has been banned by '
                                                                           f'**{ctx.message.author}**.'
                                                                           f' \n **Reason:** ' + reason,
                            color=0xf30000)

    a_log_channel = bot.get_channel(902599258857955348)
    await a_log_channel.send(embed=ban_log)
    await ctx.send(embed=ban_log)
    print(f'User **' + member.display_name + f'** has been banned by '
                                             f'**{ctx.message.author}**.'
                                             f' \n **Reason:** ' + reason)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        error_ban = discord.Embed(description="You don't have permission to ban members :warning:", color=0xFFC200)
        await ctx.message.channel.send(embed=error_ban)


# Unban
@bot.command(name='unban', pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.has_role('Staff')
async def unban(ctx, *, member: discord.Member = None):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_user:
        user = ban_entry.user

        if member == None:
            return await ctx.message.channel.send(
                embed=discord.Embed(
                    description=f'**{ctx.message.author}**, please mention somebody to ban.', color=0xFFC200))

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            log_channel = bot.get_channel(902599258857955348)
            await ctx.guild.unban(user)
            embed = discord.Embed(description=f"**{ctx.message.author}** unbanned {user.mention}!")
            save_log_unban = discord.Embed(description=f"**{ctx.message.author}** unbanned {user.mention}!")
            await ctx.send(embed=embed)
            await log_channel.send(embed=save_log_unban)
            print(f"**{ctx.message.author}** unbanned {user.mention}!")
            return


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        error_unban = discord.Embed(description="You don't have permission to ban members :warning:", color=0xFFC200)
        await ctx.message.channel.send(embed=error_unban)


# Mute
@bot.command(name='mute')
@commands.has_role('Staff')
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member = None, *, reason=None):
    log_channel = bot.get_channel(902599258857955348)
    add_role = discord.utils.get(ctx.guild.roles, name='Muted')

    if member == None:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f'**{ctx.message.author},** please mention somebody to mute.', color=0xFFC200))

    if member == ctx.message.author:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"**{ctx.message.author},** you cannot mute yourself, silly.", color=0xFFC200))

    if member.bot:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description=f"You can not mute **" + format(member) + "** because the member is a bot.".format(member),
                color=0xFFC200))

    if add_role in member.roles:
        return await ctx.message.channel.send(
            embed=discord.Embed(
                description="**{}** is already muted. :warning:".format(member), color=0xFFC200))

    else:
        await member.add_roles(add_role, reason=reason)
        mute_log = discord.Embed(description=f'User {member.display_name} has been muted. \n**Reason:** '
                                             f'{reason if reason is not None else "None"}', color=0xf30000)
        await ctx.send(embed=mute_log)
        await log_channel.send(embed=mute_log)
        print(f'User {member.display_name} has been muted. \n**Reason:** {reason if reason is not None else "None"}')


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        error_mute = discord.Embed(description="You don't have permission to ban members :warning:",
                                   color=0xFFC200)
        await ctx.message.channel.send(embed=error_mute)


# Un mute
@bot.command(name='unmute', pass_context=True)
@commands.has_role('Staff')
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
    log_channel = bot.get_channel(902599258857955348)

    guild = ctx.guild
    user = member

    if member == None:
        await ctx.send(f'**{ctx.message.author},** please mention somebody to unmute.')
        return

    if member == ctx.message.author:
        await ctx.send(f'**{ctx.message.author},** wtf... what do u mean bro.')
        return

    for role in guild.roles:
        if role.name == "Muted":
            if role in user.roles:
                await member.remove_roles(muted_role)
                unmute_log = discord.Embed(
                    description='User **' + member.display_name + '** have been unmuted. ',
                    color=0xf30000)
                await ctx.send(embed=unmute_log)
                await log_channel.send(embed=unmute_log)
                print(f'User **' + member.display_name + '** have been unmuted.')
                return
            else:
                await ctx.send(f"Can't mute **{ctx.message.author}** because he/she is not muted.")


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        error_unmute = discord.Embed(description="You don't have permission to unmute members :warning:",
                                     color=0xFFC200)
        await ctx.message.channel.send(embed=error_unmute)


# clear [Amount] messages
@bot.command(aliases=["msgclear"])
async def clear(ctx, amount):
    amount = int(amount)
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} messages deleted!", delete_after=5)
    print(f"{amount} messages deleted!")


@bot.command(name='r')
async def r(ctx, *, reason=None):
    await bot.get_channel(784414610027446292).send(embed=discord.Embed(description=f"{ctx.message.author} "
                                                                                   f"\n **Reported:** " + reason))


def setup(bot):
    bot.add_command(r)
    bot.add_command(clear)
    bot.add_command(unmute)
    bot.add_command(mute)
    bot.add_command(unban)
    bot.add_command(ban)
    bot.add_command(kick)
