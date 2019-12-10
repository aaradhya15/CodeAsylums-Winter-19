# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:03:49 2019

@author: AARADHYA JAIN
"""

s = input("enter the string")
j = len(s)-1
i = 0
flag = 1
while(j>=i):
    if(s[i]==s[j]):
        i=i+1
        j=j-1
        continue
    else:
        flag = 0
        break
if(flag == 1):
    print("given string is a palindrome")
else:
    print("not a palindrome")
