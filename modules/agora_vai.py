'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import os
import sys
import string

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

stop_words = set(stopwords.words("english"))

# Open the file
with open(os.path.join(os.path.dirname(sys.argv[0]), 'randomtexts.txt'), 'r') as opened_file:
    # Read the file
    content = opened_file.read()
    # Lower
    content_lower = content.lower()
    # Remove the punctuation using the character deletion step of translate
    content_no_punctuation = content_lower.translate(None, string.punctuation)
    # Tokinize by words
    content_by_word = word_tokenize(content_no_punctuation)
    # Remove stop words
    content_no_stopwords = [w for w in content_by_word if w not in stop_words]

count = Counter(content_no_stopwords)
print(count.most_common(10))
