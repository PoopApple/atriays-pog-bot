import discord
from discord.ext import commands


class actions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('spam cog is working')


    # repeat cmd
    @commands.command()
    async def repeat(self,ctx, numrepeat=2, *, repeatthis):
        if (numrepeat >= 1 and numrepeat <= 30):
            for numrepeat in range(1, numrepeat+1):
                await ctx.send(repeatthis)
                numrepeat = numrepeat - 1




    # spam cmd
    @commands.command()
    async def spam(self,ctx, numspam=2, * , pingmember: discord.Member):
        if (numspam >= 1 and numspam <= 5):
            for numspam in range(1, numspam+1):
                await ctx.send(pingmember.mention)
                numspam = numspam - 1



def setup(client):
    client.add_cog(actions(client))
