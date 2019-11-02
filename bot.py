"""
-get guild bot is in
-add functionality to qUp command
    -count down by checking which players launched the game (count up when someone closes the game?)
        -track by reacts instead??
    -timeout after watiting for players for so long
-error checking (game not found?)
-bots own channel? only handles 1 queue at a time??
"""
# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

msg_id = 0

@bot.event
async def on_ready():
    #guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        #f'{guild.name}(id: {guild.id})'
    )

@bot.command(name='qUp', help='Finds friends who are looking to play games!')
async def queue_up(ctx, game, number_of_players):
    global msg_id
    text = f'{ctx.author} wants {number_of_players} people to play {game}!'
    msg = await ctx.send(text)
    await msg.add_reaction('💯')
    msg_id = msg.id
    #print(msg.id)

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    #print(f'{message_id}\n{msg_id}')
    # and payload.user_id != bot.user_id
    #print(payload.user_id)
    if message_id == msg_id and payload.user_id != 640022874631176193:
        print('wow')

@queue_up.error
async def queue_up_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Usage: !qUp <game> <number of players>')

#keep this at the bottom
bot.run(TOKEN)
"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return
"""
