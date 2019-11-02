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
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

msg = ''
msg_id = 0
num_players = 0
user_ids = []
author = ''

@bot.event
async def on_ready():
    #guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        #f'{guild.name}(id: {guild.id})'
    )

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
    """
    emoji = ''
    def switch_emoji(number_of_players):
        switcher = {
            0: '0⃣',
            1: '1⃣',
            2: '2⃣',
            3: '3⃣',
            4: '4⃣',
            5: '5⃣',
            6: '6⃣',
            7: '7⃣',
            8: '8⃣',
            9: '9⃣',
            10: '🔟',
        }
        print(number_of_players)
        emoji = switcher.get(number_of_players)
        #print(emoji)
    """

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

    #get_emoji(number_of_players)

    #switch_emoji(number_of_players)
    #await msg.add_reaction('💯')
    #await msg.add_reaction(emoji)
    #await msg.add_reaction('0⃣')
    msg_id = msg.id
    #print(msg.id)

@bot.event
async def on_raw_reaction_add(payload):
    global msg
    global num_players
    global author
    #global num_players
    message_id = payload.message_id
    message = ''
    #print(f'{message_id}\n{msg_id}')
    # and payload.user_id != bot.user_id
    #print(payload.user_id)
    if message_id == msg_id and payload.user_id != 640022874631176193:
        #print('wow')
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
