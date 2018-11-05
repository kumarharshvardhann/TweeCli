import re
import sys
import tweepy

consumer_key = "consumer key here"
consumer_secret = "consumer secret here"
access_token = "access token here"
access_token_secret = "access token secret here"

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

