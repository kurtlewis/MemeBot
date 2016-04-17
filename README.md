# MemeBot
A bot for sending memes on request to users in different messaging apps. Created at Revolution UC 2016.

##Installation
Using your favorite linux hosting service, make sure the dependencies below are installed.
Your bot will recieve requests on a url of style "[Your domain name].com:[Open port]/GroupMe/"

Clone this repository into a directory of your choosing.

    $git clone https://github.com/lewisku/MemeBot.git


Go to http://dev.groupme.com and login using your groupme username.
Pick a group, name your bot, and provide a callback url to the url you specified above.
You can provide an image if you so choose.

On https://dev.groupme.com/bots you'll be able to see the bots you have created.
Add a new line to Bots/GroupMeBots.txt with the Bot's Group ID and Bot ID, formatted as:
    [GroupID], [Bot ID]

Start your server on a port you specified earlier:
    $python Bots/manage.py runserver 0.0.0.0:[PORT]

Your server will now interpret messages for every bot you specified in Bots/GroupMeBots.txt.

Great work!


## Current dependencies
### Python
#### Main Bot
* Requests
* jsonpickle
* django

#### Bot management script
* Groupy
* Pillow

### Meme collecting script
* praw
* beautifulsoup4
