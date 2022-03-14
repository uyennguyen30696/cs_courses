# p28.py
# Uyen Nguyen
# 02/10/22
# Python 3.10.0
# Description:
'''
Program 28:
Write a function which given two integer parameters Returns their sum...
unless the two values are the same, then the function Returns their doubled sum.
'''

def sum_double(a, b):
  if (a != b):
    return a + b
  elif (a == b):
    return (a + b) * 2

print (sum_double(1, 2))
print (sum_double(2, 2))

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_6/p28.py =========
3
8
'''