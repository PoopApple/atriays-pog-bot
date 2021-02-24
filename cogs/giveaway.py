import discord
import json
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import asyncio
import random
from datetime import timedelta , datetime
import pytz

def update_cogs_file():
    ref = db.reference(f'cogs')
    data = ref.get()
    with open(os.path.dirname(__file__) + '/../cog_data.json', "w") as cog__data:
        json.dump(data, cog__data, indent = 4)


with open(f'{os.path.dirname(__file__) + "/../cog_data.json"}') as f:
  cog_data = json.load(f)

def cog_check():
    def predicate(ctx):

        cog = cog_data.get(str(ctx.guild.id))

        if cog != None:
            actions_enabled = cog['actions']
            return actions_enabled == '1';
        else:
            ref = db.reference(f'cogs/{ctx.guild.id}')
                # Generate a reference to a location
            emp_ref = ref.update(
                    {
                    'actions': '1',
                    'badping': '0',
                    'spam': '0',
                    'callouts': '0',
                    'giveaway' : '1'
                    }
                )
            update_cogs_file()
            return True;
    return predicate;


class giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('giveaway cog is working')


    @commands.check(cog_check())
    @commands.has_permissions(kick_members=True)
    @commands.command(aliases = ['gaw'])
    async def giveaway(self, ctx, time_gaw_raw , channel_gaw : discord.TextChannel , no_of_winners : int = 1, * , prize_gaw : str ):

        # time => 10000s , 1000m , 02299h , 22d


        time_gaw = time_gaw_raw[:-1]

        if time_gaw_raw.endswith('s' or 'S'):
            time_gaw_sec = 1*int(time_gaw)

        elif time_gaw_raw.endswith('m' or 'M'):
            time_gaw_sec = 60*int(time_gaw)

        elif time_gaw_raw.endswith('h' or 'H'):
            time_gaw_sec = 3600*int(time_gaw)

        elif time_gaw_raw.endswith('d' or 'D'):
            time_gaw_sec = 86400 * int(time_gaw)
        else:
            await ctx.send('Invalid Time.')
            return


        IST = pytz.timezone('Asia/Kolkata')
        gaw_embed = discord.Embed(title = f'🎉 GIVEAWAY 🎉' , description = f'`{prize_gaw}`\nReact with 🎉 to enter\nEnds at: `{str(datetime.now(IST) + timedelta(0,time_gaw_sec))[11:-13]} IST`\nNumber of Winners: `{no_of_winners}`', color = 0x71b4e3) #, description = f'Hosted by: {ctx.author.mention}'
        #gaw_embed.add_field(name = 'Ends at' , value = f'{str(datetime.utcnow() + timedelta(0,time_gaw_sec))[11:-7]} UTC')
        gaw_embed.set_footer(text = f'Hosted by {ctx.author} at {datetime.now(IST).strftime("%H:%M:%S")} IST')
        #PST = pytz.timezone('Etc/GMT-8')

        #gaw_embed.set_footer(text = f'{datetime.utcnow().strftime("%H:%M:%S")} UTC\n{datetime.now(PST).strftime("%H:%M:%S")} PST\n{datetime.now(IST).strftime("%H:%M:%S")} IST')



        gaw = await channel_gaw.send(embed = gaw_embed)
        await gaw.add_reaction('🎉')
        await asyncio.sleep(time_gaw_sec)


        gaw_msg = await ctx.fetch_message(gaw.id)

        users = await gaw_msg.reactions[0].users().flatten()
        users.pop(0)
        winner_list = random.choices(users , k = no_of_winners)
        winner_msg =''
        for winners in winner_list:
            winner_msg += f'{winners.mention} '


        winnerEmbed = discord.Embed(title ='🎉 GIVEAWAY WINNERS 🎉' ,description = f'`{prize_gaw}`' , color = 0x71b4e3)
        winnerEmbed.add_field(name = 'Winner(s):' , value = f'{winner_msg}', inline = False)
        winnerEmbed.add_field(name = 'Giveaway:' , value = f'[Click Here]({gaw.jump_url})', inline = False)
        await channel_gaw.send(embed = winnerEmbed)

        new_gaw_embed = discord.Embed(title = f'🎉 GIVEAWAY 🎉' , description = f'`{prize_gaw}`\nWinner(s): {winner_msg} \nNumber of Winners: `{no_of_winners}`', color = 0x71b4e3)
        new_gaw_embed.set_footer(text = f'Hosted by {ctx.author} | Ended at {datetime.now(IST).strftime("%H:%M:%S")} IST')
        await gaw.edit(embed = new_gaw_embed)



    @commands.check(cog_check())
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def reroll(self, ctx, gaw_msg_id : int , numb_of_rerolls : int = 1):

        gaw_msg = await ctx.fetch_message(gaw_msg_id)

        users = await gaw_msg.reactions[0].users().flatten()
        users.pop(0)
        winner_list = random.choices(users , k = numb_of_rerolls)
        winner_msg =''
        for winners in winner_list:
            winner_msg += f'{winners.mention} '


        winnerEmbed = discord.Embed(title = f'🎉 GIVEAWAY REROLL 🎉' ,description = f'`{prize_gaw}``', color = 0x71b4e3)
        winnerEmbed.add_field(name = 'Winner(s):' , value = f'{winner_msg}', inline = False)
        winnerEmbed.add_field(name = 'Giveaway:' , value = f'[Click Here]({gaw_msg.jump_url})', inline = False)
        await ctx.send(embed = winnerEmbed)




def setup(client):
    client.add_cog(giveaway(client))
