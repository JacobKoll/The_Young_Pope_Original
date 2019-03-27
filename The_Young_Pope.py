import discord
import asyncio
import random
from discord import opus
from discord.ext import commands


bot = commands.Bot(command_prefix='.')

# This gives the user login information to the console. test

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('===================================')


# This adds announcements for when users mute, deafen, leave, or move.

@bot.event
async def on_voice_state_update(before, after):
    try:
        if not before.self_mute and after.self_mute:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has muted themself.')

        if before.self_mute and not after.self_mute:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has un-muted themself.')

        if not before.self_deaf and after.self_deaf:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has deafened themself.')

        if before.self_deaf and not after.self_deaf:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has un-deafened themself.')

        elif not before.mute and after.mute:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has been muted.')

        elif before.mute and not after.mute:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has been un-muted.')

        elif not before.deaf and after.deaf:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has been deafened.')

        elif before.deaf and not after.deaf:
            await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has been un-deafened.')

        elif before.voice_channel != after.voice_channel:
            if str(after.voice_channel) == 'None':
                await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has left the server.')
            else:
                await bot.send_message(discord.Object(id = '338770103778672641'), after.display_name + ' Has moved to ' + str(after.voice_channel) + '.')
    except discord.ClientException:
        pass
    except discord.errors.HTTPException:
        pass

# recieves a user message.

@bot.event
async def on_message(message):
    if random.randint(0,99) == 50:
        await bot.send_file(message.author, 'TheYoungPope.jpg')
    if message.channel.id == '284688856748523520':
        await bot.process_commands(message)
# Rolls any number sided dice any number of times.

@bot.command()
async def roll(dice : str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.send_message(discord.Object(id = '284688856748523520'), 'Format has to be in "Number of Dice"d"Number of Sides", for example ".roll 3d5"!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.send_message(discord.Object(id = '284688856748523520'), result)

# Plays a sound file in the channel it was called in.

@bot.command(pass_context = True)
async def fogman(ctx, member: discord.Member = None):
    try:
        channel = ctx.message.author.voice.voice_channel
        voice = await bot.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('FogMan.mp3')
        await asyncio.sleep(1)
        player.volume = 0.1
        player.start()
        await asyncio.sleep(5)
        player.stop()
        await bot.voice_client_in(ctx.message.server).disconnect()
    except discord.ClientException:
        await bot.send_message(discord.Object(id = '284688856748523520'), 'Wait your turn!')



bot.run('MzM4MTY4MjkyNDYyMDM0OTU0.DFR2eg.EfzFNn2HGc9uJwXzKCLAJnJCv3A')
