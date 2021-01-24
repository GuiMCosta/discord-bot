import os
import sys

from dotenv import load_dotenv

import botUtils

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = '$', intents=intents)

userId = 0
votos = 0
totalMembersOn = 0
voteOnToMute = 0
voteOnToUnmute = 0

def resetVariables():
	global votos, totalMembersOn, userId, voteOn
	
	votos = 0
	voteOnToMute = 0
	voteOnToUnmute = 0
	totalMembersOn = 0
	userId = 0

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='takasrage')
async def takas_rage(ctx):
	await ctx.send("Estamos a 0 dias", tts=True)
	
@bot.command(name='mute')
async def mute_member(ctx, user):
	resetVariables()

	global votos, totalMembersOn, userId, voteOnToMute

	try:
		userId = int(user[3:(len(user)-1)])
	except:
		await ctx.send('O usuário não foi digitado com a utilização de menção')
	
	guild = ctx.guild
	memberIsOn = botUtils.VerifyIfMemberIsOn(discord, guild, userId)
	
	if memberIsOn == 0:
		await ctx.send("O usuário digitado não está online")
		return
	
	voteOnToMute = 1
	
	members = botUtils.getOnMembersInVoiceGeneral(discord, guild)
	totalMembersOn = len(members)
	userToMute = botUtils.getMemberNickById(userId, discord, guild)
	
	await ctx.send(f'Digite $vote na votação para mutar {userToMute} ou digite $cancelVote para cancelar a votação')
	await ctx.send(f'Votação está em 1/{totalMembersOn}')
	
	votos += 1

@bot.command(name='unmute')
async def unmute_member(ctx, user):
	global votos, totalMembersOn, userId, voteOnToUnmute

	try:
		userId = int(user[3:(len(user)-1)])
	except:
		await ctx.send('O usuário não foi digitado com a utilização de menção')
	
	guild = ctx.guild
	memberIsOn = botUtils.VerifyIfMemberIsOn(discord, guild, userId)
	
	if memberIsOn == 0:
		await ctx.send("O usuário digitado não está online")
		return
	
	voteOnToUnmute = 1
	
	members = botUtils.getOnMembersInVoiceGeneral(discord, guild)
	totalMembersOn = len(members)
	userToUnmute = botUtils.getMemberNickById(userId, discord, guild)
	
	await ctx.send(f'Digite $vote na votação para desmutar {userToUnmute} ou digite $cancelVote para cancelar a votação')
	await ctx.send(f'Votação está em 1/{totalMembersOn}')
	
	votos += 1

@bot.command(name='vote')
async def vote(ctx):
	global votos, totalMembersOn, userId, voteOnToMute, voteOnToUnmute
	
	if voteOnToMute == 1:
		votos += 1
		await ctx.send(f'Votação está em {votos}/{totalMembersOn}')
		
		if votos >= (totalMembersOn/2):
			guild = ctx.guild
			member = botUtils.getMember(discord, guild, userId)
		
			await member.edit(mute=True)
			await ctx.send(f'{member.nick} mutado')
			
			resetVariables()
	elif voteOnToUnmute == 2:
		votos += 1
		await ctx.send(f'Votação está em {votos}/{totalMembersOn}')
		
		if votos >= (totalMembersOn/2):
			guild = ctx.guild
			member = botUtils.getMember(discord, guild, userId)
		
			await member.edit(mute=True)
			await ctx.send(f'{member.nick} mutado')
			
			resetVariables()
	else:
		await ctx.send("Nenhuma votação iniciada")

@bot.command(name='cancelVote')
async def cancel_vote(ctx):
	resetVariables()

bot.run(TOKEN)
