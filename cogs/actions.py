import discord
from discord.ext import commands
from PIL import Image
import requests
from io import  BytesIO

class actions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('actions cog is working')


    batman = 'https://cdn.discordapp.com/attachments/792026292781973515/793810852700094475/Batman-Slapping-Robin-Meme-Explained.png'
    @commands.command()
    async def slap(self, ctx, user : discord.Member = None):
        batman = 'https://cdn.discordapp.com/attachments/792026292781973515/793810852700094475/Batman-Slapping-Robin-Meme-Explained.png'
        if user == None :
            user = ctx.author

            userpfp = user.avatar_url

            #img = Image.open(urlopen(url))
            #opening the imgs in pillow

            batman_opened = Image.open(BytesIO(requests.get(batman).content))
            pfp_opened = Image.open(BytesIO(requests.get(userpfp).content))

            #resizing the pfp
            pfp_opened = pfp_opened.resize((320,320))

            #pasting the pfp on the slap bg
            batman_opened.paste(pfp_opened, (290,215))
            batman_opened = batman_opened.resize((round(batman_opened.size[0]*0.), round(batman_opened.size[1]*0.5)))

            #batman_opened.save('slap.png')

            with BytesIO() as image_binary:
                batman_opened.save(image_binary, "PNG")
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary,filename="slapppppp.png"))


        else:

            userpfp = user.avatar_url

            #img = Image.open(urlopen(url))
            #opening the imgs in pillow

            batman_opened = Image.open(BytesIO(requests.get(batman).content))
            pfp_opened = Image.open(BytesIO(requests.get(userpfp).content))

            #resizing the pfp
            pfp_opened = pfp_opened.resize((320,320))

            #pasting the pfp on the slap bg
            batman_opened.paste(pfp_opened, (290,215))
            batman_opened = batman_opened.resize((round(batman_opened.size[0]*0.), round(batman_opened.size[1]*0.5)))

            #batman_opened.save('slap.png')

            with BytesIO() as image_binary:
                batman_opened.save(image_binary, "PNG")
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary,filename="slapppppp.png"))


def setup(client):
    client.add_cog(actions(client))
