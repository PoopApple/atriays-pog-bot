import discord
from discord.ext import commands


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
        if message.author == self.client:
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
