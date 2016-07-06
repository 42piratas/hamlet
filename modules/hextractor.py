'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import os
import sys
import hg


def hextract():

    # MUST IMPLEMENT PDF READER HERE

    # Open the file
    with open(os.path.join(os.path.dirname(__file__), '../documents/', hg.filename), 'r') as open_file:
        # Read the file
        hg.content_raw = open_file.read()

if __name__ == '__main__':
    extract()
    print("Content: ", hg.content_raw)
