import os
import math
import json
import random
import string
from collections import Counter

import nltk
nltk.data.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))

from flask import Flask, render_template, request, jsonify, send_from_directory
from textblob import TextBlob
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet

app = Flask(__name__)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shakespeare.json'), 'r') as f:
    quotes = json.load(f)

STOPWORDS = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",
    'thee', 'thou', 'thy', 'thine', 'ye', 'art', 'doth', 'hath', 'tis'])

stemmer = PorterStemmer()

def tokenize(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).split()

def normalize(text):
    return [stemmer.stem(t) for t in tokenize(text) if t not in STOPWORDS and len(t) > 1]

def expand_synonyms(stems, raw_tokens):
    out = set(stems)
    for raw in raw_tokens:
        if raw in STOPWORDS or len(raw) <= 2:
            continue
        for syn in wordnet.synsets(raw)[:2]:
            for lemma in syn.lemmas()[:3]:
                w = lemma.name().lower().replace('_', ' ')
                if ' ' in w:
                    continue
                out.add(stemmer.stem(w))
    return out

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

def searchable_text(q):
    parts = [q['text']]
    if q.get('work'):
        parts.append(q['work'])
    if q.get('type') == 'sonnet' and q.get('number') is not None:
        parts.append(f"sonnet {q['number']}")
    return ' '.join(parts)

# --- precompute corpus index at startup ---
N = len(quotes)
_doc_tfs = []
_df = Counter()
for q in quotes:
    terms = normalize(searchable_text(q))
    tf = Counter(terms)
    _doc_tfs.append(tf)
    for t in tf:
        _df[t] += 1

IDF = {t: math.log(N / c) + 1 for t, c in _df.items()}

DOC_VECS = []
for tf in _doc_tfs:
    v = {t: f * IDF[t] for t, f in tf.items()}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
    DOC_VECS.append((v, norm))

DOC_SENTIMENT = [get_sentiment(q['text']) for q in quotes]

ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}

def format_source(quote):
    t = quote.get('type', 'play')
    lines = quote.get('lines')
    if t == 'sonnet':
        n = quote.get('number')
        base = f'Sonnet {n}'
        return f'{base} · {lines}' if lines else base
    if t == 'poem':
        work = quote.get('work', '')
        return f'{work} · {lines}' if lines else work
    work = quote.get('work', '')
    act, scene = quote.get('act'), quote.get('scene')
    if act and scene:
        cite = f'{ROMAN.get(act, str(act))}.{ROMAN.get(scene, str(scene)).lower()}'
        return f'{work} · {cite} · {lines}' if lines else f'{work} · {cite}'
    if lines:
        return f'{work} · {lines}'
    return work

SYNONYM_WEIGHT = 0.5
SENTIMENT_BLEND = 0.1
TOP_K = 5

def get_response(user_input):
    raw = tokenize(user_input)
    stems = [stemmer.stem(t) for t in raw if t not in STOPWORDS and len(t) > 1]
    user_sent = get_sentiment(user_input)

    if not stems:
        idx = random.randrange(N)
        return quotes[idx]['text'], format_source(quotes[idx])

    expanded = expand_synonyms(stems, raw)
    q_tf = Counter()
    for s in stems:
        q_tf[s] += 1.0
    for s in expanded - set(stems):
        q_tf[s] += SYNONYM_WEIGHT

    q_vec = {t: f * IDF[t] for t, f in q_tf.items() if t in IDF}
    q_norm = math.sqrt(sum(x * x for x in q_vec.values())) or 1.0

    scored = []
    for i, (d_vec, d_norm) in enumerate(DOC_VECS):
        common = q_vec.keys() & d_vec.keys()
        if not common:
            continue
        dot = sum(q_vec[t] * d_vec[t] for t in common)
        sim = dot / (q_norm * d_norm)
        if sim <= 0:
            continue
        sent_diff = abs(user_sent - DOC_SENTIMENT[i])
        scored.append((i, sim - SENTIMENT_BLEND * sent_diff))

    if scored:
        scored.sort(key=lambda x: -x[1])
        chosen = quotes[random.choice(scored[:TOP_K])[0]]
    else:
        ranked = sorted(range(N), key=lambda i: abs(user_sent - DOC_SENTIMENT[i]))
        chosen = quotes[random.choice(ranked[:TOP_K])]

    return chosen['text'], format_source(chosen)

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
