# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:53:58 2019

@author: AARADHYA JAIN
linear search
"""

n = int(input("Enter the size of the array"))
arr=[]
flag=0
for i in range(n):
	arr.append(input())
key = input("Enter the element to search")
for i in arr:
	if i==key:
		print(str(key)+" is found on index "+str(arr.index(i)))
		flag = 1
		break
if flag == 0:
	print(str(key)+" was not found.")