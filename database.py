#This script will hold functions that will manage the logic and arithmatic for the server
#The database will serve as a repository for memes, it will store the images with tags and a popularity ranking


"""
Meme Object:
	-Image
	-Tags
	-Popularity

"""

"""
Connection > Database:
	storeMeme(img,tagsList,popularity) - Database will create a new meme object and store it
	getMeme(tagsList) - Database will return the most popular meme that best matches the tags (will harm popularity once used)
	
"""
