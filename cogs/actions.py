import discord
import json
from discord.ext import commands
from PIL import Image
import requests
from io import BytesIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os


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








class actions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('actions cog is working')



    def slaplol(self,pfp_url : str):
        batman = 'https://cdn.discordapp.com/attachments/792026292781973515/793810852700094475/Batman-Slapping-Robin-Meme-Explained.png'
        batman_opened = Image.open(BytesIO(requests.get(batman).content))
        pfp_opened = Image.open(BytesIO(requests.get(pfp_url).content))

        #resizing the pfp
        pfp_opened = pfp_opened.resize((320,320))

        #pasting the pfp on the slap bg
        batman_opened.paste(pfp_opened, (290,215))
        batman_opened = batman_opened.resize((round(batman_opened.size[0]*0.5), round(batman_opened.size[1]*0.5)))

        with BytesIO() as image_binary:
            batman_opened.save(image_binary, "PNG")
            image_binary.seek(0)
            #batman_opened.save('slap.png')
            return discord.File(fp=image_binary,filename="slapppppp.png")

    @commands.check(cog_check())
    @commands.command()
    async def slap(self, ctx, user : discord.Member = None):
        if user == None :
            user = ctx.author
            userpfp = user.avatar_url
            file = self.slaplol(userpfp)
            await ctx.send(file= file)

        else:
            userpfp = user.avatar_url
            file = self.slaplol(userpfp)
            await ctx.send(file= file)


def setup(client):
    client.add_cog(actions(client))
