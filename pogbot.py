"""
cmds :-
actions:
  slap
​No Category:
  Pog
  _8ball
  adinub
  botinvite
  clear
  cowsay
  createinvite
  disable
  enable
  guilds
  help
  ping
  repeat
  shutdown
  spam

"""

token_file = open("token.txt", 'r')
TOKEN = token_file.read()
token_file.close()


# owner.get('name') ;-;
owner ={
'name' : 'Atriays',
'hash' : '2984',
'id' : 543718305773387776 }

#LIBRARIES
import discord
from discord.ext import commands
from discord.utils import get

from discord import member

import datetime
from datetime import datetime

import random
from random import choice

import pandas as pd

import os

from PIL import Image

import requests
from io import  BytesIO

#from youtube_search import YoutubeSearch
#import youtube_dl
import asyncio

#---------------------------------------------------------------------------------#


# Prefix
prefix = [".", '<@!779225458159386624> ']

# Permission for intents
intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)

# setting the discord bot thinga majik
client = commands.Bot(command_prefix= prefix,
                      intents=intents , help_command=None) #, help_command=None

#todaynow = datetime.now().strftime("%d/%m/%Y  %H:%M")

# Conditions for commands :-
# example code ;-; - @commands.check(is_Atriays or is_Mutant or is_Nerdy or has_permissions(administrator=True))
def is_Atriays(ctx):
    return ctx.author.id == 543718305773387776;

def is_Mutant(ctx):
    return ctx.author.id == 460335920260841482;

def is_Nerdy(ctx):
    return ctx.author.id == 516173155216392193;



# Help cmd (help)
@client.command(aliases=['help'])
async def _help(ctx):
    helpembed = discord.Embed(
        title="Commands", description="Commands available in Atriays's Pog Bot", color=0x3fc2c9)
    helpembed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/779225458159386624/f3ba776ec26d2b00811a33d60ddea532.png?size=1024")
    helpembed.set_author(name="Atriays's Pog Bot", url="https://cdn.discordapp.com/avatars/779225458159386624/f3ba776ec26d2b00811a33d60ddea532.png?size=1024",
                         icon_url="https://cdn.discordapp.com/avatars/779225458159386624/f3ba776ec26d2b00811a33d60ddea532.png?size=1024")
    helpembed.add_field(
        name="Help", value=f"This Command. *Usage - {prefix[0]}help* => Shows this embed", inline=False)
    helpembed.add_field(
        name="Clear", value=f"Clears chat upto a point. *Usage - {prefix[0]}clear 10* => Clears 10 chat before the command. ", inline=False)
    helpembed.add_field(
        name="Repeat", value=f'Repeats anything you say. (max: 100 times) *Usage - {prefix[0]}Repeat 5 Hi I am Pog=>* Repeats "Hi I am Pog" 10 times.', inline=False)
    helpembed.add_field(
        name="Spam", value=f"Spams a user. (max: 5 times) *Usage - {prefix[0]}spam 2 @User =>* Spam pings the user 2 times.", inline=False)
    helpembed.add_field(
        name="Ping", value=f"Shows the bot's ping. *Usage - {prefix[0]}Ping*", inline=False)
    helpembed.add_field(
        name="adinub", value=f"Shows the Universal Truth", inline=False)
    helpembed.add_field(
        name="8Ball", value=f"A general 8ball command. *Usage - {prefix[0]}8ball Am i pog? =>* Gives you a random answer.", inline=False)
    helpembed.add_field(
        name="pog", value=f"Tells you if the statement is pog or not. *Usage - {prefix[0]}pog u r a poopi*", inline=False)
    helpembed.add_field(
        name="slap", value=f"slaps the user you mentioned. *Usage - {prefix[0]}slap @user*", inline=False)
    # await ctx.send(embed = helpembed)
    await ctx.author.send(embed=helpembed)

    dmembed = discord.Embed(
        title=f'{ctx.author}, Check Your DM', color=0x3fc2c9)
    msg = await ctx.send(embed=dmembed)
    await msg.add_reaction(u'\u2705')


# pog or not pog cmd (pog)
# respnses for pog or not pog
pogresponses = ['pog', 'not pog', 'Pog', 'Not Pog']


@client.command(aliases=['pog', 'POG'])
async def Pog(ctx, *, pog_notpog):
    pog_notpog.author: discord.Member
    # await ctx.send(f"`{pog_notpog}` \nHmmmm.\n{ctx.author.mention} That was {random.choice(pogresponses)}.")
    # description =f'**{pog_notpog}**'
    pogembed = discord.Embed(title="Pog Or Not Pog", color=0xffcc26)
    pogembed.add_field(
        name=f"*`{pog_notpog}`*", value=f'Hmmmmmm \n**That was {random.choice(pogresponses)}**')
    pogembed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/735404390843809826/780086292733886484/My_Video.gif")
    await ctx.send(embed=pogembed)


# clear cmd (clear)
@client.command(aliases = ['purge'])
@commands.check(is_Atriays or is_Mutant or is_Nerdy or has_permissions(administrator=True))
async def clear(ctx, amount=1):
    await ctx.message.delete()
    #await str(cleared_msgs[0])[12:30]).delete()


    cleared_msgs = await ctx.channel.purge(limit=amount)

    purge_embed = discord.Embed(title = f'Deleted {amount} message(s)' , color = 0x3fc2c9)
    await ctx.send(embed = purge_embed , delete_after = 1.7)

    print(f'{ctx.author} cleared {amount} msg(s)')

    df = pd.read_csv(r"./output/output.csv" , index_col = 0)
    df = df.append({'guild_id' : f'{ctx.guild.id}' , 'guild_name' : ctx.guild , 'user_id' : f'{ctx.author.id}' , 'user_name' : ctx.author , 'numb_msgs_del_requested' : amount , 'date-time' : datetime.now().strftime("%d/%m/%Y  %H:%M")} , ignore_index=True)
    df.to_csv(r'./output/output.csv' , index = False)



# repeat cmd
@client.command()
async def repeat(ctx, numrepeat=2, *, repeatthis):
    if (numrepeat >= 1 and numrepeat <= 30):
        for numrepeat in range(1, numrepeat+1):
            await ctx.send(repeatthis)
            numrepeat = numrepeat - 1




# spam cmd
@client.command()
async def spam(ctx, numspam=2, * , pingmember: discord.Member):
    if (numspam >= 1 and numspam <= 5):
        for numspam in range(1, numspam+1):
            await ctx.send(pingmember.mention)
            numspam = numspam - 1


@client.command()
async def ping(ctx):
    dmembed = discord.Embed(
        title=f'Poggers!! \nThe Ping is {round(client.latency * 1000)}ms', color=0x3fc2c9)
    msg = await ctx.send(embed=dmembed)
    await msg.add_reaction(u'\U0001F1F5')
    await msg.add_reaction(u'\U0001F1F4')
    await msg.add_reaction(u'\U0001F1F3')
    await msg.add_reaction(u'\U0001F1EC')


@client.command()
async def adinub(ctx):
    await ctx.send('Adinub is the biggest poopi') #discord.User(id = 543718305773387776).mention



ballresponses = [
    # positive
    'Yesss',
    'Probably yes',
    'Think so',
    'Pog Yeaaah',
    'Poop Yeahhh',
    'Boii of course yess',
    # negative
    'Pog Nooo',
    'Probably no',
    'Nooooo',
    'I dont think so',
    'Poop Noooo',
    'Boii of course nooo',
    # lol
    'shut man',
    "Don't ask me nub",
]


@client.command(aliases=['8ball', 'also8ball', 'magicball', '8b', 'mb'])
async def _8ball(ctx, *, question):
    ballembed = discord.Embed(title="The Magic 8Ball", color=0x12d0ff)
    ballembed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/778886054215942164/780300717373128714/ezgif-4-d4f11b723c24.gif")
    ballembed.add_field(
        name=f"*`{question}`*", value=f'Response: \n**{random.choice(ballresponses)}**', inline=False)

    # await ctx.send(f'{question} \nHmmmm \nResponse : {random.choice(ballresponses)}.')
    await ctx.send(embed=ballembed)



@client.command()
@commands.check(is_Atriays or is_Mutant or is_Nerdy)
async def guilds(ctx):

    guild_embed = discord.Embed(title = "Atriays's Pog Bot is in these Guilds: ", color = 0xFF2424)

    for guild in client.guilds:
        guild_embed.add_field(
            name=f"Name: {guild}", value=f'ID: {guild.id}', inline=True)

    await ctx.author.send(embed=guild_embed)






@client.command()
@commands.check(is_Atriays or is_Mutant or is_Nerdy)
async def createinvite(ctx,id : int = None ):

    if id == None:
        id = ctx.guild.id

        guild = client.get_guild(id)
        channel = guild.text_channels[0]

        link = await channel.create_invite(max_uses=1)
        await ctx.author.send(f"Here's the invite link of {guild}: {link}")
    else:
        guild = client.get_guild(id)
        channel = guild.text_channels[0]

        link = await channel.create_invite(max_uses=1)
        await ctx.author.send(f"Here's the invite link of {guild}: {link}")




@client.command()
async def cowsay(ctx, *, cowsaylol = "Y is this empty ;-;"):
    if len(cowsaylol) > 93:

        underscore = '_'*93
        dash = '-'*93

        msg = f"```\n_{underscore}_\n<{cowsaylol}>\n-{dash}-\n        \   ^__^\n         \  (oo)\_______\n            (__)\       )\/\\ \n                ||----w |\n                ||     ||\n```"

    else:

        underscore = '_'*len(cowsaylol)
        dash = '-'*len(cowsaylol)

        msg = f"```\n_{underscore}___\n< {cowsaylol} >\n-{dash}---\n        \   ^__^\n         \  (oo)\_______\n            (__)\       )\/\\ \n                ||----w |\n                ||     ||\n```"

    await ctx.send(msg)


@client.command()
async def botinvite(ctx):
    await ctx.send("Invite Atriays's Pog Bot: http://bit.ly/3n3PmGV")


#MUSIC

MUSIC_COLOUR = 0x78f0b4
"""
#results = YoutubeSearch(search, max_results=10).to_dict()
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
"""
# .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |  _________   | || | ____   ____  | || |  _________   | || | ____  _____  | || |  _________   | || |    _______   | |
# | | |_   ___  |  | || ||_  _| |_  _| | || | |_   ___  |  | || ||_   \|_   _| | || | |  _   _  |  | || |   /  ___  |  | |
# | |   | |_  \_|  | || |  \ \   / /   | || |   | |_  \_|  | || |  |   \ | |   | || | |_/ | | \_|  | || |  |  (__ \_|  | |
# | |   |  _|  _   | || |   \ \ / /    | || |   |  _|  _   | || |  | |\ \| |   | || |     | |      | || |   '.___`-.   | |
# | |  _| |___/ |  | || |    \ ' /     | || |  _| |___/ |  | || | _| |_\   |_  | || |    _| |_     | || |  |`\____) |  | |
# | | |_________|  | || |     \_/      | || | |_________|  | || ||_____|\____| | || |   |_____|    | || |  |_______.'  | |
# | |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'


# on ready - checks if the bot is running
@client.event
async def on_ready():
    print('bot is poopi ready man')
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Atriays's Pog Bot"))


#@client.event
#async def on_member_join(member):
#    print(f'{member} joined. /nPOGGGG')
#################################################
#@client.event
#async def on_member_remove(member):
#    print(f'{member} left /nNotPOG ;-;')"""



"""
@client.event
async def on_message(message):
    message.author: discord.member
    if message.author == client.user:
        return

    messageContent = message.content
    messageMentions = message.mentions
    if len(messageContent) > 0:
        await message.channel.send(f'```{messageContent}```')
"""


# .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |  ________    | || |     _____    | || |    _______   | || |     ______   | || |      __      | || |  _______     | || |  ________    | || |  _________   | || |  ________    | |
# | | |_   ___ `.  | || |    |_   _|   | || |   /  ___  |  | || |   .' ___  |  | || |     /  \     | || | |_   __ \    | || | |_   ___ `.  | || | |_   ___  |  | || | |_   ___ `.  | |
# | |   | |   `. \ | || |      | |     | || |  |  (__ \_|  | || |  / .'   \_|  | || |    / /\ \    | || |   | |__) |   | || |   | |   `. \ | || |   | |_  \_|  | || |   | |   `. \ | |
# | |   | |    | | | || |      | |     | || |   '.___`-.   | || |  | |         | || |   / ____ \   | || |   |  __ /    | || |   | |    | | | || |   |  _|  _   | || |   | |    | | | |
# | |  _| |___.' / | || |     _| |_    | || |  |`\____) |  | || |  \ `.___.'\  | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  _| |___.' / | || |  _| |___/ |  | || |  _| |___.' / | |
# | | |________.'  | || |    |_____|   | || |  |_______.'  | || |   `._____.'  | || ||____|  |____|| || | |____| |___| | || | |________.'  | || | |_________|  | || | |________.'  | |
# | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'




# Important stuff
@client.command()
async def shutdown(ctx):
    if (ctx.author.id == 543718305773387776):
        await ctx.send(f"Shutting Down Atriays's Pog Bot. \nIssued by {ctx.author.mention} ")
        await client.logout()
    else:
        await ctx.send(f"Shut {ctx.author.mention}. You don't have the permission to Shutdown Atriays's Pog Bot.")


# Cog Stuff
unload_cog = ['cogs.callouts',
              'cogs.badping'
                ]

@client.command()
async def enable(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')

@client.command()
async def disable(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for unload in unload_cog:
    client.unload_extension(unload)



client.run(TOKEN)
