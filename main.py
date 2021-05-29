import nest_asyncio
import discord
from currency import get_cur
from table import update
from table import get_voltage
from get_period import get_image

# from bs4 import BeautifulSoup

TOKEN = "ODEwMDg4ODQ3MDk3NDYyNzk2.YCekBw.7MADVjHD6NQdJiuc8-ZYQz6KS9o"

prefix = '!'

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

    if message.content.startswith(prefix + 'cur'):
        await message.channel.send(get_cur(message.content.split()[1]))
        print(message.content.split()[1])

    if message.content.startswith(prefix + 'range'):
        content = message.content.split()
        ln = len(content)
        curr = content[1:ln-2]
        curr = ' '.join(curr)
        start_date = content[-2]
        end_date = content[-1]
        img = get_image(curr, start_date, end_date)
        await message.channel.send(file=discord.File(img))
        # print(content)
        print(curr)
        # await message.channel.send(img)
    if message.content.startswith(prefix + 'prediction'):
        await message.channel.send("Пока в разработке")


if __name__ == "__main__":
    client.run(TOKEN)
