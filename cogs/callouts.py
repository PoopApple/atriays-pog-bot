import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import json

def update_cogs_file():
    ref = db.reference(f'cogs')
    data = ref.get()
    with open(os.path.dirname(__file__) + '/../cog_data.json', "w") as cog__data:
        json.dump(data, cog__data, indent = 4)


with open(f'{os.path.dirname(__file__) + "/../cog_data.json"}') as f:
  cog_data = json.load(f)


def cogcheck(message):

    cog = cog_data.get(str(message.guild.id))

    if cog != None:
        enabled = cog['callouts']
        return enabled == '1';
    else:
        ref = db.reference(f'cogs/{message.guild.id}')
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
        return False;


class callouts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('callouts is working')


    @commands.Cog.listener()
    async def on_message(self, message):
        his = ['hi', 'hello', 'hlo', 'Hi', 'Hello', 'Hlo', 'yo', 'Yo']
        shuts = ['shut', 'SHUT', 'Shut']
        aht = ['all hail trimunati', 'ALL HAIL TRIMUNATI', 'aht' , 'Aht']
        dont = ['dont', 'Dont', "Don't", "don't"]

        message.author: discord.member
        if message.author.id == self.client.user.id:
            return
        elif cogcheck(message) == False:
            return

        messageContent = message.content
        messageMentions = message.mentions
        if len(messageContent) > 0:
            for word in his:
                if word == messageContent:
                    await message.channel.send(random.choice(his))
            for words in shuts:
                if words == messageContent:
                    await message.channel.send(':regional_indicator_s: :regional_indicator_h: :regional_indicator_u: :regional_indicator_t:')
            for words in aht:
                if words == messageContent:
                    await message.channel.send(':regional_indicator_a: :regional_indicator_l: :regional_indicator_l:   :regional_indicator_h: :regional_indicator_a: :regional_indicator_i: :regional_indicator_l:   :regional_indicator_t: :regional_indicator_r: :regional_indicator_i: :regional_indicator_m: :regional_indicator_u: :regional_indicator_n: :regional_indicator_a: :regional_indicator_t: :regional_indicator_i:')
            for words in dont:
                if words == messageContent:
                    await message.channel.send(':regional_indicator_d: :regional_indicator_o: :regional_indicator_n: :regional_indicator_t:')



def setup(client):
    client.add_cog(callouts(client))
