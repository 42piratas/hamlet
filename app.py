# app.py
import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import random
import json

app = Flask(__name__, static_folder='static')

# Set up custom NLTK data directory
current_dir = os.path.dirname(os.path.abspath(__file__))
nltk_data_dir = os.path.join(current_dir, 'data')
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Function to download NLTK data to custom directory
def download_nltk_data(package):
    nltk.download(package, download_dir=nltk_data_dir, quiet=True)

# Download required NLTK data
download_nltk_data('punkt')
download_nltk_data('stopwords')
download_nltk_data('wordnet')
download_nltk_data('averaged_perceptron_tagger')
download_nltk_data('punkt_tab')

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

@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/img', filename)

if __name__ == '__main__':
    app.run(debug=True)
