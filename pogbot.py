"""
cmds :-
help
cleared
repeat
spam
shut
ping
kuku
8ball
"""
me = 'Atriays#5462'

#Libraries and stuff
import discord
from discord.ext import commands
from discord import member

import datetime
from datetime import datetime

import random
from random import choice

import pandas as pd

prefix = "."  # Prefix

# Permission for intents
intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)

# setting the discord bot thinga majik
client = commands.Bot(command_prefix=prefix,
                      intents=intents, help_command=None)

#todaynow = datetime.now().strftime("%d/%m/%Y  %H:%M")

# Conditions for commands :-

def is_Atriays(ctx):
    return ctx.author.id == 543718305773387776

def is_Mutant(ctx):
    return ctx.author.id == 460335920260841482

def is_Nerdy(ctx):
    return ctx.author.id == 516173155216392193



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
        name="Help", value=f"This Command. *Usage - {prefix}help* => Shows this embed", inline=False)
    helpembed.add_field(
        name="Clear", value=f"Clears chat upto a point. *Usage - {prefix}clear 10* => Clears 10 chat before the command. ", inline=False)
    helpembed.add_field(
        name="Repeat", value=f'Repeats anything you say. (max: 100 times) *Usage - {prefix}Repeat 5 Hi I am Pog=>* Repeats "Hi I am Pog" 10 times.', inline=False)
    helpembed.add_field(
        name="Spam", value=f"Spams a user. (max: 5 times) *Usage - {prefix}spam @User 2 =>* Spam pings the user 2 times.", inline=False)
    helpembed.add_field(
        name="Ping", value=f"Shows the bot's ping. *Usage - {prefix}Ping*", inline=False)
    helpembed.add_field(
        name="adinub", value=f"Shows the Universal Truth", inline=False)
    helpembed.add_field(
        name="8Ball", value=f"A general 8ball command. *Usage - {prefix}8ball Am i pog? =>* Gives you a random answer.", inline=False)
    helpembed.add_field(
        name="pog", value=f"Tells you if the statement is pog or not. *Usage - {prefix}pog u r a poopi*", inline=False)
    # await ctx.send(embed = helpembed)
    await ctx.author.send(embed=helpembed)

    dmembed = discord.Embed(
        title=f'{ctx.author}, Check Your DM', color=0x3fc2c9)
    msg = await ctx.send(embed=dmembed)
    await msg.add_reaction(u'\u2611')


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
@client.command()
@commands.check(is_Atriays or is_Mutant or is_Nerdy)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Deleted {amount} message(s)')
    print(f'{ctx.author} cleared {amount} msg(s)')
    df = pd.read_csv("C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv", index_col=0)
    df = df.append({'Log': f'{ctx.author} cleared {amount} message(s) on {datetime.now().strftime("%d/%m/%Y  %H:%M")}'},ignore_index=True)  # , {'Cleared' : f'{amount}'} , {'User' : f'{ctx.author}'}
    df.to_csv('C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv')

    #df = pd.read_csv("C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv" , index_col = 1 )
    #df = df.append({'Cleared' : f'{amount}'} , ignore_index = True) #, {'Cleared' : f'{amount}'} , {'User' : f'{ctx.author}'}
    #df.to_csv('C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv')
    #df = pd.read_csv("C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv" , index_col = 2 )
    #df = df.append({'User' : f'{ctx.author}'} , ignore_index = True) #, {'Cleared' : f'{amount}'} , {'User' : f'{ctx.author}'}
    #df.to_csv('C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv')
    #print(df)"""


# repeat cmd
@client.command()
async def repeat(ctx, numrepeat=1, *, repeatthis):
    while numrepeat in range(1, 101):
        if (numrepeat > 0):
            await ctx.send(repeatthis)
            numrepeat = numrepeat - 1
        else:
            return


# spam cmd
@client.command()
async def spam(ctx, pingmember: discord.Member, *, numspam=1):
    while numspam in range(1, 6):
        if (numspam > 0):
            await ctx.send(pingmember.mention)
            numspam = numspam - 1
        else:
            return


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


"""@client.command()
async def atri(ctx):
    await ctx.send(discord.Member.id.mentioned_in(ctx))"""


@client.command()
async def test(ctx):
    await ctx.send('test')
    print('test')


ballresponses = [
    # positive
    'Yesss',
    'Probably yes',
    'Think so',
    'Pog Yeaaah',
    'Poop Yeahhh',
    'Man of course yess',
    # negative
    'Pog No',
    'Probably no',
    'Nooooo',
    'I dont think so',
    'Poop Noooo',
    'Man of course nooo',
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
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Atriays's Pog Bot"))

#    df = pd.DataFrame({'Log' : ['blah blah']})
#    df.to_csv("C:/Users/aryan/OneDrive/Desktop/discord/bot files/output/output.csv")

# on msg - just send a msg if a string is present in a text
his = ['hi', 'hello', 'hlo', 'Hi', 'Hello', 'Hlo', 'yo', 'Yo']
shuts = ['shut', 'SHUT', 'Shut']
aht = ['all hail trimunati', 'ALL HAIL TRIMUNATI', 'aht' , 'Aht']
badpings = ['@!543718305773387776', 'Atriays' , '543718305773387776' , '543718305773387776']  # this is the key poop :D
dont = ['dont', 'Dont', "Don't", "don't"]
nig = ['nigga' , 'nigger' , 'nig' , 'N Word']


@client.event
async def on_message(message):
    message.author: discord.member
    if message.author == client.user:
        return

    messageContent = message.content
    messageMentions = message.mentions
    if len(messageContent) > 0:
        for word in his:
            if word == messageContent:
                await message.channel.send(random.choice(his))
        for words in shuts:
            if words == messageContent:
                await message.channel.send(':regional_indicator_s: :regional_indicator_h: :regional_indicator_u: :regional_indicator_t: \nhttps://tenor.com/view/shut-up-shush-shh-ok-bird-gif-17679708')
        for words in aht:
            if words == messageContent:
                await message.channel.send(':regional_indicator_a: :regional_indicator_l: :regional_indicator_l:   :regional_indicator_h: :regional_indicator_a: :regional_indicator_i: :regional_indicator_l:   :regional_indicator_t: :regional_indicator_r: :regional_indicator_i: :regional_indicator_m: :regional_indicator_u: :regional_indicator_n: :regional_indicator_a: :regional_indicator_t: :regional_indicator_i:')
    #    for members in message.mentions:
    #        for bad in badpings:
    #            if bad.mention in message.mentions:
    #                await message.channel.send(f'Dont ping him, {message.author.mention}')
    #            else :
    #                for memebers in message.mentions:
    #                    print(members.id , discord.member(id = 543718305773387776))
    #    for men in messageMentions:
    #        if messageMentions.find('543718305773387776') >= 0  :
    #            await message.channel.send('pinged')
    #    for string in messageMentions:
    #        if any('543718305773387776' in string ):
    #            await message.channel.send('pinged')
        """if len(messageMentions) > 0 :
            l = len(messageMentions) - 1
            print(l)
            while (l > -1):
                mentions = [ message.mentions[l]]
                if '543718305773387776' in  f' {mentions}':
                    await message.channel.send(f"**Don't** Ping him, U Poopi {message.author.mention} :poop:" )
                    l= l - 1
                else:
                    l = l-1"""

            #mention_list = ", ".join(mentions[:-1]) + " and " + mentions[-1]
            #if any('543718305773387776' in string for string in messageMentions[0]):
            #    await message.channel.send('pinged lol')
            #await message.channel.send(mention_list)

        for words in dont:
            if words == messageContent:
                await message.channel.send(':regional_indicator_d: :regional_indicator_o: :regional_indicator_n: :regional_indicator_t:')
        for words in nig:
            if words == messageContent:
                await message.channel.send(':regional_indicator_n: :regional_indicator_i: :regional_indicator_g: :regional_indicator_g: :regional_indicator_a:')
        # if messageContent.startswith('/'):
        #    await message.channel.purge(limit=2)

        await client.process_commands(message)


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

    #   if len(messageMentions) > 0:
    """    if message.author == client.user:
                return
            for word in messageMentions:
                if word in badpings or 'Atriays#5462' in messageMentions or 'Atriays#5462' in messageContent:
                    await message.channel.send('pinged')

#            if discord.member.id == '543718305773387776':
#                await message.channel.send('pinged')
#            else:
#                await message.channel.send(discord.user.mentioned_in(messageMentions).id)





           for word in badpings:

                #await message.channel.send(messageMentions)
                await message.channel.send(discord.member.metioned_in(message))
                if word in messageMentions:
                    await message.channel.send('pinged')






word_list = ['@Adinub']

messageContent = message.content
if len(messageContent) > 0:
        for word in word_list:
                if word in messageContent:
                    await message.channelsend('yes')


#@client.event
#async def on_member_join(member):
#    print(f'{member} joined. /nPOGGGG')
#################################################
#@client.event
#async def on_member_remove(member):
#    print(f'{member} left /nNotPOG ;-;')"""


# Important stuff
@client.command()
async def shutdown(ctx):
    if (ctx.author.id == 543718305773387776):
        await ctx.send(f"Shutting Down Atriays's Pog Bot. \nIssued by {ctx.author.mention} ")
        await client.logout()
    else:
        await ctx.send(f"Shut {ctx.author.mention}. You don't have the permission to Shutdown Atriays's Pog Bot.")



client.run('Nzc5MjI1NDU4MTU5Mzg2NjI0.X7dcQg.W-3EtcJFpzWCBYjYLfwq676EwZw')
