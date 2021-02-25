import nest_asyncio
import discord
import requests
from bs4 import BeautifulSoup
from bot_token import TOKEN

nest_asyncio.apply()
intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
client = discord.Client(intents=intents)


def get_dollar():
    html = requests.get('https://www.cbr.ru/').text
    soup = BeautifulSoup(html)
    mydivs = soup.findAll("div", {"class": "col-md-2 col-xs-9 _right mono-num"})
    return (mydivs[0].text)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('курс доллара'):
        await message.channel.send(get_dollar())

client.run(TOKEN)
