import os

import tweepy


try:
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SCERET']
    access_token = os.environ['ACCESS_TOKEN']
    access_secret = os.environ['ACCESS_SECRET']
except KeyError:
    print('No keys setup.')
else:
    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    tweets = api.search(q='#python #django')

    # display results to screen
    for t in tweets:
        print(t.created_at, t.text, '\n')
