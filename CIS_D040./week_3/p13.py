# p13.py
# Uyen Nguyen
# 01/10/22
# Python 3.10.0
# Description:
'''
Program 13:

Write a program to convert any given number of total cents (under 100) into the correct number of: quarters, dimes, nickels, pennies.

Hint: use integer casting,  66/25 equals 2.64 , but int(66/25) = 2
'''

# User enters total cents
totalCents = int(input('Enter total cents (100 or lower): '))
if totalCents > 100:
    totalCents = int(input('Enter total cents (100 or lower): '))

# Use integer division to get a whole number for quarters:
quarters = int(totalCents / 25)

# If there are any quarters
if quarters > 0:
    # Show how many quarters they have
    print ('You have', quarters, 'quarters x 25c =', quarters * 25, 'cents total')
    # Subtract the quarters from total cents to get the remaining cents
    totalCents = totalCents - quarters * 25

# Use integer division to get a whole number for dimes:
dimes = int(totalCents / 10)

# If there are any dimes
if dimes > 0:
    # Show how many dimes they have
    print ('You have', dimes, 'dimes x 10c =', dimes * 10, 'cents total')
    # Subtract the dimes from total cents to get the remaining cents
    totalCents = totalCents - dimes * 10

# Use integer division to get a whole number for nickels:
nickels = int(totalCents / 5)

# If there are any nickels
if nickels > 0:
    # Show how many nickels they have
    print ('You have', nickels, 'nickels x 5c =', nickels * 5, 'cents total')
    # Subtract the nickels from total cents to get the remaining cents, also equals to pennies
    totalCents = totalCents - nickels * 5

# Use integer division to get a whole number for pennies:
pennis = totalCents

# If there are any cents
if pennis > 0:
    # Show how many cents they have
    print ('You have', pennis, 'pennis x 1c =', pennis * 1, 'cents total')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p13.py =========
Enter total cents (100 or lower): 68
You have 2 quarters x 25c = 50 cents total
You have 1 dimes x 10c = 10 cents total
You have 1 nickels x 5c = 5 cents total
You have 3 pennis x 1c = 3 cents total

========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p13.py =========
Enter total cents (100 or lower): 17
You have 1 dimes x 10c = 10 cents total
You have 1 nickels x 5c = 5 cents total
You have 2 pennis x 1c = 2 cents total

========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p13.py =========
Enter total cents (100 or lower): 7
You have 1 nickels x 5c = 5 cents total
You have 2 pennis x 1c = 2 cents total

========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p13.py =========
Enter total cents (100 or lower): 3
You have 3 pennis x 1c = 3 cents total
'''
