from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os,sys,inspect
import requests
import json


class Bot:
	def __init__(self, groupID, botID):
		self.groupID = groupID
		self.botID = botID

def getBots():
	file = open('GroupMeBots.txt', 'r')
	bots = list()
	for line in file:
		if ('#' != line[0]):
			line = line.strip('\n')
			IDs = line.split(", ")
			bots.append(Bot(IDs[0], IDs[1]))
	file.close()
	return bots

# Create your views here.
@csrf_exempt
def message(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		text = body['text']
		text = text.lower()
		if 'memebot' in text:
			args = text.split(' ')
			#memes from conncection
			currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
			parentdir = os.path.dirname(currentdir)
			parentdir = os.path.dirname(parentdir)
			sys.path.insert(0, parentdir)
			import connection
			link = connection.parseUserArguments(1)

			groupID = body['group_id']
			botID = ""
			bots = getBots()
			for bot in bots:
				if groupID == bot.groupID:
					botID = bot.botID
					break
			payload = {'bot_id': botID, 'text': 'Did someone request a meme? ' + link}

			r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)
				
			#r = requests.post("https://api.groupme.com/v3/bots/post?bot_id=6d6ba25b737f0906bc0c36ea39&text=dank+memes+from+page")
	return HttpResponse("Hello, world. You are at the views for this")
