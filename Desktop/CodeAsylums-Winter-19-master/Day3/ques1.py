# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:14:58 2019

@author: AARADHYA JAIN
"""
n = int(input("Enter the number of strings"))
lst = []
for i in range(n):
    lst.append(input())
new_lst = list(filter(lambda x:x[0]==x[-1] , lst))
print(len(new_lst))
    
      

































