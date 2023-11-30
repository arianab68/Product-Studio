# sentiment_model.py
from transformers import pipeline 
import data
import tweet_processor

def load_model():
    """Load the pre-trained sentiment analysis model."""
    # Pre-trained model
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    # Load the sentiment analysis pipeline with the  model
    sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
    return sentiment_analyzer

# Predicting the sentiment of preprocessed tweets
model = load_model()
sentiment_predictions = model.predict(tweet_processor.preprocessed_tweets)
sentiment_predictions[:5]