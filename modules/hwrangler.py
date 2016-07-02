'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import hg
import string

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


ps = PorterStemmer()
stop_words = set(stopwords.words("english"))


def wrangle():
    # Lower
    content_lower = hg.content
    # Remove the punctuation using the character deletion step of translate
    content_no_punctuation = content_lower.translate(string.punctuation)
    # Tokinize by words
    hg.content_by_word = word_tokenize(content_no_punctuation)
    # Remove stop words
    hg.content_no_stopwords = [w for w in hg.content_by_word if w not in stop_words]
    # Steam
    hg.content_stemmed = [ps.stem(w) for w in hg.content_no_stopwords]
