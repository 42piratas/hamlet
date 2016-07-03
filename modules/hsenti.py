'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-


import hg

from senti_classifier import senti_classifier

def senti():
    for w in hg.content_summary:
        pos_score, neg_score = senti_classifier.polarity_scores(w)
        hg.content_summary[w].append({'positive': pos_score})
        hg.content_summary[w].append({'negative': neg_score})


if __name__ == '__main__':
    senti()
