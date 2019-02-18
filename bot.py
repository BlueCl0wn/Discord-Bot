import discord
from discord.ext import commands
import time

print(discord.__version__)
print("----------------")

client = commands.Bot(command_prefix = ".")


#def emoji(smiley):
    #if ":"+ smiley + ":" not in message.content:
        #if smiley in message.content:
            #string = message.content
            #start = string.find(smiley)
            #end = string.find(smiley) + 8
            #text = string[:start] + ":" + smiley + ":" + string[end:]
            #await client.send_message(message.channel, text)
#emoji("eggplant") """In on_message() function."""

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------------")

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if message.content == "cookie":
            await client.send_message(message.channel, ":cookie:")
        if message.content == "hello":
            await client.send_message(message.channel, "Hello %s" % (message.author.name))
        if message.content.upper().startswith("/SAY"):
            args = message.content.split(" ")
            await client.send_message(message.channel, " ".join(args[1:]))
            await client.delete_message(message)
        if "DAREK" in message.content.upper():
            await client.send_message(message.channel, "__**Darek macht nur Scheiße!**__")

client.run("NTQzMTgzMjYzNjgyNzg5NDA3.D0jhVA.ryvcBQy0kK2zUdXEM-jhsUj1kgY")
