import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from textblob import TextBlob
import random
import json
import string

app = Flask(__name__)

# Load Shakespeare quotes
with open('shakespeare.json', 'r') as f:
    quotes = json.load(f)

# Simple tokenization function
def simple_tokenize(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).split()

# Simple stopwords list
STOPWORDS = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])

def preprocess(text):
    tokens = simple_tokenize(text)
    return [token for token in tokens if token not in STOPWORDS]

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
