from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import requests
import json


class Bot:
	def __init__(self, groupID, botID):
		self.groupID = groupID
		self.botID = botID

def getBots():
	file = open('bots.txt', 'r')
	bots = list()
	for line in file:
		#line = line.strip('\n')
		IDs = line.split(", ")
		bots.append(Bot(IDs[0], IDs[1]))
	close('bots.txt')
	return bots

# Create your views here.
@csrf_exempt
def message(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		text = body['text']
		print(text)
		text = text.lower()
		if 'memebot' in text:
			#args = text.split(' ')
			#memes from laura

			#groupID = body['group_id']
			botID = ""
			bots = getBots()
			"""
			for bot in bots:
				if groupID == bot.groupID:
					botID = bot.botID
					break
			"""
			#payload = {'bot_id': botID, 'text': 'Hey this bot requested a meme.'}

			#r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)
				
			r = requests.post("https://api.groupme.com/v3/bots/post?bot_id=6d6ba25b737f0906bc0c36ea39&text=dank+memes+from+page")
	return HttpResponse("Hello, world. You are at the views for this")
