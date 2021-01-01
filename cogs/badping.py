import discord
from discord.ext import commands


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
        if message.author.id == 779068718486519828:
            return
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
