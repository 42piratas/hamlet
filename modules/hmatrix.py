'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import nltk
import hg


from nltk.stem import PorterStemmer, WordNetLemmatizer
from senti_classifier import senti_classifier
from nltk.corpus import wordnet


ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Stand back! We're going to try Science!!!")

def hmatrix_filtered():
    for w in hg.content_filtered_words_tops:
        # Quantity
        hg.content_filtered_words_matrix_tops[w[0]] = {'Qtde' : w[1]}
        # Tagged
        tagged = nltk.pos_tag([w[0]])
        hg.content_filtered_words_matrix_tops[w[0]]['Tag'] = tagged[0][1]
        # Synonym
        if wordnet.synsets(w[0]):
            hg.content_filtered_words_matrix_tops[w[0]]['Synonym'] = wordnet.synsets(w[0])[0].name()
        else:
            hg.content_filtered_words_matrix_tops[w[0]]['Synonym'] = "---"
        # Antonym
        # if wordnet.synsets(w[0]):
        #     hg.content_filtered_words_matrix_tops[w[0]]['Antonym'] = wordnet.antonyms()#(w[0])[0]
        # else:
        #     hg.content_filtered_words_matrix_tops[w[0]]['Antonym'] = "---"
        # Steammed
        hg.content_filtered_words_matrix_tops[w[0]]['Stemmed'] = ps.stem(w[0])
        # Lemmatized
        lem = lemmatizer.lemmatize(w[0])
        hg.content_filtered_words_matrix_tops[w[0]]['Lemm'] = lem
        # Sentiment Analyzer
        pos_score, neg_score = senti_classifier.polarity_scores(w[0])
        hg.content_filtered_words_matrix_tops[w[0]]['Score +'] = pos_score
        hg.content_filtered_words_matrix_tops[w[0]]['Score -'] = neg_score


if __name__ == '__main__':
    from hextractor import hextract
    from hfilter import hfilter
    hextract()
    hfilter()
    hmatrix_filtered()
    for w in hg.content_filtered_words_matrix_tops:
        print(w, hg.content_filtered_words_matrix_tops[w])
    print("Finished! <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
