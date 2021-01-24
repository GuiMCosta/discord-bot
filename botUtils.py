import os

def getOnMembersInVoiceGeneral(discord, guild):
	channel = discord.utils.get(guild.channels, name="General", type=discord.ChannelType.voice)
	members = channel.members
	return [member.id for member in members]
	
def getMemberNickById(userId, discord, guild):
	channel = discord.utils.get(guild.channels, name="General", type=discord.ChannelType.voice)
	members = channel.members
	for m in range (len(members)):
		if int(members[m].id) == int(userId):
			return members[m].nick
			
def getMember(discord, guild, userId):
	channel = discord.utils.get(guild.channels, name="General", type=discord.ChannelType.voice)
	members = channel.members
	for m in range (len(members)):
		if int(members[m].id) == int(userId):
			return members[m]

def VerifyIfMemberIsOn(discord, guild, userId):
	channel = discord.utils.get(guild.channels, name="General", type=discord.ChannelType.voice)
	members = channel.members
	for m in range (len(members)):
		if int(members[m].id) == int(userId):
			return 1
	
	return 0
	
