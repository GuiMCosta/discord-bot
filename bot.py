import os
import sys
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	for guild in client.guilds:
		members = '\n - '.join([member.name for member in guild.members])
		print(f'Guild Members:\n - {members}')

	print ("teste")
client.run(TOKEN)