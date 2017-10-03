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


client.run('MjQyMzA3OTU2OTMzMTMyMjg4.DLSApg.w5I3VxX4UvzllAWmUmt09bNw45A')

