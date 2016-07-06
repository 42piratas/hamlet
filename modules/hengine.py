'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import string
import hg

from collections import Counter
from nltk.stem import PorterStemmer, WordNetLemmatizer


ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

'''SHOULD tag, stem and lemmatize together!!!!!!'''

# def hengine_raw():
#
#     # Stem words from raw content
#     hg.content_raw_words_stemmed = [ps.stem(w) for w in hg.content_raw_words]
#
#     # Counting unique stemmed words from raw content
#     hg.content_raw_words_stemmed_unique_len = len(set(hg.content_raw_words_stemmed))


def hengine_filtered():
    for w in hg.content_filtered_words:
        # Add steammed word to list of stemmed words
        hg.content_filtered_words_stemmed.append(ps.stem(w))
        # Add tag to list of tags
        tagged = nltk.pos_tag(w)
        hg.content_filtered_words_tags.append(tagged[0][1])
        # Add lemmatized word to list of lemmatized words
        lem = lemmatizer.lemmatize(w)
        hg.content_filtered_words_lemmatized.append(lem)

        # Filtered Matrix

    # Counting unique stemmed words from raw content
    hg.content_filtered_words_stemmed_unique_len = len(set(hg.content_filtered_words_stemmed))
