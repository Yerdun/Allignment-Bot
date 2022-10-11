import discord
import json
from calcAllign import calculate_alignment
import os

#format for dictionary works as the following: word: (chaotic-lawful) (evil-good)

if os.name == "posix": 
    botID = open("ignore_files/token.txt", "r")
elif os.name == "nt":
    botID = open("ignore_files\\token.txt", "r")

TOKEN = botID.read()
client = discord.Client()


@client.event
async def on_ready():
    print("Bot turned on")


# When each message plays
@client.event
async def on_message(message):
    # ensures bot does not read itself
    if message.author == client.user:
        return
    # Takes Discord account info and message content
    username = str(message.author)
    usernameID = str(message.author.id)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} {usernameID}: {user_message} ({channel})')

    if message.content.lower().startswith("!alignment"):
        await message.channel.trigger_typing()
        messages = []
        async for my_message in message.channel.history(limit=None).filter(
                lambda x:
                x.author.id == message.author.id and not x.content.startswith("!")
        ):
            messages.append(my_message)
            if len(messages) > 100:
                break
        print([msg.content for msg in messages])
        print(len(messages))
        await message.channel.send(calculate_alignment([msg.content for msg in messages]))

botID.close()

client.run(TOKEN)
