# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:42:21 2019

@author: AARADHYA JAIN

SPOJ: ADDREV
"""
def rev(n):
    num=0
    while n>0:
        rem=n%10
        num=num*10+rem
        n=n//10
    return num
    
n = int(input())
for i in range(n):
    k1,k2 = input().split()
    k1 = int(k1)
    k2 = int(k2)
    print(rev(rev(k1)+rev(k2)))
    
    

    