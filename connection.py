import os
import redditmemes
import database

def parseUserArguments(num):
	#set some defaults. Subject to change
	sizeDatabase = 100
	acceptablePop = 10
	nullList = list()
	
	
	#check database for memes
	for i in range (0, num):
		newMeme = getMeme(nullList)
	
		#check usage, availability
		if newMeme == None or newMeme.popularity < acceptablePop:
			
			#get meme from AWS
			
			#cycle through subreddits. 
			#Keep track of current subreddit in subFile.txt
			subredditChoice = open('subFile.txt','r')
			choice = int(subredditChoice.read())
			subredditChoice.close()
			
			sub = ["blackpeopletwitter","me_irl","meow_irl","notmyjob","memes","adviceanimals"]
				
			#call Zach's function to get 20 memes
			filenames = redditmemes.getSomeMemes(sub[choice], 20)	
				
			if choice == 5:
				choice = -1			
			
			#write value of next subreddit back to file	
			choice_s = repr(choice+1)
			subredditChoice = open('subFile.txt','w')
			subredditChoice.write(choice_s)
			subredditChoice.close()
			
			for x in filenames:
				#parsing filename
				extension = filename.split(".")[-1]
				source = filename.split("_")[-7]
				subreddit = filename.split("_")[-6]
				imgHost = filename.split("_")[-2]
				id = filename.split("_")[-1]
				
				#concatenate to form link to image
				if imgHost == "imgur":
					link = "i.imgur.com/" + id + "." + extension			
				#Populate object fields
				popularity = 1
				tagsList = [sub[choice]]
				
				#create local object
				newMeme = database.Meme(link,tagsList,popularity)
				
				#save to database
				storeMeme(newMeme)
			break
			
	#writes the ID of the returned meme to use in the evaluateFeedback function		
	
	# memeID = open('memeID.txt','w')
	# memeID.write(newMeme.id)
	# memeID.close()
		
	#return meme link to bot
	return newMeme.link
	
# def evaluateFeedback(num): 
	# #reads from file to see which ID the user is referring to
	# memeID = open('subredditChoiceFile','r')
	# id = memeID.read()
	# memeID.close()
	# if num == 0:
		# #tell database to add one to the popularity
		# updatePop(id, 1)
	# if num = 1:
		# #tell database to subtract one to the popularity
		# updatePop(id, -1)
		