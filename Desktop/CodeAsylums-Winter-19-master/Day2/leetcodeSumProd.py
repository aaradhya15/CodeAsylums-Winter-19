# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:57:07 2019

@author: AARADHYA JAIN

problem link : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
"""

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sm=0
        mul=1
        while n>0:
            r = n%10
            sm=sm+r
            mul = mul*r
            n=n//10
        return mul-sm