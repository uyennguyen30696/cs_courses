# p26.py
# Uyen Nguyen
# 01/20/22
# Python 3.10.0
# Description:
'''
Program 26:

Write a program that generates a random list of numbers.

(start with an empty list and use append() )

The length of the list X can be a random number between 15 to 20.

Each of the random numbers on the list can be between 2 to 5.

Count how many times the number 3 appears.
'''

from random import randint

# Create an empty list x
x = []
# Length of list x is random, from 15 to 20
len = randint(15, 20)
# To count how many times number 3 appears
count3 = 0

# Append random numbers from 2 to 5 to the list
for i in range(0, len):
    num = randint(2, 5)
    x.append(num)

    # Count how many times number 3 appears
    if x[i] == 3:
        count3 += 1

print ('Generating a list of', len, 'numbers: ')
print (x)
print ('Number 3 appears', count3, 'time(s)')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p26.py =========
Generating a list of 15 numbers: 
[3, 4, 2, 4, 3, 5, 2, 4, 2, 3, 5, 2, 2, 4, 2]
Number 3 appears 3 time(s)
'''
