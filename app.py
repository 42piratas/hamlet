import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import random
import json

app = Flask(__name__)

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Load Shakespeare quotes
with open('shakespeare.json', 'r') as f:
    quotes = json.load(f)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

def get_response(user_input):
    tokens = preprocess(user_input)
    user_sentiment = get_sentiment(user_input)

    relevant_quotes = []
    for quote in quotes:
        quote_tokens = preprocess(quote['text'])
        quote_sentiment = get_sentiment(quote['text'])
        if any(token in quote_tokens for token in tokens):
            sentiment_diff = abs(user_sentiment - quote_sentiment)
            relevant_quotes.append((quote, sentiment_diff))

    if relevant_quotes:
        relevant_quotes.sort(key=lambda x: x[1])
        chosen_quote = random.choice(relevant_quotes[:3])[0]
        return chosen_quote['text'], chosen_quote['play']
    else:
        sentiment_similar_quotes = sorted(quotes, key=lambda x: abs(user_sentiment - get_sentiment(x['text'])))
        chosen_quote = random.choice(sentiment_similar_quotes[:3])
        return chosen_quote['text'], chosen_quote['play']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat():
    user_message = request.form['message']
    quote, source = get_response(user_message)
    return jsonify({'quote': quote, 'source': source})

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
