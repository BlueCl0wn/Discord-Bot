import discord
from discord.ext import commands

print(discord.__version__)
print("----------------")

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Looged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------------")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

client.run("NTQzMTgzMjYzNjgyNzg5NDA3.D0jhVA.ryvcBQy0kK2zUdXEM-jhsUj1kgY")
