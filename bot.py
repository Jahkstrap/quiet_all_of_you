import discord
import asyncio
from discord.ext import commands
import config
import os



intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command()
async def quiet(ctx):
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name='talk')
    if voice_channel:
        #connect to channel
        voice_client = await voice_channel.connect()

        #mute all
        for member in voice_channel.members:
            if member != bot.user: # don't mute the bot itself
                await member.edit(mute=True)

        #play sound
        file_name = 'quiet_all_of_you.mp3'
        file_path = os.path.join(os.getcwd(), file_name)
        voice_client.play(discord.FFmpegPCMAudio(file_name))

        await asyncio.sleep(3) # sleep for 3 seconds
        
        #unmute all
        for member in voice_channel.members:
            if member != bot.user: # don't unmute the bot itself
                await member.edit(mute=False)

        #fuck off
        await voice_client.disconnect()
    else:
        await ctx.send('The "talk" voice channel does not exist.')

bot.run(config.TOKEN)
