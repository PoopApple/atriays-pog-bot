import discord
import json
from discord.ext import commands , tasks
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import asyncio
import random
from datetime import timedelta, datetime
import pytz
import time






def update_cogs_file():
    ref = db.reference(f'cogs')
    data = ref.get()
    with open(os.path.dirname(__file__) + '/../cog_data.json', "w") as cog__data:
        json.dump(data, cog__data, indent=4)


with open(f'{os.path.dirname(__file__) + "/../cog_data.json"}') as f:
    cog_data = json.load(f)


def cog_check():
    def predicate(ctx):

        cog = cog_data.get(str(ctx.guild.id))

        if cog != None:
            actions_enabled = cog['actions']
            return actions_enabled == '1'
        else:
            ref = db.reference(f'cogs/{ctx.guild.id}')
            # Generate a reference to a location
            emp_ref = ref.update(
                {
                    'actions': '1',
                    'badping': '0',
                    'spam': '0',
                    'callouts': '0',
                    'giveaway': '1'
                }
            )
            update_cogs_file()
            return True
    return predicate






#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################





class giveaway(commands.Cog):
    def __init__(self, client ):
        self.client = client
        self.gaws = {}
        self.man = 1




    @tasks.loop(seconds=10)
    async def bg_gaw_loop(self):
        IST = pytz.timezone('Asia/Kolkata')

        if self.gaws != {}:
            #print(self.gaws)
            for msg_ids in self.gaws:
                #print(f"time now `{str(datetime.now(IST))[:-16]}`  time gaw `{str(self.gaws.get(msg_ids).get('time'))[:-3]}`")
                if (str(datetime.now(IST))[:-16] == str(self.gaws.get(msg_ids).get("time"))[:-3]):
                    #print('equal')

                    channel_gaw = await self.client.fetch_channel(self.gaws.get(msg_ids).get("channel_id"))
                    gaw_msg = await channel_gaw.fetch_message(msg_ids)
                    host_user = await self.client.fetch_user(self.gaws.get(msg_ids).get("host_id"))

                    users = await gaw_msg.reactions[0].users().flatten()
                    users.remove(self.client.user)

                    winner_list = random.sample(users, k= int(self.gaws.get(msg_ids).get("num_of_winners")))
                    winner_msg = ''
                    for winners in winner_list:
                        winner_msg += f'{winners.mention} '

                    winnerEmbed = discord.Embed(
                        title='🎉 GIVEAWAY WINNERS 🎉', description=f'`{self.gaws.get(msg_ids).get("prize")}`', color=0x71b4e3)
                    winnerEmbed.add_field(
                        name='Winner(s):', value=f'{winner_msg}', inline=False)
                    winnerEmbed.add_field(
                        name='Giveaway:', value=f'[Click Here]({gaw_msg.jump_url})', inline=False)
                    await channel_gaw.send(embed=winnerEmbed)

                    new_gaw_embed = discord.Embed(
                        title=f'🎉 GIVEAWAY 🎉', description=f'`{self.gaws.get(msg_ids).get("prize")}`\nWinner(s): {winner_msg} \nNumber of Winner(s): `{self.gaws.get(msg_ids).get("num_of_winners")}`', color=0x71b4e3)
                    new_gaw_embed.set_footer(
                        text=f'Hosted by {host_user} | Ended at {datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S")} IST')
                    await gaw_msg.edit(embed=new_gaw_embed)
                    self.gaws.pop(msg_ids)

    """@bg_gaw_loop.before_loop
    async def before_bg_gaw_loop(self):
        await self.client.wait_until_ready()"""


    @commands.Cog.listener()
    async def on_ready(self):
        print('giveaway cog is working')
        self.bg_gaw_loop.start()


    '''@commands.command()
    async def gawcheck(self , ctx):
        await ctx.send(self.gaws)'''


    @commands.command(aliases=["stopgiveaway" , "endgaw" , "endgiveaway"])
    async def stopgaw(self , ctx , gaw_id : str):
        #print(type(gaw_id))
        if self.gaws.get(f"{gaw_id}") == None:
            await ctx.send(f"No current Giveaway with MessageID `{gaw_id}`")
        else:
            await ctx.send(f'Ended Giveaway with MessageID `{gaw_id}`\nPrize => {self.gaws.get(gaw_id).get("prize")} ')

            IST = pytz.timezone('Asia/Kolkata')

            channel_gaw = await self.client.fetch_channel(self.gaws.get(gaw_id).get("channel_id"))
            gaw_msg = await channel_gaw.fetch_message(gaw_id)
            host_user = await self.client.fetch_user(self.gaws.get(gaw_id).get("host_id"))

            users = await gaw_msg.reactions[0].users().flatten()
            users.remove(self.client.user)

            winner_list = random.sample(users, k= int(self.gaws.get(gaw_id).get("num_of_winners")))
            winner_msg = ''
            for winners in winner_list:
                winner_msg += f'{winners.mention} '

            winnerEmbed = discord.Embed(
                title='🎉 GIVEAWAY WINNERS 🎉', description=f'`{self.gaws.get(gaw_id).get("prize")}`', color=0x71b4e3)
            winnerEmbed.add_field(
                name='Winner(s):', value=f'{winner_msg}', inline=False)
            winnerEmbed.add_field(
                name='Giveaway:', value=f'[Click Here]({gaw_msg.jump_url})', inline=False)
            await channel_gaw.send(embed=winnerEmbed)

            new_gaw_embed = discord.Embed(
                title=f'🎉 GIVEAWAY 🎉', description=f'`{self.gaws.get(gaw_id).get("prize")}`\nWinner(s): {winner_msg} \nNumber of Winner(s): `{self.gaws.get(gaw_id).get("num_of_winners")}`', color=0x71b4e3)
            new_gaw_embed.set_footer(
                text=f'Hosted by {host_user} | Ended at {datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S")} IST')
            await gaw_msg.edit(embed=new_gaw_embed)


            self.gaws.pop(f"{gaw_id}")


    @commands.check(cog_check())
    @commands.has_permissions(kick_members=True)
    @commands.command(aliases=['gaw'])
    async def giveaway(self, ctx, time_gaw_raw, channel_gaw: discord.TextChannel, no_of_winners: int = 1, *, prize_gaw: str):

        # time => 10000s , 1000m , 02299h , 22d

        time_gaw = time_gaw_raw[:-1]

        if time_gaw_raw.endswith('m' or 'M'):
            time_gaw_sec = 60 * int(time_gaw)

        elif time_gaw_raw.endswith('h' or 'H'):
            time_gaw_sec = 3600 * int(time_gaw)

        elif time_gaw_raw.endswith('d' or 'D'):
            time_gaw_sec = 86400 * int(time_gaw)
        else:
            await ctx.send('Invalid Time.')
            return

        IST = pytz.timezone('Asia/Kolkata')
        # , description = f'Hosted by: {ctx.author.mention}'
        end_time = str(datetime.now(IST) + timedelta(0,time_gaw_sec))[:-13]
        gaw_embed = discord.Embed(
            title=f'🎉 GIVEAWAY 🎉', description=f'`{prize_gaw}`\nReact with 🎉 to enter\nEnds at: `{end_time} IST`\nNumber of Winners: `{no_of_winners}`', color=0x71b4e3)
        #gaw_embed.add_field(name = 'Ends at' , value = f'{str(datetime.utcnow() + timedelta(0,time_gaw_sec))[11:-7]} UTC')
        gaw_embed.set_footer(
            text=f'Hosted by {ctx.author} at {datetime.now(IST).strftime("%d/%m/%Y %H:%M:%S")} IST')
        #PST = pytz.timezone('Etc/GMT-8')

        #gaw_embed.set_footer(text = f'{datetime.utcnow().strftime("%H:%M:%S")} UTC\n{datetime.now(PST).strftime("%H:%M:%S")} PST\n{datetime.now(IST).strftime("%H:%M:%S")} IST')

        gaw = await channel_gaw.send(embed=gaw_embed)
        await gaw.add_reaction('🎉')

        self.gaws[f"{gaw.id}"] = {"time" : f"{end_time}" , "channel_id" : f"{channel_gaw.id}" , "prize" : f'{prize_gaw}' , "host_id" : f"{ctx.author.id}" , "num_of_winners" : f"{no_of_winners}"}
        #print(self.gaws)

#        await asyncio.sleep(time_gaw_sec)





        """
        gaw_msg = await ctx.fetch_message(gaw.id)

        users = await gaw_msg.reactions[0].users().flatten()
        users.remove(self.client.user)
        print(users)
        winner_list = random.sample(users, k=no_of_winners)
        winner_msg = ''
        for winners in winner_list:
            winner_msg += f'{winners.mention} '

        winnerEmbed = discord.Embed(
            title='🎉 GIVEAWAY WINNERS 🎉', description=f'`{prize_gaw}`', color=0x71b4e3)
        winnerEmbed.add_field(
            name='Winner(s):', value=f'{winner_msg}', inline=False)
        winnerEmbed.add_field(
            name='Giveaway:', value=f'[Click Here]({gaw.jump_url})', inline=False)
        await channel_gaw.send(embed=winnerEmbed)

        new_gaw_embed = discord.Embed(
            title=f'🎉 GIVEAWAY 🎉', description=f'`{prize_gaw}`\nWinner(s): {winner_msg} \nNumber of Winners: `{no_of_winners}`', color=0x71b4e3)
        new_gaw_embed.set_footer(
            text=f'Hosted by {ctx.author} | Ended at {datetime.now(IST).strftime("%d/%m/%Y %H:%M:%S")} IST')
        await gaw.edit(embed=new_gaw_embed)
        """

    @commands.check(cog_check())
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def reroll(self, ctx, gaw_msg_id: int, numb_of_rerolls: int = 1):

        gaw_msg = await ctx.fetch_message(gaw_msg_id)

        users = await gaw_msg.reactions[0].users().flatten()
        users.pop(0)
        winner_list = random.choices(users, k=numb_of_rerolls)
        winner_msg = ''
        for winners in winner_list:
            winner_msg += f'{winners.mention} '

        winnerEmbed = discord.Embed(
            title=f'🎉 GIVEAWAY REROLL 🎉', color=0x71b4e3)
        winnerEmbed.add_field(
            name='Winner(s):', value=f'{winner_msg}', inline=False)
        winnerEmbed.add_field(
            name='Giveaway:', value=f'[Click Here]({gaw_msg.jump_url})', inline=False)
        await ctx.send(embed=winnerEmbed)





def setup(client):
#    client.loop.create_task(gawclass.bg_gaw_loop())
    client.add_cog(giveaway(client))
