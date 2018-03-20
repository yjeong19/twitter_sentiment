
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
        polarity_value = sentiment_value.sentiment.polarity
        if polarity_value > 0:
            polarity.append('positive')
        else:
            polarity.append('negative')
        # polarity.append(sentiment_value.sentiment.polarity)
        subjectivity.append(sentiment_value.sentiment.subjectivity)
        tweet.append(status.text.encode('utf-8'))

    return polarity, subjectivity, tweet

polarity, subjectivity, tweet = tweets(data)

def combined (polarity, subjectivity, tweet):
    sentinmental_analysis = []
    for x in range(len(tweet)):
        if polarity[x] == 'positive':
            positive = polarity[x], 'tweet:', tweet[x], 'subjectivity: ', subjectivity[x]
            sentinmental_analysis.append(positive)
        else:
            negative = polarity[x], 'tweet:', tweet[x], 'subjectivity: ', subjectivity[x]
            sentinmental_analysis.append(negative)
    return sentinmental_analysis

import csv
with open ('Myfile.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=' ')
    wr.writerow(combined(polarity, subjectivity, tweet))
    # wr.writerow(polarity)
    # wr.writerow(subjectivity)
