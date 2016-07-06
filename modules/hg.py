'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

filename = "document.txt"
top_words_num = 10

# Raw Content
content_raw = ""
content_raw_words = []
content_raw_words_len = 0
content_raw_words_top = []
content_raw_words_unique_len = 0

content_raw_words_syns = []
content_raw_words_syns_top = []

content_raw_words_tags = []
content_raw_words_tags_top = []

content_raw_words_stemmed = []
content_raw_words_stemmed_unique_len = 0

# Filtered Content
content_filtered_words = []
content_filtered_words_len = 0
content_filtered_words_tops = []
content_filtered_words_unique_len = 0

content_filtered_words_tags = []
content_filtered_words_tags_top = []

content_filtered_words_stemmed = []
content_filtered_words_stemmed_unique_len = 0
content_filtered_words_stemmed_unique_top_words = []

content_filtered_words_matrix_tops = {}
