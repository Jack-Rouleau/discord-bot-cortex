import discord
import asyncio
import random
import os
import json

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
        if not os.path.isfile("quote_file.json"):
            quote_list = []
        else:
            with open("quote_file.json", "r") as quote_file:
                quote_list = json.load(quote_file)
        quote_list.append(message.content[10:])
        with open("quote_file.json", "w") as quote_file:
            json.dump(quote_list, quote_file)
    elif message.content.startswith('!quote'):
        with open("quote_file.json", "r") as quote_file:
            quote_list = json.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))

with open("..\Local\key.json", "r") as key_file:
    key = json.load(key_file)
client.run(key)

