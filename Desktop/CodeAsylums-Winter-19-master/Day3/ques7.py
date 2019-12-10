# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:13:34 2019

@author: AARADHYA JAIN
"""
from functools import reduce

dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
sm = reduce((lambda x,y:x+y), dict1.values())

for i in dict1.keys():
    dict1[i] = sm/int(len(dict1.values()))
print(dict1)
    