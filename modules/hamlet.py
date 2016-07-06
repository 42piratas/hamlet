'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import hg

from hextractor import hextract
from hfilter import hfilter
from hstem import hsteammer_raw, hsteammer_filtered
# import hsenti


hg.filename = "document.txt"
hg.top_words_num = 10

hextract()
hfilter()

hsteammer_raw()
hsteammer_filtered()

# hsenti.senti()

""" PROCESS:
hexctractor > hfilter > hsteammer > htagger > hentfinder
"""

# Report
print("\nSUMMARY ######################################")

print("\nRAW CONTENT BY WORDS *************************")
print("Total words from raw content: ", hg.content_raw_words_len)
print("Unique words from raw content: ", hg.content_raw_words_unique_len)
print("Top %s words from raw content: " %(hg.top_words_num), hg.content_raw_words_top)

print("\nFILTERED CONTENT BY WORDS ************************")
print("Total words from filtered content: ", hg.content_filtered_words_len)
print("Unique words from filtered content: ", hg.content_filtered_words_unique_len)
print("Top %s words from filtered content: " %(hg.top_words_num), hg.content_filtered_words_tops)

print("\nSTEMMED CONTENT BY WORDS ************************")
# print("Total unique stemmed words:", content_filtered_stemmed_unique)
# print("Top %s unique stemmed words: " %(top_words_num), content_filtered_stemmed_unique_top_words)
# print("######################################")
# print("TOP %s WORDS:" %top_words_num)
# for w in content_filtered_top_words_matrix:
#     print(w, content_filtered_top_words_matrix[w])
