
import tweepy
import configparser
from textblob import TextBlob

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['consumer_key']['key']
consumer_secret = config['consumer_secret']['key']
access_token = config['access_token']['key']
access_token_secret = config['access_token_secret']['key']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


data = api.user_timeline(screen_name = 'realdonaldtrump')

def tweets(data):
    polarity = []
    subjectivity = []
    tweet = []
    for status in data:
        sentiment_value = TextBlob(status.text)
        polarity.append(sentiment_value.sentiment.polarity)
        subjectivity.append(sentiment_value.sentiment.subjectivity)
        tweet.append(status.text.encode('utf-8'))
    return polarity, subjectivity, tweet

polarity, subjectivity, tweet = tweets(data)

import csv
with open ('sentiment.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',')
    # wr.writerow(sentiment)
    wr.writerow(tweet)
    wr.writerow(polarity)
    wr.writerow(subjectivity)
