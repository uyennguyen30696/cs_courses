# p31.py
# Uyen Nguyen
# 02/10/22
# Python 3.10.0
# Description:
'''
Program 31:
Write a function that has an integer N as parameter and returns true if N is even.
'''

n = int(input('Enter integer n: '))

def isEven(n):
  if (n % 2 == 0):
    return True
  elif (n % 2 != 0):
    return False

print (n, 'is even:', isEven(n))

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_6/p31.py =========
Enter integer n: 12
12 is even: True

Enter integer n: 9
9 is even: False
'''