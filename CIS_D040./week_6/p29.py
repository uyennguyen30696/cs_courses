# p29.py
# Uyen Nguyen
# 02/10/22
# Python 3.10.0
# Description:
'''
Program 29:
Write a function that calculates the absolute value and returns the absolute value of a number.
'''

a = float(input('Enter a positive or negative value: '))

def absolute(a):
  if (a >= 0):
    return a
  else:
    a = a * (-1)
    return a

print ('The absolute value of', a, 'is', absolute(a))

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_6/p29.py =========
Enter a positive or negative value: 6
The absolute value of 6.0 is 6.0

Enter a positive or negative value: -6
The absolute value of -6.0 is 6.0
'''