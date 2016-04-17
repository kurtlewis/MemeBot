import os
import redditmemes
import database

def parseUserArguments(num):
	#set some defaults. Subject to change
	sizeDatabase = 100
	acceptablePop = 10
	
	#create local object
	newMeme = Meme()
	newMeme = None
	
	#check database for memes
	for i in range (0, numMemes):
		newMeme = getMeme(nullList)
	
		#check usage, availability
		if newMeme.popularity < acceptablePop or newMeme == None:
			
			#get meme from AWS
			
			#cycle through subreddits. 
			#Keep track of current subreddit in subFile.txt
			subredditChoice = open('subFile.txt','r+')
			choice = int(subredditChoice.read())
			subredditChoice.close()
			
			sub = ["blackpeopletwitter","me_irl","meow_irl","holdmybeer","notmyjob","memes","adviceanimals"]
				
			if choice == 6:
				choice = -1
				
			#call Zach's function to get 20 memes
			filenames = redditmemes.getSomeMemes(sub, 20)
			
			#write value of next subreddit back to file	
			choice = choice + 1
			choice = repr(choice)
			subredditChoice.write(choice)
			subredditChoice.close()
			
			for x in filenames:
				#parsing filename
				extension = filename.split(".")[-1]
				source = filename.split("_")[-7]
				subreddit = filename.split("_")[-6]
				imgHost = filename.split("_")[-2]
				id = filename.split("_")[-1]
				
				#concatenate to form link to image
				if imgHost = "imgur":
					link = "i.imgur.com/" + id + "." + extension			
				#Populate object fields
				newMeme.awsDirectory
				newMeme.imgLink = link
				newMeme.popularity = 1
				newMeme.tagsList = [sub]
				
				#save to database
				#storeMeme(newMeme):
			break
			
	#writes the ID of the returned meme to use in the evaluateFeedback function		
	memeID = open('memeID.txt','w')
	memeID.write(newMeme.id)
	memeID.close()
		
	#return meme to bot
	return newMeme
	
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
		
parseUserArguments(1)