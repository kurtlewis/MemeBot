#This script will hold functions that will manage the logic and arithmatic for the server
#The database will serve as a repository for memes, it will store the images with tags and a popularity ranking


"""
Meme Object:
	-ImageLink (str)
	-Tags (list Tags)
	-Popularity (int)

"""
Class Meme:
	def __init__(self,imgLink,tagList,popularity=0):
		self.imgLink = imgLink
		self.tagList = tagList
		self.popularity = popularity
		

"""
Connection > Database:
	storeMeme(imgLink,tagsList,popularity) - Database will create a new meme object and store it
	getMeme(tagsList) - Database will return the most popular meme that best matches the tags (will harm popularity once used)
	
"""
