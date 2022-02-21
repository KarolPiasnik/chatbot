import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message(message):
    if message.author.name != 'Chatbot restaurant':
        await message.channel.send('Pong!')

client.run('OTQ1MDUyMTc1NTEwNDI1NjEy.YhKibA.yMQUIYQ-zzpRVfIerf2FqNjBg6o')
