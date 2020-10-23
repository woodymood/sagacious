from os import environ
import tweepy 
from datetime import datetime, timedelta
import time 
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ["CONSUMER_SECRET"]
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)


INTERVAL = int(environ['INTERVAL'])
DEBUG = environ['DEBUG'] == '1'

def main():
    while True:
        print('hello')
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()