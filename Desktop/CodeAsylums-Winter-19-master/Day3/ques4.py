# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:03:47 2019

@author: AARADHYA JAIN
"""

dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 225, 15: 225}
set1=set([])
set1={j for j in dict1.values()}
'''for j in dict1.values():
    #set1 = (dict1[i] for i in range(len(dict1)))
    set1.add(j)'''
print(set1)