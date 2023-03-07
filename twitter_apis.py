import tweepy
import time
import random
import os

from .generate_messages import generate_funny_reply

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_SECRET_KEY')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

FILE_NAME = 'last.txt'

api = tweepy.API(auth)

# This function will open the text file and return the ID of
# the latest tweet the bot has successfully replied to
# TODO: User sqlite database to store this info
def read_last_seen(FILE_NAME):
    with open(FILE_NAME, 'r') as file_read:
        last_seen_id = int(file_read.read().strip())
    return last_seen_id

# Overwrite the previous Tweet ID with latest
def store_last_seen(FILE_NAME, last_seen_id):
    with open(FILE_NAME, 'w') file_write:
      file_write.write(str(last_seen_id))
    return

# Pick appreciation randomly
def funny_reply(tweet_text):
    return generate_funny_reply(tweet_text)

def reply():
    # The API will only send a response containing tweets with IDs that come after the ID
    # stored in the text file
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#FunnyReplyGPT' in tweet.full_text.lower() or '@FunnyReplyGPT' == tweet.full_text.lower().strip() or '.@FunnyReplyGPT' == tweet.full_text.lower().strip():
            print("Funny Reply GPT!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            api.update_with_media("@"+ tweet.user.screen_name + " " + funny_reply(), in_reply_to_status_id=tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

        elif '#FunnyReplyGPT' not in tweet.full_text.lower():
            print("Liked!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            store_last_seen(FILE_NAME, tweet.id)

        api.create_favorite(tweet.id) # Like the tweet with mentions


"""
The program needs to run continuously to fetch and reply to tweets. This loop
runs infinitely and executes the reply() functions checking for mentions and
has a timeout of 30 seconds between each poll so that rate limits imposed by
Twitter APIs are not tripped.
"""
while True:
    reply()
    time.sleep(30)
