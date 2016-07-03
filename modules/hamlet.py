'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-


import hg
import hextractor
import hpdfs
import hwrangler
import hsenti

hg.filename = "document.txt"
hg.n = 10

hextractor.extract()
hwrangler.wrangle()
hsenti.senti()

# Report
print("######################################")
print("SUMMARY:")
print("Total general words: ", hg.content_nonfiltered_len)
print("Top %s general words: " %(hg.n), hg.content_nonfiltered_top)
print("Total words without stopwords: ", hg.content_filtered_len)
print("Top %s words without stopwords: " %(hg.n), hg.content_filtered_top)
print("Total unique stemmed words:", hg.content_stemmed_unique)
print("Top %s unique stemmed words: " %(hg.n), hg.content_stemmed_top)
print("######################################")
print("TOP %s WORDS:" %hg.n)
for w in hg.content_summary:
    print(w, hg.content_summary[w])
