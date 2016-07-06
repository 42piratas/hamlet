    # TEMP
    # for w in hg.content_no_stopwords:
    # postag =
    # content_NNP = [w[0][0] for w in hg.content_no_stopwords if (pos_tag(w))[0][1] == "NNP"]
    # print(content_NNP)

import nltk
import hg

from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter



def htag_raw_content():
    content_raw_words_tags = []
    for w in hg.content_raw_words:
        tagged = nltk.pos_tag([w])
        content_raw_words_tags.append(tagged[0][1])

    # Identify top tags from raw content
    content_raw_words_tags_counter = Counter(hg.content_raw_tags)
    hg.content_raw_words_tags_top = (content_raw_words_tags_counter.most_common(hg.top_words_num))

    print(hg.content_raw_words_tags_top)


if __name__ == '__main__':
    from hextractor import hextract
    from hfilter import hfilter
    hextract()
    hfilter()
    htag_raw_content()
