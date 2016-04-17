import os
import redditmemes
import database

def parseUserArguments(num):
	#set some defaults. Subject to change
	acceptablePop = 10
	nullList = list()
	
	
	#check database for memes
	for i in range (0, num):
		newMeme = database.getMeme(nullList)
		print("return popularity: {}".format(newMeme.popularity))
	
		#check usage, availability
		if not (newMeme is None or newMeme.popularity < acceptablePop-10):
			print("popularity: {} and acceptablePop: {}".format(newMeme.popularity, acceptablePop-10))
		
		if newMeme is None or newMeme.popularity < acceptablePop-10:
			
			#get meme from AWS
			
			#cycle through subreddits. 
			#Keep track of current subreddit in subFile.txt
			subredditChoice = open('subFile.txt','r')
			choice = int(subredditChoice.read())
			subredditChoice.close()
			
			sub = ["me_irl","meow_irl","woofbarkwoof","notmyjob","firstworldanarchists"]
				
			#call Zach's function to get 20 memes
			filenames = redditmemes.getSomeMemes(sub[choice], 20)	
				
			if choice == 4:
				choice = -1			
			
			#write value of next subreddit back to file	
			choice_s = repr(choice+1)
			subredditChoice = open('subFile.txt','w')
			subredditChoice.write(choice_s)
			subredditChoice.close()
			
			for x in filenames:
				#parsing filename
				extension = x.split(".")[-1]
				source = x.split("_")[-7]
				subreddit = x.split("_")[-6]
				imgHost = x.split("_")[-2]
				id = x.split("_")[-1]
				
				#concatenate to form link to image
				if imgHost == "imgur":
					link = "http://i.imgur.com/" + id			
				#Populate object fields
				popularity = 10
				tagsList = [sub[choice]]
				
				#create local object
				newMeme = database.Meme(link,tagsList,popularity)
				
				#save to database
				database.storeMeme(newMeme)
			break
			
		
	#return meme link to bot
	return newMeme.imgLink
	