# p33.py
# Uyen Nguyen
# 02/10/22
# Python 3.10.0
# Description:
'''
Program 33:

If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle.

For any three sticks, there is a simple test to see if it is possible to form a triangle:

“If any of the three sticks is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can.”

Write a function named isTriangle(a,b,c) that has three sides a,b,c  as parameters.

The function returns either True or False, depending on whether you can form a triangle from the sides with the given lengths.
'''

a = int(input('Enter stick a length: '))
b = int(input('Enter stick b length: '))
c = int(input('Enter stick c length: '))

def isTriangle(a, b, c):
  if ((a + b < c) or (a + c < b) or (b + c < a)):
    return False
  else:
    return True

print ('Three sticks with length', a, b, c, 'can form a triangle:', isTriangle(a, b, c))

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_6/p33.py =========
Enter stick a length: 3
Enter stick b length: 6
Enter stick c length: 9
Three sticks with length 3 6 9 can form a triangle: True

Enter stick a length: 1
Enter stick b length: 3
Enter stick c length: 8
Three sticks with length 1 3 8 can form a triangle: False
'''