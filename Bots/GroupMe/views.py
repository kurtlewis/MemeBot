from django.http import HttpResponse
from rest_framework.decorators import detail_route
from django.views.decorators.csrf import csrf_exempt
import requests


# Create your views here.
@csrf_exempt
def message(request):
	if request.method == "POST":
		print(request.POST)
		payload = {'bot_id': '6d6ba25b737f0906bc0c36ea39', 'text': 'Webpage+visited.'}
		#r = requests.post("https://api.groupme.com/v3/bots/post', data=payload)
		r = requests.post("https://api.groupme.com/v3/bots/post?bot_id=6d6ba25b737f0906bc0c36ea39&text=dank+memes+from+page")
	return HttpResponse("Hello, world. You are at the views for this")
