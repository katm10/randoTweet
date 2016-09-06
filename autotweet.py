# pommunism auto-tweeter

import tweepy, time
import brainscrape
import random
import os
import pommunism

with open("access.txt") as f:
    secrets = f.readlines()

# get twitter auth secrets, being sure to remove the newline character
CONSUMER_KEY = secrets[0].rstrip('\n')
CONSUMER_SECRET = secrets[1].rstrip('\n')
ACCESS_TOKEN = secrets[2].rstrip('\n')
ACCESS_SECRET = secrets[3].rstrip('\n')

# auth is love, auth is life
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
imgdir = os.listdir("img/")

# obtain quotes using brainscrape.py, parse so that only <160 character tweets are made
def sendTweet():
    tweetbase = brainscrape.getQuotes()
    img = pommunism.get_pom()
    if len(str(tweetbase)) <= 140: # then cite by author
        api.update_with_media(img,tweetbase)
    else: # not enough space for author
        sendTweet()

# randomize images and status to create random tweets

sendTweet()


