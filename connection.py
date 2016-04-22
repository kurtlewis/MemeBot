import os
import redditmemes
import database

def parseUserArguments(num):
	#set some defaults. Subject to change
	acceptablePop = 20
	
	#check database for memes
	for i in range (0, num):
		newMeme = [database.getMeme(list())]

		#check usage, availability		
		if newMeme[0] is None or newMeme[0].popularity <= acceptablePop:
			#cycle through subreddits. 
			#Keep track of current subreddit in subFile.txt
			with open('subFile.txt','r') as subredditChoice:
				choice = int(subredditChoice.read())
			
			sub = ["me_irl","meow_irl","woofbarkwoof","notmyjob","firstworldanarchists", "memes"]
				
			#call Zach's function to get 7 memes
			filenames = redditmemes.getSomeMemes(sub[choice], 7)
			filenames += redditmemes.getSomeMemes(sub[choice+1],7)
			filenames += redditmemes.getSomeMemes(sub[choice+2],7)
			
			if choice + 3 >= 5:
				choice = -3			
			
			#write value of next subreddit back to file	
			choice_s = repr(choice+3)
			with open('subFile.txt','w') as subredditChoice:
				subredditChoice.write(choice_s)
			
			id = list()
			for i,x in enumerate(filenames):
				#parsing filename
				extension = x.split(".")[-1]
				subreddit = x.split("_")[-6]
				if subreddit == "irl":
					subreddit = x.split("_")[-7] + "_irl"
					source = x.split("_")[-8]
				else:
					source = x.split("_")[-7]	
				imgHost = x.split("_")[-2]
				#id.insert(i, x.split("_")[-1])
				id = x.split("_")[-1]
				
				#concatenate to form link to image
			#list.sort(id)
			#for x in id:
				link = "http://i.imgur.com/" + id #str(id[i])	
				#print("link: ", link)
				#Populate object fields
				popularity = 25
				tagsList = subreddit
				
				#create local object
				if i != 0:
					newMeme.append(database.Meme(link,tagsList,popularity))
				else:
					newMeme.append(database.Meme(link,tagsList,0))
				#save to database
			
			m=1
			n = 2
			count = 0
			while n < 6:
				database.storeMeme(newMeme[m])
				m += 4
				if m > len(newMeme)-1:
					m = n
					n += 1
				count += 1
				
			return newMeme[1].imgLink

		else:
			#If database meme is accepted
			newMeme[0].popularity = 0
			database.storeMeme(newMeme[0])
		

	#return meme link to bot
	return newMeme[0].imgLink
	
parseUserArguments(1)
