# tweet_processor.py
import re
import data

def clean_tweet(tweet):
    """Clean the tweet by removing URLs, special characters, and converting to lowercase."""
    tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs
    tweet = re.sub(r'[^A-Za-z0-9\s]', '', tweet)  # Remove special characters
    tweet = tweet.lower()  # Convert to lowercase
    return tweet.strip()

def get_tweets(tweets):
    """Return a list of preprocessed fake tweets."""
    return [clean_tweet(tweet) for tweet in tweets]

# Preprocess the fake tweets
preprocessed_tweets = get_tweets(data.fake_tweets)
preprocessed_tweets[:5]
