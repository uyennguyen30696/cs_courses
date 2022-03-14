# p30.py
# Uyen Nguyen
# 02/10/22
# Python 3.10.0
# Description:
'''
Program 30:

Write a function which has two parameters, N and M.

The function returns True if N is evenly divisible by M, and False otherwise.
'''

n = int(input('Enter integer n: '))
m = int(input('Enter integer m: '))

def isDivisible(n, m):
  if (n % m == 0):
    return True
  elif (n % m != 0):
    return False

print (n, 'is evenly divisible by', m, 'is', isDivisible(n, m))

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_6/p30.py =========
Enter integer n: 8
Enter integer m: -2
8 is evenly divisible by -2 is True

Enter integer n: 9
Enter integer m: 4
9 is evenly divisible by 4 is False
'''