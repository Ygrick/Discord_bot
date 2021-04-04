import nest_asyncio
import discord
from currency import get_cur
from table import update
# from bs4 import BeautifulSoup

TOKEN = "ODEwMDg4ODQ3MDk3NDYyNzk2.YCekBw.7MADVjHD6NQdJiuc8-ZYQz6KS9o"



nest_asyncio.apply()
intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    update()


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!'):
        await message.channel.send(get_cur(message.content[1:]))
        print(message.content[1:])


client.run(TOKEN)
