import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Importing your custom modules
from sentiment_model import load_model as load_sentiment_model
from virality_model import train_model, predict_virality
import tweet_processor
import data
import sentiment_model
import virality_model

# Create a Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Assume we have functions to get data, process twgiteets, and predict sentiment and virality
# You'd need to adapt the below code to use your actual data and model functions

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Sentiment Analysis Dashboard"), className="mb-2"),
            dbc.Col(dcc.Dropdown(
                id='brand-dropdown',
                options=[
                    {'label': 'Pepsi', 'value': 'PEP'},
                    # Add other brands
                ],
                value='PEP'  # default value
            ), width=4),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='sentiment-timeline'), width=12),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='comment-sentiment-pie'), width=4),
            dbc.Col(html.Div(id='sentiment-score'), width=4),
            dbc.Col(html.Div(id='comment-statistics'), width=4),
            dbc.Col(html.Div(id='user-statistics'), width=4),
        ]),
    ])
])

@app.callback(
    [
        Output('sentiment-timeline', 'figure'),
        Output('comment-sentiment-pie', 'figure'),
        Output('sentiment-score', 'children'),
        Output('comment-statistics', 'children'),
        Output('user-statistics', 'children')
    ],
    [Input('brand-dropdown', 'value')]
)
def update_dashboard(brand_value):

    # Now you can call your model prediction functions
    sentiment_predictions = sentiment_model.sentiment_predictions
    virality_scores = virality_model.virality_scores

    sentiment_figure = create_sentiment_timeline(sentiment_predictions)
    pie_chart_figure = comment_sentiment_pie(sentiment_predictions)
    sentiment_score = calculate_overall_sentiment(sentiment_predictions)
    comment_stats = calculate_comment_statistics(sentiment_predictions)
    user_stats = calculate_user_statistics(virality_scores)


    # Convert dictionaries to formatted strings or Dash components for rendering
    formatted_comment_stats = ', '.join([f"{key}: {value}" for key, value in comment_stats.items()])
    formatted_user_stats = ', '.join([f"{key}: {value:.2f}" for key, value in user_stats.items()])

    return sentiment_figure, pie_chart_figure, f"Overall Sentiment Score: {sentiment_score}", formatted_comment_stats, formatted_user_stats

import plotly.graph_objs as go

# Helper function to create a pie chart for comment sentiment
def comment_sentiment_pie(sentiment_predictions):
    # Assume sentiment_predictions includes a 'label' that can be POSITIVE, NEGATIVE, or NEUTRAL
    labels = ['Positive', 'Neutral', 'Negative']
    values = [
        sum(1 for prediction in sentiment_predictions if prediction['label'] == 'POSITIVE'),
        sum(1 for prediction in sentiment_predictions if prediction['label'] == 'NEUTRAL'),
        sum(1 for prediction in sentiment_predictions if prediction['label'] == 'NEGATIVE')
    ]
    
    fig = px.pie(values=values, names=labels, title='Comment Sentiment')
    return fig

# Helper function to create a sentiment timeline figure without dates
def create_sentiment_timeline(sentiment_predictions):
    # Assuming that sentiment_predictions includes a sentiment score
    scores = [prediction['score'] if prediction['label'] == 'POSITIVE' else 1 - prediction['score']
              for prediction in sentiment_predictions]

    # Create the figure
    fig = go.Figure()
    fig.add_trace(go.Bar(y=scores, name='Sentiment Score'))
    fig.update_layout(title='Sentiment Scores', yaxis_title='Sentiment Score', xaxis_title='Data Points')
    return fig


# Helper function to check if a tweet contains the brand
def tweet_contains_brand(tweet, brand_value):
    return brand_value.lower() in tweet.lower()

# Helper function to calculate overall sentiment score
def calculate_overall_sentiment(sentiment_predictions):
    # Calculate the mean of the sentiment scores
    sentiment_scores = [prediction['score'] if prediction['label'] == 'POSITIVE' else 1 - prediction['score']
                        for prediction in sentiment_predictions]
    overall_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    return overall_sentiment

# Helper function to calculate comment statistics
def calculate_comment_statistics(sentiment_predictions):
    # Let's assume we count the number of positive, negative, and neutral comments
    positive_comments = sum(1 for prediction in sentiment_predictions if prediction['label'] == 'POSITIVE')
    negative_comments = sum(1 for prediction in sentiment_predictions if prediction['label'] == 'NEGATIVE')
    neutral_comments = sum(1 for prediction in sentiment_predictions if prediction['label'] == 'NEUTRAL')
    total_comments = len(sentiment_predictions)
    
    stats = {
        'total_comments': total_comments,
        'positive_comments': positive_comments,
        'negative_comments': negative_comments,
        'neutral_comments': neutral_comments
    }
    return stats

# Helper function to calculate user statistics
def calculate_user_statistics(virality_scores):
    # Let's assume we simply return the average virality score for now
    if virality_scores:
        average_virality = sum(virality_scores) / len(virality_scores)
    else:
        average_virality = 0
    user_stats = {'average_virality': average_virality}
    return user_stats

if __name__ == '__main__':
    app.run_server(debug=True)
