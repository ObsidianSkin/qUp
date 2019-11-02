"""
-get guild bot is in
-add functionality to qUp command
    -count down by checking which players launched the game (count up when someone closes the game?)
        -track by reacts instead??
    -timeout after watiting for players for so long
-error checking (game not found?, same user filling multiple spots, clicking on eggplant does nothing??, )
-bots own channel? only handles 1 queue at a time??
-clean up qup
"""
# bot.py
import os

import discord
import pprint
from discord.ext import commands
from dotenv import load_dotenv

pp = pprint.PrettyPrinter()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

msg = ''
msg_id = 0
num_players = 0
user_ids = []
author = ''

def get_member_list(members):
    inactive = 0
    for member in members:
        if member.activity is None:
            inactive += 1
        else:
            pp.pprint(member.activity)

    pp.pprint(f'inactive players {inactive}')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        #f'{guild.name}(id: {guild.id})'
    )
    get_member_list(guild.members)

def get_emoji(number_of_players):
    #await msg.clear_reactions()
    #lovely block of garbage :)
    if number_of_players == 0:
        return '0⃣'
    elif number_of_players == 1:
        return '1⃣'
    elif number_of_players == 2:
        return '2⃣'
    elif number_of_players == 3:
        return '3⃣'
    elif number_of_players == 4:
        return '4⃣'
    elif number_of_players == 5:
        return '5⃣'
    elif number_of_players == 6:
        return '6⃣'
    elif number_of_players == 7:
        return '7⃣'
    elif number_of_players == 8:
        return '8⃣'
    elif number_of_players == 9:
        return '9⃣'
    elif number_of_players == 10:
        return '🔟'
    else:
        return '🍆'

@bot.command(name='qUp', help='Finds friends who are looking to play games!')
async def queue_up(ctx, game, number_of_players: int):
    global msg
    global msg_id
    global num_players
    global user_ids
    global author

    user_ids = []
    num_players = number_of_players - 1
    author = ctx.author
    text = f'{ctx.author} wants {number_of_players} people to play {game}!'
    msg = await ctx.send(text)

    #lovely block of garbage :)
    if num_players == 0:
        await msg.add_reaction('0⃣')
    elif num_players == 1:
        await msg.add_reaction('1⃣')
    elif num_players == 2:
        await msg.add_reaction('2⃣')
    elif num_players == 3:
        await msg.add_reaction('3⃣')
    elif num_players == 4:
        await msg.add_reaction('4⃣')
    elif num_players == 5:
        await msg.add_reaction('5⃣')
    elif num_players == 6:
        await msg.add_reaction('6⃣')
    elif num_players == 7:
        await msg.add_reaction('7⃣')
    elif num_players == 8:
        await msg.add_reaction('8⃣')
    elif num_players == 9:
        await msg.add_reaction('9⃣')
    elif num_players == 10:
        await msg.add_reaction('🔟')
    else:
        await msg.add_reaction('🍆')

    msg_id = msg.id

@bot.event
async def on_raw_reaction_add(payload):
    global msg
    global num_players
    global author

    message_id = payload.message_id
    message = ''

    if message_id == msg_id and payload.user_id != 640022874631176193:
        print(num_players)
        user_ids.append(payload.user_id)
        if(num_players == 0):
            print(user_ids)
            message += 'Attention '
            for id in user_ids:
                message += f'<@{id}> '
            message += f'and <@{author.id}>! You have enough players, so get goin\'!'
            await msg.edit(content=message)

        await msg.clear_reactions()
        num_players -= 1
        emoji = get_emoji(num_players)
        await msg.add_reaction(emoji)
        #num_players -= 1
        #get_emoji(num_players)
        #queue_up.invoke

#def notify_users():
#    for id in user_ids:


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
