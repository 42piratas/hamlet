'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import os
import sys
import nltk
import string

from nltk.corpus import stopwords
from collections import Counter


def get_clean_tokens():
    # with open('randomtexts.txt', 'r') as content:
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'randomtexts.txt'), 'r') as content:

        text = content.read()
        # Lower
        lowers = text.lower()
        # Remove the punctuation using the character deletion step of translate
        no_punctuation = lowers.translate(string.punctuation)
        # Remove stopwords
        filtered = [w for w in no_punctuation if not w in stopwords.words('english')]
        # Tokenize
        tokens = nltk.word_tokenize(filtered)

        return tokensu


tokens = get_clean_tokens()
count = Counter(tokens)
print(count)
print(count.most_common(10))






"""READ A PDF / BUT NEED TO SOLVE BUGS FIRST :)
# from nltk.tokenize import sent_tokenize, word_tokenize
import PyPDF2 # Caso seja PDF a ser lido

# Read a PDF file
pdf_to_read = open('distributedscrumprimer-1.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(pdf_to_read)
pdf_num_pages = pdf.numPages
# page = pdf.getPage(9)
# content = page.extractText()
# print(content)

# Put the content of each page as a single value
# in a list / i.e. one list-value for each page
content_by_pages = []
for page_num in range(pdf_num_pages):
    page = pdf.getPage(page_num)
    page_content = page.extractText()
    content_by_pages.append(page_content)
"""
