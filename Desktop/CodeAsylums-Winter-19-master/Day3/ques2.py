# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:26:30 2019

@author: AARADHYA JAIN
"""

n1 = int(input("Enter the number of elements in list 1"))
n2 = int(input("Enter the number of elements in list 2"))


lst1 = []
lst2 = []
print("enter elements of list1")
for i in range(n1):
    lst1.append(input())

print("enter elements of list2")
for i in range(n2):
    lst2.append(input())

new_list = list(map(lambda x,y:int(x)+int(y),lst1,lst2))
print(new_list)