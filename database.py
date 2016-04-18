#This script will hold functions to open, update and close the list storing the memes

#The database will serve as a repository for memes, it will store the images with tags and a popularity ranking
import json
import os
import jsonpickle


class Meme:
	def __init__(self,imgLink,tagsList,popularity=1):
		self.imgLink = imgLink
		self.tagsList = tagsList
		self.popularity = popularity
	
	
	#Merges the given meme with the meme object
	def mergeMeme(self,memeObj):
		#Add tagslists together
		self.tagsList = memeObj.tagsList
	
		#Add popularity together
		self.popularity = memeObj.popularity
		
		
	#Returns the number of tags in the intersection of the meme's tags list with the given tagsList
	def numTagMatches(self,tagsList):
		matchCount = 0
		for tag in tagsList:
			if tag in self.tagsList:
				matchCount += 1
		
		return matchCount
		

#Prints a list of memes
def printMemes(memeDB):
	for meme in memeDB:
		print("link: {}, popularity: {}".format(meme.imgLink,meme.popularity))
		
#This function will return the list of meme objects
def openMemeDB():
	if not os.path.exists("MemeDB.json"):
		memeDbFile = open("MemeDB.json","w")
		memeDbFile.write("[]")
		memeDbFile.close()
	
	memeDbFile = open("MemeDB.json","r")
	
	memeDbStr = memeDbFile.read()
	
	memesList = jsonpickle.decode(memeDbStr)
	
	memeDbFile.close()
	
	return memesList
	
	
	
#This function will take a list of meme objects and save it to MemeDB.json
def closeMemeDB(memesList):
	memeDbFile = open("MemeDB.json","w")
	
	jsonStr = jsonpickle.encode(memesList)
	
	memeDbFile.write(jsonStr)
	
	memeDbFile.close()
	

#########################  Below are functions intended to be called externally by other scripts (above are functions used by this script)	
	
#This function will take a meme object put it into the list appropriately (may need to merge with existing meme)
def storeMeme(memeObj):
	memeDB = openMemeDB()
	
	#Search memeDB for meme's matching given object
	for currMeme in memeDB:
		if currMeme.imgLink == memeObj.imgLink:
			
			currMeme.mergeMeme(memeObj)
			#If memes match, merge them then save the list then save and close memeDB
			closeMemeDB(memeDB)
			return
		
	#If meme does not match any in memeDB, add it then save and close memeDB
	memeDB.append(memeObj)
	closeMemeDB(memeDB)
	
	
#This function will return a meme object that best suits the given tagsList
def getMeme(tagsList):
	memeDB = openMemeDB()
		
	if len(tagsList) > 0:
		matchingMemes = list()
	
		#Search memeDB for meme's matching tagslist
		for currMeme in memeDB:
			#If any tag in currMeme.tagsList is contained in the tagsList argument, add it to the matches list
			if any(currTag in tagsList for currTag in currMeme.tagsList):
				matchingMemes.append(currMeme)
	else:
		matchingMemes = memeDB
	
	if len(matchingMemes) == 0:
		return None
	
	#Sort by tag relevance and popularity
	for index,currMeme in enumerate(matchingMemes):
		i = index
		#While the current meme is not the first one (there is one above it) and has more matches than the one above
		while i > 0 and matchingMemes[i].popularity > matchingMemes[i-1].popularity:
			tmp = matchingMemes[i]
			matchingMemes[i] = matchingMemes[i-1]
			matchingMemes[i-1] = tmp
			i-=1
			
	
	#Update popularity
	for meme in memeDB:
		meme.popularity += 1
		storeMeme(meme)
	
	#Return the best meme		
	return matchingMemes[0]
	
	#This function will clear the database
def flushDatabase():

	#Open the json and overwrite with an empty json
	memeDB = open("MemeDB.json","w")
	memeDB.write("[]")
	

	
	
	
	
	
	
	
	
	
	
	
