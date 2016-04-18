import os
import redditmemes
import database

def parseUserArguments(num):
	#set some defaults. Subject to change
	acceptablePop = 20
	nullList = list()
	
	
	#check database for memes
	for i in range (0, num):
		newMeme = database.getMeme(nullList)

		#check usage, availability		
		if newMeme is None or newMeme.popularity <= acceptablePop:
			#cycle through subreddits. 
			#Keep track of current subreddit in subFile.txt
			subredditChoice = open('subFile.txt','r')
			choice = int(subredditChoice.read())
			subredditChoice.close()
			
			sub = ["me_irl","meow_irl","woofbarkwoof","notmyjob","firstworldanarchists"]
				
			#call Zach's function to get 7 memes
			filenames = redditmemes.getSomeMemes(sub[choice], 7)	
				
			if choice == 4:
				choice = -1			
			
			#write value of next subreddit back to file	
			choice_s = repr(choice+1)
			subredditChoice = open('subFile.txt','w')
			subredditChoice.write(choice_s)
			subredditChoice.close()
			
			for i,x in enumerate(filenames):
				#parsing filename
				extension = x.split(".")[-1]
				source = x.split("_")[-7]
				subreddit = x.split("_")[-6]
				imgHost = x.split("_")[-2]
				id = x.split("_")[-1]
				
				
				#concatenate to form link to image

				link = "http://i.imgur.com/" + id	
				#Populate object fields
				popularity = 25
				tagsList = [sub[choice]]
				
				#create local object
				if i != len(filenames)-1:
					newMeme = database.Meme(link,tagsList,popularity)
				else:
					newMeme = database.Meme(link,tagsList,0)
				#save to database
				database.storeMeme(newMeme)
			break

		else:
			#If database meme is accepted
			newMeme.popularity = 0
			database.storeMeme(newMeme)
		

	#return meme link to bot
	return newMeme.imgLink
	

