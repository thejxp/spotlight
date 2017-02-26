import tweepy

import nltk

import time
import datetime

#BASELINE
#from import_from import *
from data import *


class Spotlight(object):
    
    auth = 0 # stub
    
    def __init__(self):
        #ACCESS_TOKEN = '1265991884-ZTn3kJtYdOqxEKrCmQh24mVU1Ri0MHYpMRTVrf2'
        ACCESS_TOKEN = '1265991884-SFsWE1moDMSkqzBxoQDpzhlxz4gj41gHbbebbqR'
        
        #ACCESS_SECRET = 'jBq4pAImH27NHKYCSvtmn49SCxgrQlzQG5uZuVenGZCZR'
        ACCESS_SECRET = 'bTP6cEyD9hiXXs0UnPkBIaFMaqV1V3EiwlKXKf3qff08x'
        
        #CONSUMER_KEY = 'EWgmuSU6Ar7lpO1ocjsLoN3kk'
        CONSUMER_KEY = '8XVEfSAM21dPPLrTVq4rMF4vp'
        
        #CONSUMER_SECRET = 'KEKHBy3IkrR6jYMlrhwS8jBECO0Si3zQmwRFqAFwhhI2A8oZ69'
        CONSUMER_SECRET = 'KN3ch1hdxJmgAYiul1AjPEcdi35etPGV4cfjw4X1yl0xibXisB'
        
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.manage_data()
        
    def manage_data(self):
        """Re-initializes ID_array, rated_tweets, and start_index based on
        imported values"""

        self.ID_array = ID_array
        self.rated_tweets = rated_tweets
        self.start_index = START_INDEX
    
    def increase_start_index(self):
        """Increases start_index by 1; is called by analyze_tweets_manual"""
        self.start_index += 1
    
    def add_rand_tweets(self, num, array):
        """Adds num (an integer) tweets to the array specified
        array should be an array that stores IDs of tweets based off of
        current implementation
        
        *** Random tweets ***
        """
        
        for i in range(num):
            tweets = self.api.search(q="lang:%s" % "en")
            for tweet in tweets:
                if tweet.id not in array:
                    array.append(tweet.id)
                
    def add_tweets(self, num, array):
        """Adds num (an integer) tweets to the array specified from a specific
        user. Uses userID to go through certain tweets"""
        
        for i in range(num):
            search_query = "from%3ACmdr_Hadfield%20%23nasa&result_type=popular"
            #tweets = self.api.search(q="%40realdonaldtrump&src=typd")
            tweets = self.api.search(q="lang:%s" % "en")
            for tweet in tweets:
                if tweet.id not in array:
                    array.append(tweet.id)
                
    def tweet_to_array(self, text):
        """Input: string of <140 characters representing a tweet
        Returns: array representing keywords in tweet"""
        
        tokens = nltk.word_tokenize(text)
        result = []
        for words in (tokens):
            if (len(words) > 2) and "#" not in words and "@" not in words and ".com" not in words:
                result.append(words)
        return result
        
            
    def analyze_tweets_manual(self, ID_array, full_array, start):
        """Given an array ID_array containing only IDs of tweets, analyze all tweets in
        said array and add them to full_array along with tokenized tweet text and mood
        association.
        
        full_array is the large ass array
        
        Each element of full_array should be in the following format:
        [ID, text, rating] where ID is an int, text is an array, rating is a string
        
        """
        
        for i in range(start, len(ID_array)):
            ID = ID_array[i]
            try:
                text = self.api.get_status(ID).text
            except:
                break
            
            print ("\n\n\n")
            print (text)
            
            rating = raw_input("Rate this tweet: (j: positive, k: neutral, l: negative, f: quit)  \n\n " )
            if (rating == "j"):
                rating = "pos"
            elif (rating == "k" ):
                rating = "neu"
            elif (rating == "l"):
                rating = "neg"
            else:
                
                break
            
            self.increase_start_index()
            text = self.tweet_to_array(text)
            
            rated_tweets.append([ID, text, rating])
        
    
    def write_data(self, file_name, message="No name given"):
        """ Writes data to file (appends; doesn't delete or override)
        
        Optional parameter: message defaults to "No name given"
        """
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        with open(file_name, "a") as myfile:
            myfile.write("\n\n\n######################### UPDATED ##############################")
            myfile.write(" #   " + message)
            myfile.write(" #   " + timestamp)
            
            myfile.write("\n\nID_array = ")
            myfile.write(`self.ID_array`)
            
            myfile.write("\n\nrated_tweets = ")
            myfile.write(`self.rated_tweets`)
            
            myfile.write("\n\nSTART_INDEX = ")
            myfile.write(`self.start_index`)
                        
        
        
    

