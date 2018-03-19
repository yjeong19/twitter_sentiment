import tweepy
from textblob import textblob

consumer_key = '5uZChGSRmdSsUpphDhtCRTVDt'
consumer_secret = 'yYxTgTrfSsgC63TsRHQs6yzYJDxFF5LiRTXDNELys3jS8szlgE'
access_token = '930637758078619649-astLMh7gLWT7E9ufybHQMTON6Zo4Zo7'
access_token_secret = '2KHMaQq8oHWxcxQIC6RYi7H9AshICIQsF8L6WK2QoVAyM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


data = api.user_timeline(screen_name = 'realdonaldtrump')

def tweets(data):
    status = []
    for tweet in data:
        status.append(tweet.text)
    return status

print (tweets(data))
