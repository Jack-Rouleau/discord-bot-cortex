import discord

from quote import Quote

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):
    if message.content.startswith('!addquote'):
        Quote.add(message.content[10:])
    elif message.content.startswith('!quote'):
        await client.send_message(message.channel, Quote.random())

with open("..\Local\key.json", "r") as key_file:
    key = json.load(key_file)
client.run(key)


