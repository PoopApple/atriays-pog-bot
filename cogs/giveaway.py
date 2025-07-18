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


#NOTE add sleep(1) after gaw-dict = self.gaws
#NOTE anotyer dic for times . Dict = {'18:02'  : msg ids using commad}



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




#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################





class giveaway(commands.Cog):
    def __init__(self, client ):
        self.client = client
        self.gaws = {}
        self.gaw_tasks = {}
        self.man = 1
        self.IST = pytz.timezone('Asia/Kolkata')




    #@tasks.loop(seconds=10)
    async def bg_gaw_loop(self):

        if self.gaws != {}:
            #print(self.gaws)
            gaw_dict = self.gaws
            for msg_ids in gaw_dict:
                #print(f"time now `{str(datetime.nowself.IST)[:-16]}`  time gaw `{str(gaw_dict.get(msg_ids).get('time'))[:-3]}`")
                if (str(datetime.now(self.IST))[:-16] == str(gaw_dict.get(msg_ids).get("time"))[:-3]):
                    #print('equal')

                    channel_gaw = await self.client.fetch_channel(gaw_dict.get(msg_ids).get("channel_id"))
                    gaw_msg = await channel_gaw.fetch_message(msg_ids)
                    host_user = await self.client.fetch_user(gaw_dict.get(msg_ids).get("host_id"))

                    winner_msg = "**NO WINNERS**"
                    if gaw_dict.get(msg_ids).get("num_of_winners") != "0":
                        users = await gaw_msg.reactions[0].users().flatten()
                        users.remove(self.client.user)

                        winner_list = random.sample(users, k= int(gaw_dict.get(msg_ids).get("num_of_winners")))
                        winner_msg = ''
                        for winners in winner_list:
                            winner_msg += f'{winners.mention} '

                    winnerEmbed = discord.Embed(
                        title='🎉 GIVEAWAY WINNERS 🎉', description=f'`{gaw_dict.get(msg_ids).get("prize")}`', color=0x71b4e3)
                    winnerEmbed.add_field(
                        name='Winner(s):', value=f'{winner_msg}', inline=False)
                    winnerEmbed.add_field(
                        name='Giveaway:', value=f'[Click Here]({gaw_msg.jump_url})', inline=False)
                    await channel_gaw.send(embed=winnerEmbed)

                    new_gaw_embed = discord.Embed(
                        title=f'🎉 GIVEAWAY 🎉', description=f'`{gaw_dict.get(msg_ids).get("prize")}`\nWinner(s): {winner_msg} \nNumber of Winner(s): `{gaw_dict.get(msg_ids).get("num_of_winners")}`', color=0x71b4e3)
                    new_gaw_embed.set_footer(
                        text=f'Hosted by {host_user} | Ended at {datetime.now(self.IST).strftime("%d-%m-%Y %H:%M:%S")} IST')
                    await gaw_msg.edit(embed=new_gaw_embed)

                    try:
                        self.gaws.pop(msg_ids)
                    except:
                        asyncio.sleep(3)
                        self.gaws.pop(msg_ids)


    """@bg_gaw_loop.before_loop
    async def before_bg_gaw_loop(self):
        await self.client.wait_until_ready()"""


    @commands.Cog.listener()
    async def on_ready(self):
        print('giveaway cog is working')
    #    self.bg_gaw_loop.start()

    @commands.check_any(is_atriays() ,is_mutant() , is_nerdy() ,is_trimunati())
    @commands.command()
    async def gawcheck(self , ctx):
        await ctx.send(self.gaws)
        await ctx.send(self.gaw_tasks)

    def pop_gaw(self , guild_id , msg_id):
        try:
            self.gaws.get(f"{guild_id}").pop(f"{msg_id}")
            self.gaw_tasks.pop(msg_id)
        except:
            self.pop_gaw(guild_id , msg_id)




    @commands.check(cog_check())
    @commands.check_any(is_atriays() ,is_mutant() , is_nerdy() , commands.has_permissions(kick_members=True),is_trimunati())
    @commands.command(aliases=["stopgiveaway" , "endgaw" , "endgiveaway"])
    async def stopgaw(self , ctx , gaw_id : str):
        #print(type(gaw_id))
        try:
            gaw_dict = self.gaws
        except:
            asyncio.sleep(1)
            gaw_dict = self.gaws

        if gaw_dict.get(str(ctx.guild.id)).get(f"{gaw_id}") == None:
            await ctx.send(f"No current Giveaway with MessageID `{gaw_id}`")
        else:
            await ctx.send(f'Ended Giveaway with MessageID `{gaw_id}`\nPrize => {gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("prize")} ')
            gaw_task = self.gaw_tasks.get(int(gaw_id))
            gaw_task.cancel()

            channel_gaw = await self.client.fetch_channel(gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("channel_id"))
            gaw_msg = await channel_gaw.fetch_message(gaw_id)
            host_user = await self.client.fetch_user(gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("host_id"))



            winner_msg = "**NO WINNERS**"
            if gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("num_of_winners") != '0':
                users = await gaw_msg.reactions[0].users().flatten()
                try:
                    users.remove(self.client.user)
                except:
                    pass
                if len(users) > 0:
                    winner_list = random.sample(users, k= int(gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("num_of_winners")))
                    winner_msg = ''
                    for winners in winner_list:
                        winner_msg += f'{winners.mention} '


            winnerEmbed = discord.Embed(
                title='🎉 GIVEAWAY WINNERS 🎉', description=f'`{gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("prize")}`', color=0x71b4e3)
            winnerEmbed.add_field(
                name='Winner(s):', value=f'{winner_msg}', inline=False)
            winnerEmbed.add_field(
                name='Giveaway:', value=f'[Click Here]({gaw_msg.jump_url})', inline=False)
            await channel_gaw.send(embed=winnerEmbed)

            new_gaw_embed = discord.Embed(
                title=f'🎉 GIVEAWAY 🎉', description=f'`{gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("prize")}`\nWinner(s): {winner_msg} \nNumber of Winner(s): `{gaw_dict.get(str(ctx.guild.id)).get(gaw_id).get("num_of_winners")}`', color=0x71b4e3)
            new_gaw_embed.set_footer(
                text=f'Hosted by {host_user} | Ended at {datetime.now(self.IST).strftime("%d-%m-%Y %H:%M:%S")} IST')
            await gaw_msg.edit(embed=new_gaw_embed)

            self.pop_gaw(guild_id , gaw_msg_id)


#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

    async def gaw_proccess_start(self , gaw_msg_id , end_time_as_object , channel_id , host_user_id , num_of_winners , prize , guild_id ):


        #print(end_time_as_object)

        channel_gaw = await self.client.fetch_channel(channel_id)
        gaw_msg = await channel_gaw.fetch_message(gaw_msg_id)
        host_user = await self.client.fetch_user(host_user_id)

        while(end_time_as_object >= datetime.now(self.IST)):
            #print(str(end_time_as_object - datetime.now(self.IST))[:-7])




            gaw_embed = discord.Embed(
                title=f'🎉 GIVEAWAY 🎉', description=f'`{prize}`\nReact with 🎉 to enter\nEnds at: `{str(end_time_as_object)[:-13]} IST`\nTime Remaining: `{str(end_time_as_object - datetime.now(self.IST))[:-7]}`\nNumber of Winners: `{num_of_winners}`', color=0x71b4e3)
                #gaw_embed.add_field(name = 'Ends at' , value = f'{str(datetime.utcnow() + timedelta(0,time_gaw_sec))[11:-7]} UTC')
            gaw_embed.set_footer(
                text=f'Hosted by {host_user}')
            await gaw_msg.edit(embed = gaw_embed)
            await asyncio.sleep(5)





        winner_msg = "**NO WINNERS**"
        if (num_of_winners != 0):

            users = await gaw_msg.reactions[0].users().flatten()
            #print(users)
            try:
                users.remove(self.client.user)
            except:
                pass

            if len(users) > 0:
                winner_list = random.sample(users, k= int(num_of_winners))
                winner_msg = ''
                for winners in winner_list:
                    winner_msg += f'{winners.mention} '
        winnerEmbed = discord.Embed(
            title='🎉 GIVEAWAY WINNERS 🎉', description=f'`{prize}`', color=0x71b4e3)
        winnerEmbed.add_field(
            name='Winner(s):', value=f'{winner_msg}', inline=False)
        winnerEmbed.add_field(
            name='Giveaway:', value=f'[Click Here]({gaw_msg.jump_url})', inline=False)
        await channel_gaw.send(embed=winnerEmbed)


        new_gaw_embed = discord.Embed(
            title=f'🎉 GIVEAWAY 🎉', description=f'`{prize}`\nWinner(s): {winner_msg} \nNumber of Winner(s): `{num_of_winners}`', color=0x71b4e3)
        new_gaw_embed.set_footer(
            text=f'Hosted by {host_user} | Ended at {datetime.now(self.IST).strftime("%d-%m-%Y %H:%M:%S")} IST')
        await gaw_msg.edit(embed=new_gaw_embed)




        self.pop_gaw(guild_id , gaw_msg_id)
        '''try:
            self.gaws.get(f"{guild_id}").pop(f"{gaw_msg_id}")
            self.gaw_tasks.pop(gaw_msg_id)
        except:
            await asyncio.sleep(1)
            self.gaws.get(f"{guild_id}").pop(f"{gaw_msg_id}")
            self.gaw_tasks.pop(gaw_msg_id)'''











    @commands.check(cog_check())
    @commands.check_any(is_atriays() ,is_mutant() , is_nerdy() , commands.has_permissions(kick_members=True),is_trimunati())
    @commands.command(aliases=['gaw'])
    async def giveaway(self, ctx, time_gaw_raw, channel_gaw : discord.TextChannel, no_of_winners: int = 1, *, prize_gaw: str):

        # time => 10000s , 1000m , 02299h , 22d

        time_gaw = time_gaw_raw[:-1]

        if (time_gaw_raw.endswith('s') or time_gaw_raw.endswith('S')):
            time_gaw_sec = int(time_gaw)
        elif (time_gaw_raw.endswith('m') or time_gaw_raw.endswith('M')):
            time_gaw_sec = 60 * int(time_gaw)

        elif (time_gaw_raw.endswith('h') or time_gaw_raw.endswith('H')):
            time_gaw_sec = 3600 * int(time_gaw)

        elif (time_gaw_raw.endswith('d') or time_gaw_raw.endswith('D')):
            time_gaw_sec = 86400 * int(time_gaw)
        else:
            await ctx.send('Invalid Time.')
            return

        if no_of_winners < 0:
            await ctx.send('Invalid Number of Winners')
            return




        # , description = f'Hosted by: {ctx.author.mention}'
        end_time_as_object = datetime.now(self.IST) + timedelta(0,time_gaw_sec)

        end_time = str(datetime.now(self.IST) + timedelta(0,time_gaw_sec))[:-13]
        gaw_embed = discord.Embed(
            title=f'🎉 GIVEAWAY 🎉', description=f'`{prize_gaw}`\nReact with 🎉 to enter\nEnds at: `{end_time} IST`\nTime Remaining: `{str(end_time_as_object - datetime.now(self.IST))}`\nNumber of Winners: `{no_of_winners}`', color=0x71b4e3)
        #gaw_embed.add_field(name = 'Ends at' , value = f'{str(datetime.utcnow() + timedelta(0,time_gaw_sec))[11:-7]} UTC')
        gaw_embed.set_footer(
            text=f'Hosted by {ctx.author}')
        #PST = pytz.timezone('Etc/GMT-8')

        #gaw_embed.set_footer(text = f'{datetime.utcnow().strftime("%H:%M:%S")} UTC\n{datetime.now(PST).strftime("%H:%M:%S")} PST\n{datetime.now(self.IST).strftime("%H:%M:%S")} IST')

        gaw = await channel_gaw.send(embed=gaw_embed)
        await gaw.add_reaction('🎉')

        self.gaws[f"{gaw.guild.id}"] = {f"{gaw.id}" : {"time" : f"{end_time}" , "channel_id" : f"{channel_gaw.id}" , "prize" : f'{prize_gaw}' , "host_id" : f"{ctx.author.id}" , "num_of_winners" : f"{no_of_winners}" }}
        #print(self.gaws)
        #task = asyncio.create_task(self.test())
        #print(task)
        gaw_task = asyncio.create_task(self.gaw_proccess_start(gaw.id , end_time_as_object , channel_gaw.id , ctx.author.id , no_of_winners , prize_gaw , gaw.guild.id))
        self.gaw_tasks[gaw.id] = gaw_task
        await gaw_task






        #self.gaw_tasks[f"{gaw.id}"] = task
        #print(self.gaw_tasks)
        # await asyncio.sleep(time_gaw_sec)


    '''async def get_winners():
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
            text=f'Hosted by {ctx.author} | Ended at {datetime.now(self.IST).strftime("%d/%m/%Y %H:%M:%S")} IST')
        await gaw.edit(embed=new_gaw_embed)'''

    @commands.check(cog_check())
    @commands.check_any(is_atriays() ,is_mutant() , is_nerdy() , commands.has_permissions(kick_members=True),is_trimunati())
    @commands.command()
    async def reroll(self, ctx, gaw_msg_id: int, numb_of_rerolls: int = 1):

        gaw_msg = await ctx.fetch_message(gaw_msg_id)

        users = await gaw_msg.reactions[0].users().flatten()
        try:
            users.pop(self.user.client)
        except:
            pass

        winner_list = random.sample(users, k=numb_of_rerolls)
        if len(winner_list) <= 0:
            winner_msg = '**NO WINNERS**'

        else:
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
#    client.loop.create_    task(gawclass.bg_gaw_loop())
    client.add_cog(giveaway(client))
