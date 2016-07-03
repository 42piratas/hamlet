lt = [('oh', 13), ('ye', 12), ('mr', 11), ('sir', 8), ('yet', 7)]

d = {}

for i in lt:
    d[(i)[0]] = {'qtde': (i)[1]}

print d


''' oh: {   'quant': 13,
            'stemm' : 'u'tf',
            'stemm_quant': 7,
            'sent_good': 10,
            'sent_bad': 3}
'''
