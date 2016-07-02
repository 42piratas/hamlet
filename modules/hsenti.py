# '''
# @author: 42piratas
# '''
#
# # -*- coding: utf-8 -*-
#
#
# import hg
#
# from senti_classifier import senti_classifier
#
# def senti():
#     top_words_string = ""
#     for t in hg.top_words:
#         top_words_string += t[0]
#     pos_score, neg_score = senti_classifier.polarity_scores(top_words_string)
#     print(pos_score, neg_score)
#
# if __name__ == '__main__':
#     senti()
