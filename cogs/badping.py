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
        enabled = cog['badping']
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


class badpings(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('badpings is working')


    @commands.Cog.listener()
    async def on_message(self, message):
        badpings = ['543718305773387776','516173155216392193']  # ids of bad pings

        message.author: discord.member
        if message.author.id == self.client.user.id:
            return
        elif cogcheck(message) == False:
            return


        #elif message.author.bot:
        #    return
        else:
            messageContent = message.content
            messageMentions = message.mentions
            if len(messageContent) > 0:
                if len(messageMentions) > 0 :
                    l = len(messageMentions) - 1
                    badl = len(badpings) - 1
                    print(l)
                    while (l > -1):
                        while (badl > -1):
                            mentions = [ message.mentions[l]]
                            badmention = badpings[badl]
                            if badmention in  f' {mentions}':
                                await message.channel.send(f"**Don't** Ping him, U Poopi {message.author.mention} :poop:" )
                                l= l - 1
                                badl -= 1
                            else:
                                l = l-1
                                badl -= 1

def setup(client):
    client.add_cog(badpings(client))
