from spotlight_class import *
from sentiment_analysis import *


def generate_tweets(num):
    """Adds num IDs to ID_array and prints to console"""
    
    app.add_tweets(num, ID_array)


def rate_tweets():
    """Updates rated_tweets array and prints to console"""
    
    app.analyze_tweets_manual(ID_array, rated_tweets, app.start_index)

app = Spotlight()

generate_tweets(50)
rate_tweets()

app.write_data("data.py", "Julie")
