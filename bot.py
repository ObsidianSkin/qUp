"""
-add functionality to qUp command
    -count down by checking which players launched the game (count up when someone closes the game?)
        -track by reacts instead??
    -timeout after watiting for players for so long
-error checking (game not found?, same user filling multiple spots, clicking on eggplant does nothing??, )
-bots own channel? only handles 1 queue at a time??
-clean up qup
-react with role to recieve challenel notifications? or only for specific games? => how?
-or just recieve notification all the time??
-send message when someone starts a game and listen for those messages? => also how

# TODO:
-assign roles?
-user sends request looking for game friends (done? trim the fat?)
-xtimeout after ~30min if not enough players found
-send user analytics to website for analytical stuff. redirect user and post players game activity
-xdisplay users as they join + xx?look into launching game as way to keep track??
-more bot functionality:
    -xxmore modular and customizable
    -xxsome useless/fun commands!
        -bup command
    -other stuff??
    -integrate giphy?
"""
# bot.py
import os
import requests
import discord
import json
import pprint
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')
pp = pprint.PrettyPrinter()

guild = '' #guild the bot and users belong to (channel)
msg = '' #msg that holds reactions and changes when timer runs out/squad is full
msg_id = 0 #tracks reactions on specific bot message (<msg.id>)
num_players = 0 #number of players request at the time of !qUp
user_ids = [] #user_ids of players who've reacted (not including author. user_ids only counts additional players)
author = '' #user who called !qUp ...
game_name = '' #name of game (<name>) to be played

def get_member_list(members):
    #user firebase info sent here! (those interested and non interested)
    #-discord name
    #-discord tag
    #-activity (if any)
    #-eagerness (did thdey react to the essage?)
    #-server (should be the same for all of them)
    #-discord avatar
    #handle inactive users differently? nu
    inactive = 0
    membersN = []
    i = 0
    for member in members:
        i += 1
        #loop through user_ids and compare to get eagerness
        eagerness = False
        for id in user_ids:
            if id == member.id or id == author.id:
                eagerness = True
        inmember = {"discordName": member.display_name, "discordTag": member.discriminator, 'avatarURL':  ('https://cdn.discordapp.com/avatars/' + str(member.discriminator) + '/' + str(member.avatar) + '.png'), "looking":False }
        membersN.append(inmember)
    print(membersN)
    r = requests.post('http://www.queueUp.tech/user', json=membersN)
    print(r.status_code) #console log

    pp.pprint(f'inactive players {inactive}')

@bot.event
async def on_ready():
    global guild
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

def get_emoji(number_of_players):
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
    global game_name
    global guild

    user_ids = []
    num_players = number_of_players - 1
    author = ctx.author
    game_name = game
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

    get_member_list(guild.members) #getting guild memebers on !qUp ... call
"""
#add random bups!
@bot.command(name='bup', help='bup. that\'s it')
async def bup_alert(ctx):
    if not client.is_voice_connected(ctx.message.server):
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
    else:
        voice = client.voice_client_in(ctx.message.server)

    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=yKt0kG64Ev8&list=PLff_NK5jtKi1blKP4N1MRriXDqs4_TcFy&index=1', after=toggle_next)
    await songs.put(player)

def toggle_next():
    client.loop.call_soon_threadsafe(play_next_song.set)

@bot.command(name='join', help='Pepe joins your voice channel.')
async def join_voice(ctx):
    voice = await client.join_voice_channel(ctx.message.author.voice_channel)

@bot.command(name='leave', help='Pepe leaves your voice channel.')
async def leave_voice(ctx):
    voice_client = bot.voice_client_in(ctx.message.server)
    await voice_client.disconnect()
"""
@bot.event
async def on_raw_reaction_add(payload):
    global msg
    global num_players
    global author
    global game_name

    message_id = payload.message_id
    message = ''

    #times out after 30 min, also add ability for players to become uninterested??
    #check for duplicate user ids?
    if message_id == msg_id and payload.user_id != 640022874631176193:
        #print(num_players)
        if num_players >= 0:
            print('\n')
            user_ids.append(payload.user_id)
            get_member_list(guild.members) #updating member list (+1 interested player)
            if(num_players == 0):
                print(user_ids)
                message += 'Attention '
                for id in user_ids:
                    message += f'<@{id}> '
                message += f'and <@{author.id}>! You have enough players for {game_name}, so get goin\'!'
                await msg.edit(content=message)

            await msg.clear_reactions()
            num_players -= 1
            emoji = get_emoji(num_players)
            await msg.add_reaction(emoji)

@queue_up.error
async def queue_up_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Usage: !qUp <game> <number of players>')

#keep this at the bottom
bot.run(TOKEN)
