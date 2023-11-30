# Creating a dataset of 100 fake tweets about Pepsi
import random

def create_fake_tweet():
    """Generates a fake tweet with random sentiment about Pepsi."""
    phrases = [
        "Loving the new Pepsi flavor!",
        "I prefer Coke over Pepsi any day.",
        "Pepsi is my go-to drink for parties.",
        "Not a big fan of Pepsi, tastes too sweet for me.",
        "Pepsi always refreshes me after a long day.",
        "Why choose Pepsi when you can have natural juice?",
        "Pepsi's new ad campaign is brilliant!",
        "Miss the old Pepsi taste, not a fan of the new one.",
        "Pepsi or Coke? Always Pepsi for me!",
        "Can't understand the hype around Pepsi."
    ]
    return random.choice(phrases)

# Generate 100 fake tweets
fake_tweets = [create_fake_tweet() for _ in range(100)]
fake_tweets[:5]  # Displaying the first 5 tweets for demonstration
