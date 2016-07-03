'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import hg
import string
from collections import Counter

from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


ps = PorterStemmer()
stop_words = set(stopwords.words("english"))


def wrangle():
    # Lower
    content_lower = hg.content
    # Remove punctuation
    content_no_punctuation = content_lower.translate(None, string.punctuation)
    # Tokinize by words
    hg.content_by_word = word_tokenize(content_no_punctuation)
    # Remove stop words
    hg.content_no_stopwords = [w for w in hg.content_by_word if w not in stop_words]

    # Counting non-filtered
    hg.content_nonfiltered_len = len(hg.content_by_word)
    content_nonfiltered_counter = Counter(hg.content_by_word)
    hg.content_nonfiltered_top = (content_nonfiltered_counter.most_common(hg.n))

    # Reducing filtered content to 'n' top words
    hg.content_filtered_len = len(hg.content_no_stopwords)
    content_filtered_counter = Counter(hg.content_no_stopwords)
    hg.content_filtered_top = (content_filtered_counter.most_common(hg.n))
    for w in hg.content_filtered_top:
        hg.content_summary[(w)[0]] = [{'qtde': (w)[1]}]

    # Tagging 'n' tops words
    for w in hg.content_summary:
        postag = pos_tag([w])
        hg.content_summary[w].append({'pos-tag': postag[0][1]})

    # Stem all filtered words and counting uniques
    content_stemmed = [ps.stem(w) for w in hg.content_no_stopwords]
    hg.content_stemmed_unique = len(set(content_stemmed))
    content_stemmed_counter = Counter(content_stemmed)
    hg.content_stemmed_top = (content_stemmed_counter.most_common(hg.n))

    # Stem 'n' top filtered words
    for w in hg.content_summary:
        s = ps.stem(w)
        hg.content_summary[w].append({'stem': s})
        hg.content_summary[w].append({'stem qtde': 'xxx'}) # NEED HELP (ALSO) HERE!
