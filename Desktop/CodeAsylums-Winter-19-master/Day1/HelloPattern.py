# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:36:31 2019

@author: AARADHYA JAIN


"""

num = int(input("enter the number"))
arr=[]
while num>0:
    arr.append(num%10)
    #print(num%10)
    num=num//10
    #print(num)
arr.reverse()
for i in range(len(arr)):
    for j in range(arr[i]):
        print("hello "+str(j+1),end=" ")
    print()

    
