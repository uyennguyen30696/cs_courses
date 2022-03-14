# p15.py
# Uyen Nguyen
# 01/10/22
# Python 3.10.0
# Description:
'''
Program 15:

Write a program that asks the user to enter 4 numbers (positive or negative).

The program shows:

the sum of all numbers (sumAll)
the sum of positive numbers (sumPos),
the sum of negative numbers (sumNeg)
The Algorithm for this problem:

sumNeg is going to hold the total of all negative numbers, it starts at zero (0)
sumPos is going to hold the total of all positive numbers, it starts at zero (0)
if a number is negative you ADD it to sumNeg
if a number is positive you ADD it to sumPos
'''

# User enters four numbers
a = float(input('Enter number 1: '))
b = float(input('Enter number 2: '))
c = float(input('Enter number 3: '))
d = float(input('Enter number 4: '))

# Sum of all numbers
sumAll = 0
sumAll += a
sumAll += b
sumAll += c
sumAll += d
print ('Sum of all numbers is %.2f' %sumAll)

# Sum of positive numbers
sumPos = 0
if a > 0:
    sumPos = sumPos + a # Only add it to sumPos if it is a positive number
if b > 0:
    sumPos += b
if c > 0:
    sumPos += c
if d > 0:
    sumPos += d
print ('Sum of positive numbers is %.2f' %sumPos)

# Sum of negative numbers
sumNeg = 0
if a < 0:
    sumNeg = sumNeg + a # Only add it to sumNeg if it is a negative number
if b < 0:
    sumNeg += b
if c < 0:
    sumNeg += c
if d < 0:
    sumNeg += d
print ('Sum of negative numbers is %.2f' %sumNeg)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p15.py =========
Enter number 1: 3.143
Enter number 2: -2.432
Enter number 3: -1.002
Enter number 4: 4.124
Sum of all numbers is 3.83
Sum of positive numbers is 7.27
Sum of negative numbers is -3.43
'''
