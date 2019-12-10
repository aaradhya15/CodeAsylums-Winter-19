# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:25:19 2019

@author: AARADHYA JAIN
"""
if __name__ == "__main__": 
    print ("Executed when invoked directly")
else: 
    print ("Executed when imported")

def crds(n):
    ans=0
    for i in range(n):
        ans = ans + 3*i
    return (ans-n)%1000007
        
n = int(input())
for i in range(n):
    k = int(input())
    print(crds(k))