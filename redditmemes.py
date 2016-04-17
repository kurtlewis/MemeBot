# A script to get memes from Reddit

import praw, re, requests, os, glob, sys
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# A function to download the image file once the url has been determined
def downloadImage(imageUrl, localFileName):

	#Load the image file
	response = requests.get(imageUrl)
	
	#Status code 200 stands for success
	if response.status_code is 200:
	
		print('Downloading %s...' % (localFileName))
		
		#Create file with file name localFileName, 'wb' stands for write-binary
		# fo stands for file out, with statement handles exception catching for us
		with open(localFileName, 'wb') as fo:
		
			#Count how many times chunks of 4096 bytes are written
			count = 0
			
			#Chunk is a section of data from the image
			for chunk in response.iter_content(4096):
				fo.write(chunk)
				count += 1
				
			#If the image is very small (e.g. a weird icon from imgur or the 404 image)
			if count is 1:
				
				#Delete the file. It is useless to us. Return 1 for failure
				os.remove(localFileName)
				return 1
				print('File %s doesn\'t exist. Removing...' % (localFileName))
	return 0

#------------------------------------------------------------------------------------------------------		
#------------------------------------------------------------------------------------------------------	

#Our function to get memes from reddit! Great stuff.
def getSomeMemes(subredditName, submissionCount):

	#This is reddit api stuff. We need a unique user agent name. This is a reddit rule.
	#I assume nobody else is using MakeMemesDankAgain
	#PRAW handles following the rest of the rules for us, like frequency of requests.
	application = praw.Reddit(user_agent='MakeMemesDankAgain')
	
	#Specify the subreddit we'll be looking at.
	subreddit = application.get_subreddit(subredditName)
	
	#Define the regex search we'll be using to find Imgur urls.
	#This isn't used for a while, but we're getting it out of the way in the beginning.
	imgurUrlPattern = re.compile(r'(http://i.imgur.com/(.*))(\?.*)?')
	
	#Get a list of submissionCount subreddit submission objects from the subreddit.
	#Right now, we're looking at the 'hot' page, which is recently posted, popular submissions.
	subredditSubmissions = subreddit.get_hot(limit=submissionCount)
	
	#Initialize our list of file names we'll be sending to the control script.
	fileNameList = []
	
	#Look through all the submissions in our list.
	for submission in subredditSubmissions:
		
		#If the submission isn't on imgur, we are going to skip it.
		if "imgur.com/" not in submission.url:
			continue
		
		#This code allows us to skip submissions that we've downloaded content from already.
		#The file name format is reddit_[subredditName]_[submissionid]_[other stuff we'll get to later]
		#The submission is used like this: http://reddit.com/r/[subredditName]/[submissionid]
		if len(glob.glob('reddit_%s_%s_*' % (subredditName, submission.id))) > 0:
			print('Submission %s already downloaded. Skipping...' % (submission.id))
			continue
#------------------------------------------------------------------------------------------------------		
		#Album submission. We can eventually implement this, but it's not worth the effort now.
		#Album submissions are uncommon in the subreddits we'll be using most for this bot.
		if 'http://imgur.com/a/' in submission.url:
			# Album submission, we can't handle this right now
			continue
			"""
			albumName = submission.url[len('http://imgur.com/a/'):]
			htmlSourceCode = requests.get(submission.url).text
			soup = BeautifulSoup(htmlSourceCode, 'html.parser')
			foundImages = soup.select('.album-view-image-link a')
			for foundImage in foundImages:
				imageUrl = foundImage['href']
				if '?' in imageUrl:
					imageFile = imageUrl[imageUrl.rfind('/') + 1:imageUrl.rfind('?')]
				else:
					imageFile = imageUrl[imageUrl.rfind('/') + 1:]
				localFileName = 'reddit_%s_%s_album_%s_imgur_%s' % (subredditName, submission.id. albumId, imageFile)
				downloadImage('http:' + foundImage['href'], localFileName)
				"""
#------------------------------------------------------------------------------------------------------		
		#Direct link to image. This is the easiest one.
		elif 'http://i.imgur.com/' in submission.url:
			
			#Now we finally get to use the regex search we defined earlier.
			fileName = imgurUrlPattern.search(submission.url)
			
			#This is the part of the fileName object that we need to keep.
			imgurFileName = fileName.group(2)
			
			#For some reason, there is sometimes a question mark at the end of the fileName. We don't want it.
			#The link will work the same without it.
			if '?' in imgurFileName:
				imgurFileName = imgurFileName[:imgurFileName.find('?')]
				
			#Here we define our local file name that the image will be saved to the local directory under.
			#Format: reddit_subreddit_submissionid_album_albumid_sourcewebsite_sourcewebsitesubmissionid
			#Format simplified to what we're doing here: reddit_subreddit_submissionid_album_noalbum_imgur_imgurFileName
			localFileName = 'reddit_%s_%s_album_None_imgur_%s' % (subredditName, submission.id, imgurFileName)
			
			#Call the download function. If it returns 1, we had a failure.
			#If it returns zero, we add the file name to a list we will send to the control program.
			if downloadImage(submission.url, localFileName) is 1:
				continue
			else:
				print('Download successful.')
				fileNameList.append(localFileName)
#------------------------------------------------------------------------------------------------------		
		#If we don't have a direct link to the image, but we have a link to a page with only one image.
		#This page also contains comments, related images section, share buttons, etc.
		elif 'http://imgur.com/' in submission.url and ('.jpg' or '.png' or '.gif') not in submission.url:
			
			#Get the html code for this page. We will parse it to find the imgur filename.
			htmlSourceCode = requests.get(submission.url).text
			
			#Using beautifulsoup to make our file parsing easier
			soup = BeautifulSoup(htmlSourceCode, 'html.parser')
			
			#This is the pattern we are looking for in the source to find the direct link to the image
			imageUrl = soup.select('link')[10]['href']
			
			#If we don't have http:// in the link we found, we add it in (common issue).
			if imageUrl.startswith('//'):
				imageUrl = 'http:' + imageUrl
			
			#Same issue with question marks as above. We will remove them.
			#Then, parse the file to get the imgur unique image id, like before.
			if '?' in imageUrl:
				imageFile = imageUrl[imageUrl.rfind('/') + 1:imageUrl.rfind('?')]
			else:
				imageFile = imageUrl[imageUrl.rfind('/') + 1:]
				
			#Set our local file name. Same format as earlier.
			localFileName = 'reddit_%s_%s_album_None_imgur_%s' % (subredditName, submission.id, imageFile)
			
			#Call the download function. Again, return 1 means failure.
			if downloadImage(imageUrl, localFileName) is 1:
				continue
			else:
				print('Download successful.')
				fileNameList.append(localFileName)
#------------------------------------------------------------------------------------------------------
	#Finally, return the file name list to the control program.
	return fileNameList

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------