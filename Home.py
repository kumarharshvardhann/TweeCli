import re
import sys
import tweepy

consumer_key = "QtKxntbxxkFbrPmG8Aggn0enQ"
consumer_secret = "aU3fVGgpjYt7CWgnvA6cxLCszF8z8XTvZVK6mdItiLpputoWim"
access_token = "976482866396884992-8h3I2DFDcamJnGzs3vVcN0fxqMZ9tKT"
access_token_secret = "JZO17YezFDuAOIiqwVIo8sTh39k9k5d9OPJUN3lfXYFAQ"

auth = tweepy.OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token ,access_token_secret)

api = tweepy.API(auth)

mytweets = api.user_timeline()


for status in mytweets:
	tweet_string = status.text
	if status.retweeted == True:
		print('=========\nRetweeted:  ' + tweet_string + '\n=========')
	else:
		print('=========\nTweeted:  ' + tweet_string + '\n=========')
		
	