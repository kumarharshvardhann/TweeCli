import re
import sys
import tweepy

consumer_key = "Consumer key here"
consumer_secret = "Consumer secret here"
access_token = "Access token here"
access_token_secret = "Access token secret here"

auth = tweepy.OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token ,access_token_secret)

api = tweepy.API(auth)

mytweets = api.retweets_of_me()


for status in mytweets:
	tweet_string = status.text
	print('=========\n' + tweet_string + '\n=========')
	
		
	