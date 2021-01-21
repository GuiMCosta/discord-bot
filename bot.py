import os
import sys
import discord
import botUtilities
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)
votos = 0

@client.event
async def on_ready():
	for guild in client.guilds:
		members = '\n - '.join([member.name for member in guild.members])
		print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.content.lower() == '$takasrage':
        await message.channel.send("Estamos a 0 dias", tts=True)

    if message.content.lower().startswith("$mute"):
        userId = message.content[9:(len(message.content)-1)]

client.run(TOKEN)
