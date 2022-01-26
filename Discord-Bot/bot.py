import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    spongebob_quotes = [
        'I\'m the one who lives at the bottom of the sea',
        'SpongeBot!',
        (
            'Hey Patrick, what\'s funnier than 24? '
            '25!'
        ),
    ]

    office_quotes = [
        'I\'m an early bird and I\'m a night owl. So I\'m wise and I have worms.',
        'I saved a life. My own. Am I a hero?... I really can\'t say, but yes!',
        'Nothing stresses me out. Except having to seek the approval of my inferiors.',
        'Before I do anything I ask myself "Would an idiot do that?" and if the answer is yes I do not do that thing.',
    ]

    if message.content == 'apple!':
       # response = random.choice(spongebob_quotes)
        response = random.choice(office_quotes)
        await message.channel.send(response)

client.run(TOKEN)
