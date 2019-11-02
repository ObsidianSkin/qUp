"""
-print !help 1 time
-get guild bot is in
-add functionality to qUp command
"""
# bot.py
import os

#import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')
"""
@bot.event
async def on_ready():
    #guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        #f'{guild.name}(id: {guild.id})'
    )
"""
@bot.command(name='qUp', help='Finds friends who are looking to play games!')
async def queue_up(ctx, game, number_of_players):
    response = f'{ctx.author} wants {number_of_players} people to play {game}!'
    await ctx.send(response)

bot.run(TOKEN)
"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return
"""
