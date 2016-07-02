'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-

import hg
import os
import sys


def extract():

    # Open the file
    with open(os.path.join(os.path.dirname(__file__), '../documents/', hg.filename), 'r') as open_file:
        # Read the file
        content = open_file.read()
        # Lower
        hg.content = content
