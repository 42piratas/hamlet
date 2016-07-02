import hg

from collections import Counter


def count():

    # Total words
    content_nonfiltered_len = len(hg.content_by_word)
    content_nonfiltered_counter = Counter(hg.content_by_word)
    content_nonfiltered_top = (content_nonfiltered_counter.most_common(hg.n))

    # Non-stemmed words with no stopwords
    content_filtered_len = len(hg.content_no_stopwords)
    content_filtered_counter = Counter(hg.content_no_stopwords)
    content_filtered_top = (content_filtered_counter.most_common(hg.n))

    # Stemmed words with no stopwords
    content_stemmed_unique = len(set(hg.content_stemmed))
    content_stemmed_counter = Counter(hg.content_stemmed)
    content_stemmed_top = (content_stemmed_counter.most_common(hg.n))

    print("Total general words: ", content_nonfiltered_len)
    print("Top %s general words: " %(hg.n), content_nonfiltered_top)
    print("Total words without stopwords: ", content_filtered_len)
    print("Top %s words without stopwords: " %(hg.n), content_filtered_top)
    print("Total unique stemmed words:", content_stemmed_unique)
    print("Top %s unique stemmed words: " %(hg.n), content_stemmed_top)
