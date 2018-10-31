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

flag = 0
for status in mytweets:
	tweet_string = status.text
	word = sys.argv[1]
	if re.search(word, tweet_string, re.IGNORECASE):
		if status.retweeted == True:
			print('=========\nRetweeted:  ' + tweet_string + '\n=========')
		else:
			print('=========\nTweeted:  ' + tweet_string + '\n=========')
		flag = 1
	
if flag == 0:
	print('Sorry! No tweets found matching your search request!')

