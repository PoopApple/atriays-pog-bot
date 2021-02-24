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

#import pandas as pd
import json

import os

from PIL import Image

import requests
from io import  BytesIO

#from youtube_search import YoutubeSearch
#import youtube_dl
import asyncio

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import ast

#---------------------------------------------------------------------------------#
#colours
main_colour = 0x3fc2c9

#---------------------------------------------------------------------------------#
#FIREBASE

cred = credentials.Certificate('./test-3918a-firebase-adminsdk-wtefn-abb1c62607.json')

# Initialize the app with a service account
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-3918a.firebaseio.com/'
})

#---------------------------------------------------------------------------------#
# Prefix
default_prefix = ['.']

def get_prefix(client,message):
    ref = db.reference('prefixes')
    prefix = ref.get()
    if prefix.get(str(message.guild.id)) == None:
        return [f'{default_prefix[0]}','<@!779225458159386624> ']
    else:
        guild_prefix = prefix[str(message.guild.id)]
        return [guild_prefix , '<@!779225458159386624> ']


#---------------------------------------------------------------------------------#

# Permission for intents
intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)

# setting the discord bot thinga majik
client = commands.Bot(command_prefix= get_prefix,
                      intents=intents , help_command=None) #, help_command=None

#todaynow = datetime.now().strftime("%d/%m/%Y  %H:%M")

# Conditions for commands :-
# example code ;-; - @commands.check(is_Atriays or is_Mutant or is_Nerdy or has_permissions(administrator=True))
def is_atriays():
    def predicate(ctx):
        return ctx.message.author.id == 543718305773387776
    return commands.check(predicate);

def is_mutant():
    def predicate(ctx):
        return ctx.message.author.id == 460335920260841482
    return commands.check(predicate);

def is_nerdy():
    def predicate(ctx):
        return ctx.message.author.id == 516173155216392193
    return commands.check(predicate);

def is_trimunati():
    def predicate(ctx):
        return (ctx.message.author.id == 516173155216392193 or 460335920260841482 or 543718305773387776)
    return commands.check(predicate)


# Help cmd (help)
@client.command(aliases=['help'])
async def _help(ctx):
    helpembed = discord.Embed(
        title="Commands", description="Commands available in Atriays's Pog Bot", color=main_colour)
    helpembed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/779225458159386624/f3ba776ec26d2b00811a33d60ddea532.png?size=1024")
    helpembed.set_author(name="Atriays's Pog Bot", url="https://cdn.discordapp.com/avatars/779225458159386624/f3ba776ec26d2b00811a33d60ddea532.png?size=1024",
                         icon_url="https://cdn.discordapp.com/avatars/779225458159386624/f3ba776ec26d2b00811a33d60ddea532.png?size=1024")
    helpembed.add_field(
        name="Help", value=f"This Command. *Usage - {default_prefix[0]}help* => Shows this embed", inline=False)
    helpembed.add_field(
        name="Clear", value=f"Clears chat upto a point. *Usage - {default_prefix[0]}clear 10* => Clears 10 chat before the command. ", inline=False)
    helpembed.add_field(
        name="Repeat", value=f'Repeats anything you say. (max: 100 times) *Usage - {default_prefix[0]}Repeat 5 Hi I am Pog=>* Repeats "Hi I am Pog" 10 times.', inline=False)
    helpembed.add_field(
        name="Spam", value=f"Spams a user. (max: 5 times) *Usage - {default_prefix[0]}spam 2 @User =>* Spam pings the user 2 times.", inline=False)
    helpembed.add_field(
        name="Ping", value=f"Shows the bot's ping. *Usage - {default_prefix[0]}Ping*", inline=False)
    helpembed.add_field(
        name="adinub", value=f"Shows the Universal Truth", inline=False)
    helpembed.add_field(
        name="8Ball", value=f"A general 8ball command. *Usage - {default_prefix[0]}8ball Am i pog? =>* Gives you a random answer.", inline=False)
    helpembed.add_field(
        name="pog", value=f"Tells you if the statement is pog or not. *Usage - {default_prefix[0]}pog u r a poopi*", inline=False)
    helpembed.add_field(
        name="slap", value=f"slaps the user you mentioned. *Usage - {default_prefix[0]}slap @user*", inline=False)
    helpembed.add_field(
        name="avatar", value=f"Displays the avatar of the mentioned user. *Usage - {default_prefix[0]}av @user*", inline=False)
    # await ctx.send(embed = helpembed)
    await ctx.author.send(embed=helpembed)

    dmembed = discord.Embed(
        title=f'{ctx.author}, Check Your DM', color=main_colour)
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
@commands.check_any(is_atriays() ,is_mutant() , is_nerdy() , commands.has_permissions(administrator=True),is_trimunati())
async def clear(ctx, amount=1):
    await ctx.message.delete()
    #await str(cleared_msgs[0])[12:30]).delete()


    cleared_msgs = await ctx.channel.purge(limit=amount)

    purge_embed = discord.Embed(title = f'Deleted {amount} message(s)' , color = main_colour)
    await ctx.send(embed = purge_embed , delete_after = 1.7)

    print(f'{ctx.author} cleared {amount} msg(s)')




    ref = db.reference(f'log/{str(ctx.guild.id)}')
    # Generate a reference to a location
    emp_ref = ref.push(
        {
        'user' : f'{str(ctx.author.id)} | {str(ctx.author)}',
        'msgs_del': f'{str(amount)}',
        'date_time': f'{str(datetime.now().strftime("%d/%m/%Y | %H:%M"))}'
        }
    )





@client.command()
async def ping(ctx):
    dmembed = discord.Embed(
        title=f'Poggers!! \nThe Ping is {round(client.latency * 1000)}ms', color=main_colour)
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
@commands.check(is_atriays() or is_mutant() or is_nerdy())
async def guilds(ctx):

    guild_embed = discord.Embed(title = "Atriays's Pog Bot is in these Guilds: ", color = 0xFF2424)

    for guild in client.guilds:
        guild_embed.add_field(
            name=f"Name: {guild}", value=f'ID: {guild.id}', inline=True)

    await ctx.author.send(embed=guild_embed)






@client.command()
@commands.check(is_atriays() or is_mutant() or is_nerdy())
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



@client.command(aliases = ['av'])
async def avatar(ctx, user : discord.Member = None):
    if user == None:
        av_embed = discord.Embed(title=f"Avatar of `{ctx.author}`", color=main_colour)
        av_embed.add_field(
            name=f"*Link:*", value=f' [webp]({ctx.author.avatar_url}) | [jpg]({ctx.author.avatar_url_as(format = "jpeg")}) | [png]({ctx.author.avatar_url_as(format = "png")}) ', inline=False)
        av_embed.set_image(url = ctx.author.avatar_url)
        await ctx.channel.send(embed = av_embed)
    else:
        av_embed = discord.Embed(title=f"Avatar of `{user}`", color=main_colour)
        av_embed.add_field(
            name=f"*Link:*", value=f'[webp]({user.avatar_url}) | [jpg]({user.avatar_url_as(format = "jpeg")}) | [png]({user.avatar_url_as(format = "png")}) ', inline=False)
        av_embed.set_image(url = user.avatar_url)
        await ctx.channel.send(embed = av_embed)





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
    update_cogs_file()


'''@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        pass
'''
'''@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send('No Reactions :(')'''

#@client.event
#async def on_member_join(member):
#    print(f'{member} joined. /nPOGGGG')
#################################################
#@client.event
#async def on_member_remove(member):
#    print(f'{member} left /nNotPOG ;-;')"""



'''
@client.event
async def on_message(message):
    message.author: discord.member
    if message.author == client.user:
        return
    elif message.embeds:
        print(message.embeds[0].to_dict())
    messageContent = message.content
    messageMentions = message.mentions
    if len(messageContent) > 0:
        await message.channel.send(f'```{messageContent}```')
'''





# Important stuff
@client.command()
async def shutdown(ctx):
    if (ctx.author.id == 543718305773387776):
        await ctx.send(f"Shutting Down Atriays's Pog Bot. \nIssued by {ctx.author.mention} ")
        await client.logout()
    else:
        await ctx.send(f"Shut {ctx.author.mention}. You don't have the permission to Shutdown Atriays's Pog Bot.")


#settings
@client.command()
async def settings(ctx, sub_setting , set_syntax_one = None , set_syntax_two = None):
    if (sub_setting == 'prefix'):
        if (set_syntax_one == None and set_syntax_two == None):

            ref = db.reference('prefixes')
            prefix = ref.get()
            if prefix.get(str(ctx.guild.id)) == None:
                current_prefix = default_prefix[0]
            else:
                guild_prefix = prefix[str(ctx.guild.id)]
                current_prefix = guild_prefix
            await ctx.send(f"Current Prefix of {ctx.guild}:  {current_prefix}")

        elif (set_syntax_one == 'change'):
            if set_syntax_two == None:
                await ctx.send('Usage => settings prefix change {new prefix} eg. settings prefix change >')
            else:
                ref = db.reference('prefixes')
                ref.update({f'{ctx.guild.id}' : set_syntax_two})
                await ctx.send(f'Changed Server Prefix to: {set_syntax_two}')


def update_cogs_file():
    ref = db.reference(f'cogs')
    data = ref.get()
    with open("cog_data.json", "w") as cog__data:
        json.dump(data, cog__data, indent = 4)

def update_cog( guild_name , guild_id : int, enable_disable : int , cog_name : str):

    cogs_line = ''
    if enable_disable == 1:
        msg_enable_or_disable = 'Enabled'
    else:
        msg_enable_or_disable = 'Disabled'
    #numb_cogs = 1,2,3,4 etc for length  of list ( all cogs)
    for numb_cogs in range(len(all_cogs)):


        #check if the given cog is in the list
        if all_cogs[numb_cogs] == cog_name:
            ref = db.reference(f'cogs/{str(guild_id)}')
            emp_ref = ref.update({
                f'{cog_name}': f'{enable_disable}'
                })
            numb_cogs = 0
            cogs_line = ''
            msg_to_be_sent = f'{msg_enable_or_disable} `{cog_name}` for {guild_name}.'
            return msg_to_be_sent
            print(msg_to_be_sent)
        else:
            cogs_line += f'`{all_cogs[numb_cogs]}` '
    if cogs_line == '':
        return
    else:
        msg_to_be_sent = 'Choose from the following: ' + cogs_line
        return msg_to_be_sent
        print(msg_to_be_sent)






@commands.check_any(is_atriays() ,is_mutant() , is_nerdy() , commands.has_permissions(administrator=True),is_trimunati())
@client.command()
async def enable(ctx , * , cog_name : str):
    msg_sent = update_cog( ctx.guild , ctx.guild.id , 1 , cog_name)
    update_cogs_file()
    await ctx.send(msg_sent)

@commands.check_any(is_atriays() ,is_mutant() , is_nerdy() , commands.has_permissions(administrator=True),is_trimunati())
@client.command()
async def disable(ctx , * , cog_name : str):
    msg_sent = update_cog(ctx.guild , ctx.guild.id , 0 , cog_name)
    update_cogs_file()
    await ctx.send(msg_sent)


all_cogs = []

@client.command()
async def cogs(ctx):
    global all_cogs
    await ctx.send(all_cogs)





# Cog Stuff
unload_cog = [
                ]





@commands.check(is_atriays() or is_mutant() or is_nerdy())
@client.command()
async def senable(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Enabled {extension}')



@commands.check(is_atriays() or is_mutant() or is_nerdy())
@client.command()
async def sdisable(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Disabled {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        all_cogs.append(filename[:-3])

for unload in unload_cog:
    client.unload_extension(unload)

print(all_cogs)



"""
███████╗██╗░░░██╗░█████╗░██╗░░░░░
██╔════╝██║░░░██║██╔══██╗██║░░░░░
█████╗░░╚██╗░██╔╝███████║██║░░░░░
██╔══╝░░░╚████╔╝░██╔══██║██║░░░░░
███████╗░░╚██╔╝░░██║░░██║███████╗
╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
"""








def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

@is_trimunati()
@client.command()
async def evall(ctx, *, cmd):
    """Evaluates input.
    Input is interpreted as newline seperated statements.
    If the last statement is an expression, that is the return value.
    Usable globals:
      - `bot`: the bot instance
      - `discord`: the discord module
      - `commands`: the discord.ext.commands module
      - `ctx`: the invokation context
      - `__import__`: the builtin `__import__` function
    Such that `>eval 1 + 1` gives `2` as the result.
    The following invokation will cause the bot to send the text '9'
    to the channel of invokation and return '3' as the result of evaluating
    >eval ```
    a = 1 + 2
    b = a * 2
    await ctx.send(a + b)
    a
    ```
    """
    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    # add a layer of indentation
    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    # wrap in async def body
    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    insert_returns(body)

    env = {
        'bot': ctx.bot,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__
    }
    exec(compile(parsed, filename="<ast>", mode="exec"), env)

    result = (await eval(f"{fn_name}()", env))
    await ctx.send(result)



client.run(TOKEN)
