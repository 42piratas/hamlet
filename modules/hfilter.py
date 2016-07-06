'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import string
import hg

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from collections import Counter

stop_words = set(stopwords.words("english"))
# syns = wordnet.synset

'''Filtered content means:
- Punctuation removed
- Tokenized by words
- Stopwords removed'''

def hfilter():

    # RAW CONTENT ##############################

    # Remove punctuation
    content_raw_no_punctuation = hg.content_raw.translate(None, string.punctuation)
    # Tokenize by words
    hg.content_raw_words = word_tokenize(content_raw_no_punctuation)

    # Counting words from raw content
    hg.content_raw_words_len = len(hg.content_raw_words)
    # Counting unique words from raw content
    hg.content_raw_words_unique_len = len(set(hg.content_raw_words))

    # Defining top words from raw content
    content_raw_words_counter = Counter(hg.content_raw_words)
    hg.content_raw_words_top = (content_raw_words_counter.most_common(hg.top_words_num))

    # # Creating list of synonyms
    # for w in hg.content_raw_words:
    #     syn = syns(w)
    #     hg.content_raw_words_syns.append(syn)

    # FILTERED CONTENT ##############################

    # Remove stop words // Filtered by words!
    hg.content_filtered_words = [w for w in hg.content_raw_words if w not in stop_words]

    # Counting words from filtered content
    hg.content_filtered_words_len = len(hg.content_filtered_words)
    # Counting unique words from raw content
    hg.content_filtered_words_unique_len = len(set(hg.content_filtered_words))

    # Defining top words from filtered content
    content_filtered_words_counter = Counter(hg.content_filtered_words)
    hg.content_filtered_words_tops = (content_filtered_words_counter.most_common(hg.top_words_num))


if __name__ == '__main__':
    from hextractor import hextract
    hextract()
    hfilter()
