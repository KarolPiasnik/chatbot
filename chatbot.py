import discord, requests
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message(message):
    if message.author.name != 'Chatbot restaurant':
        rasaAddress = 'http://localhost:5005/webhooks/rest/webhook'
        r = requests.post(rasaAddress, json={"sender": "restaurantBot", "message": message.content})
        await message.channel.send(r.json()[0]['text'])

client.run('tokenhere')
