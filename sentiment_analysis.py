# TWEET SENTIMENT ANALYSIS 

import nltk

import time
import datetime

#BASELINE
#from import_from import *
from data import *


class MachineSpotlight(object): 

    ########################################################################################################################
    #  DATA STORAGE AND MANAGEMENT                                                                                         #
    ########################################################################################################################

    def manage_data(self):
        """Re-initializes ID_array and rated_tweets based on
        imported values"""
        self.rated_tweets = rated_tweets

        self.positive_array = []
        self.negative_array = []
        self.neutral_array = []

        self.positive_dictionary = positive_dict
        self.negative_dictionary = negative_dict
        self.neutral_dictionary = neutral_dict
        self.start_index = start_tweets
        
    
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
            
            myfile.write("\n\nstart_tweets = ")
            myfile.write(`self.start_index`)
            
            myfile.write("\n\npositive_dict = ")
            myfile.write(`self.positive_dictionary`)
           
            myfile.write("\n\nnegative_dict = ")
            myfile.write(`self.negative_dictionary`)
            
            myfile.write("\n\nneutral_dict = ")
            myfile.write(`self.neutral_dictionary`)
            
                   
                        
    def build_classifier(self):
                
        self.make_three_arrays()
        
        
        self.get_frequency_in_each(self.positive_array, self.positive_dictionary)
        self.get_frequency_in_each(self.negative_array, self.negative_dictionary)
        self.get_frequency_in_each(self.neutral_array, self.neutral_dictionary)
        
    
   
    def update_classifier(self, new_tweet):
        """Input: String representing a tweet
        
        Returns: a string representation of the score
        """
            
        tweet_score = self.get_score(new_tweet)
        self.update_dictionaries(new_tweet, tweet_score)    
        return tweet_score
    
    
    def make_three_arrays(self):
        """
        Output: Three arrays are created with a list of meaningful words
        """
                
        for i in range(self.start_index, len(self.rated_tweets)):
            words = self.rated_tweets[i][1]
            rating = self.rated_tweets[i][2]
            if rating == 'pos':
                self.positive_array.extend(words)
            elif rating == 'neu':
                self.neutral_array.extend(words)
            elif rating == 'neg':
                self.negative_array.extend(words)
            
            
            self.start_index += 1
    
    def get_frequency_in_each(self, some_array, dictionary):
        """Input: a wordlist, one of the three arrays from above..., a dictionary to write to
        
        Output: NONE ---\\\ignore ---- a dictionarys with format key: value being "word": # of occurences
        """

        
        for key in some_array:
            if key not in dictionary:
                dictionary[key] = 1
            else:
                dictionary[key] += 1

    
    def get_score(self, new_tweet):
        
        percentage = ''
        score = 0
        ## CAST new_tweet TO UNICODE FORM
        
        tokens = nltk.word_tokenize(new_tweet)
        for key in tokens:
            if key in self.positive_dictionary:
                pos = self.positive_dictionary[key]
            else:
                pos = 0
            if key in self.negative_dictionary:
                neg = self.negative_dictionary[key]
            else:
                neg = 0
            if key in self.neutral_dictionary:
                neu = self.neutral_dictionary[key]
            else:
                neu = 0
            
            try:
                score += float((pos-neg)/(pos+neg+neu))
            except ZeroDivisionError:
                score = 0.0
        try:
            score = score/(len(tokens)*2)
        except:
            score = 0.0
        
        if score > 0:
            percentage = 50 - int((score * 100) + 0.5) / 100.0
            return (str(percentage) + '% Negative (Unlikely)')
        
        elif score == 0:
            percentage = 50 - int((score * 100) + 0.5) / 100.0
            
            return (str(percentage) + '% Negative (Medium Likelihood)')
    
        else:
            percentage = 50 - int((abs(score) * 100) + 0.5) / 100.0
            
            return (str(percentage) + '% Negative (Likely)')    
        
    def update_dictionaries(self, new_tweet, score):
        """Input: tweet 
        
        """
                
        tokens = nltk.word_tokenize(new_tweet)
        
        for key in tokens:
            if score > 0:
                if (key) not in self.positive_dictionary:
                    self.positive_dictionary[key] = 1
                else:
                    self.positive_dictionary[key] += 1
            elif score == 0:
                if (key) not in self.neutral_dictionary:
                    self.neutral_dictionary[key] = 1
                else:
                    self.neutral_dictionary[key] += 1
            else:
                if (key) not in self.negative_dictionary:
                    self.negative_dictionary[key] = 1
                else:
                    self.negative_dictionary[key] += 1

    
        
    
    
    











