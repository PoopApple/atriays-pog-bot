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


def cog_check():
    def predicate(ctx):

        cog = cog_data.get(str(ctx.guild.id))

        if cog != None:
            enabled = cog['spam']
            return enabled == '1';
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
            return False;
    return predicate;


def cogcheck():
    def predicate(ctx):

        ref = db.reference('cogs')
        ref = db.reference(f'cogs/{ctx.guild.id}')
        cog = ref.get()

        if ref.get() != None:
            print('lol man its there')
            actions_enabled = cog['spam']
            return actions_enabled == '1';
        else:
            print('it not there man')
            ref = db.reference(f'cogs/{ctx.guild.id}')
                # Generate a reference to a location
            emp_ref = ref.update(
                    {
                    'actions': '1',
                    'badping': '0',
                    'spam': '0',
                    'callouts': '0'
                    }
                )
            return False;
    return predicate;

class actions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('spam cog is working')


    # repeat cmd
    @commands.check(cogcheck())
    @commands.command()
    async def repeat(self,ctx, numrepeat=2, *, repeatthis):
        if (numrepeat >= 1 and numrepeat <= 30):
            for numrepeat in range(1, numrepeat+1):
                await ctx.send(f"```{repeatthis}```")
                numrepeat = numrepeat - 1




    # spam cmd
    @commands.check(cogcheck())
    @commands.command()
    async def spam(self,ctx, numspam=2, * , pingmember: discord.Member):
        if (numspam >= 1 and numspam <= 5):
            for numspam in range(1, numspam+1):
                await ctx.send(pingmember.mention)
                numspam = numspam - 1



def setup(client):
    client.add_cog(actions(client))
