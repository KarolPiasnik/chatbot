import discord, requests
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

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