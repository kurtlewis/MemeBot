#Group Me interface for MemeBot
import groupy

bots = groupy.Bot.list()

for bot in bots:	
	print(bot.Group)
