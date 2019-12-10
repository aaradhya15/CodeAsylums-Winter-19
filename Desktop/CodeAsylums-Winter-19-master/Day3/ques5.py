# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:41:51 2019

@author: AARADHYA JAIN
"""
dict1 = {1:[1],2:1,3:[3,4]}
new_list = list(filter(lambda x:(isinstance(x,list)), dict1.values()))
print(len(new_list))