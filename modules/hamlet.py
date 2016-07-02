'''
@author: 42piratas
'''

# -*- coding: utf-8 -*-


import hg
import hextractor
import hpdfs
import hwrangler
import hcounter
# import hsenti

hg.filename = "randomtexts.txt"
hg.n = 5

hextractor.extract()
hwrangler.wrangle()
hcounter.count()

# hsenti.senti()
