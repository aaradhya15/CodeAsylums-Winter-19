# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:10:22 2019

@author: AARADHYA JAIN
"""
dict1={1: 1, 2: -4, 3: 9, 4: -16, 5: 25, 6: 36, 7: 49, 8: -64, 9: 81, 10: 100, 11: 121, 12: -144, 13: 169, 14: 196, 15: 225}

new_list = list(filter(lambda x:x>=0, dict1.values()))
print(new_list)