import nest_asyncio
import discord
from currency import get_cur
from table import update
from table import get_voltage
from get_period import get_image
from get_prediction import get_prediction
from tokens import TOKEN

# from bs4 import BeautifulSoup


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
        await message.channel.send(get_cur(' '.join(message.content.split()[1:])))
        print(' '.join(message.content.split()[1:]))

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

    if message.content.startswith(prefix + 'pred'):
        await message.channel.send("На завтра ожидается курс: "+str(round(get_prediction(' '.join(message.content.split()[1:])),5)))

if __name__ == "__main__":
    client.run(TOKEN)
