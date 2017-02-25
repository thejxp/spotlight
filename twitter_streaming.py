# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import twitter

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1265991884-ZTn3kJtYdOqxEKrCmQh24mVU1Ri0MHYpMRTVrf2'
ACCESS_SECRET = 'jBq4pAImH27NHKYCSvtmn49SCxgrQlzQG5uZuVenGZCZR'
CONSUMER_KEY = 'EWgmuSU6Ar7lpO1ocjsLoN3kk'
CONSUMER_SECRET = 'KEKHBy3IkrR6jYMlrhwS8jBECO0Si3zQmwRFqAFwhhI2A8oZ69'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# ??? 
twitter = Twitter(auth=oauth)


# print(twitter.followers.ids(screen_name="thejxp"))

# PRINT REPRESENTATION OF A TWEET



# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 

tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break
    
