# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:14:10 2019

@author: AARADHYA JAIN
"""

dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict2 = sorted(dict1.items(),key = lambda x:x[1])
n = len(dict2)
ans = [dict2[i][0] for i in range(n-3,n)]
print(ans)