#This script will hold functions to open, update and close the list storing the memes
#The database will serve as a repository for memes, it will store the images with tags and a popularity ranking
import json

"""
Meme Object:
	-ImageLink (str)
	-Tags (list Tags)
	-Popularity (int)

"""
Class Meme:
	def __init__(self,imgLink,imgPath,tagsList,popularity=0):
		self.imgLink = imgLink
		self.imgPath = imgPath
		self.tagsList = tagsList
		self.popularity = popularity
	
	
	#Merges the given meme with the meme object
	def mergeMeme(memeObj)
		#Add tagslists together
		self.tagsList = self.tagsList + memeObj.tagsList
	
		#Add popularity together
		self.popularity += memeObj.popularity
		
		
	#Returns the number of tags in the intersection of the meme's tags list with the given tagsList
	def numTagMatches(tagsList)
		matchCount = 0
		for tag in tagsList
			if tag in self.tagsList
				matchCount++
		
		return matchCount

"""
Connection > Database:
	storeMeme(imgLink,tagsList,popularity) - Database will create a new meme object and store it
	getMeme(tagsList) - Database will return the most popular meme that best matches the tags (will harm popularity once used)
	
"""


#This function will return the list of meme objects
def openMemeDB():
	memeDbFile = open("MemeDB.json","r")
	memeDbStr = memeDbFile.readlines()
	
	memesList = json.load(memeDbStr)
	
	memeDbFile.close()
	
	return memesList
	
	
	
#This function will take a list of meme objects and save it to MemeDB.json
def closeMemeDB(memesList):
	memeDbFile = open("MemeDB.json","w")
	memeDbFile.writelines(memesList.dumps(memesList))
	memeDbFile.close()
	

#This function will take a meme object put it into the list appropriately (may need to merge with existing meme)
def storeMeme(memeObj)
	memeDB = openMemeDB()
	
	#Search memeDB for meme's matching given object
	for currMeme in memeDB
		if currMeme.imgLink == memeObj.imgLink
			currMeme.mergeMeme(currMeme,memeObj)
			#If memes match, merge them then save the list then save and close memeDB
			closeMemeDB(memeDB)
			return
		
	#If meme does not match any in memeDB, add it then save and close memeDB
	memeDB.append(memeObj)
	closeMemeDB(memeDB)
	
	
#This function will return a meme object that best suits the given tagsList
def getMeme(tagsList)
	memeDB = openMemeDB()
	
	matchingMemes = list()
	
	#Search memeDB for meme's matching tagslist
	for currMeme in memeDB
		#If any tag in currMeme.tagsList is contained in the tagsList argument, add it to the matches list
		if any(currTag in tagsList for currTag in currMeme.tagsList)
			matchingMemes.append(currMeme)
	
	
	#Of matchine memes, get most popular and return:
	#First sort by tag relevance
	for index,currMeme in enumerate(matchingMemes)
		i = index
		#While the current meme is not the first one (there is one above it) and has more matches than the one above
		while i > 0 and matchingMemes[i].numTagMatches > matchingMemes[i-1].numTagMatches
			matchingMemes[i], matchingMemes[i-1] = matchingMemes[i-1], matchingMemes[i]
			i--
			
	#Then sort by popularity
	for index,currMeme in enumerate(matchingMemes)
		i = index
		#While the current meme is not the first one (there is one above it) and has a greater popularity than the one above
		while i > 0 and matchingMemes[i].popularity > matchingMemes[i-1].popularity
			matchingMemes[i], matchingMemes[i-1] = matchingMemes[i-1], matchingMeme[i]
			i--
	
	#Return the best meme
	return matchingMemes[0]
	
	
	
	
	
	
	
	
	
	
	
	
	
	
