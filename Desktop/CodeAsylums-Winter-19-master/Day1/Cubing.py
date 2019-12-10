# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:35:47 2019

@author: AARADHYA JAIN

cubing the non negative numbers
"""

def cubing(a):
    if int(a)>=0:
        return int(a)*int(a)*int(a)
    else:
        return -1
        

n = int(input("Enter n"))
arr=[]
for i in range(n):
    print("Enter "+str(i)+"th number")
    arr.append(input())
for i in range(n):
    if cubing(arr[i])!=-1:
        print(cubing(arr[i]))
    else:
        print("Negative number")
