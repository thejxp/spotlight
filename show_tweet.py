import tweepy

ACCESS_TOKEN = '1265991884-ZTn3kJtYdOqxEKrCmQh24mVU1Ri0MHYpMRTVrf2'
ACCESS_SECRET = 'jBq4pAImH27NHKYCSvtmn49SCxgrQlzQG5uZuVenGZCZR'
CONSUMER_KEY = 'EWgmuSU6Ar7lpO1ocjsLoN3kk'
CONSUMER_SECRET = 'KEKHBy3IkrR6jYMlrhwS8jBECO0Si3zQmwRFqAFwhhI2A8oZ69'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
"""

user = api.get_user('thejxp')

tweet = api.get_status('835584598868254720')

print tweet.text