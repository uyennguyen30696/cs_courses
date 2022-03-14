# p24.py
# Uyen Nguyen
# 01/20/22
# Python 3.10.0
# Description:
'''
Program 24:

Write a program that generates X random integers Num.

Num is a random number between 20 to 50. 

X is a random number between 10 to 15.

Calculate and show the Smallest, Largest, Sum, and Average of those numbers.

You are not allowed to use Python functions sample(), min(), max(), average(), sort(), sorted()!!
'''

from random import randint

# X is random integers between 10 to 15
x = randint(10, 15)
print ('x =', x)

# Generate X random numbers between 20 to 50
i = 1
sum = 0
for i in range(1, x + 1):
    num = randint(20, 50)
    print ('num %2i =' %i, num)

    # Smallest number
    if i == 1:
        smallest = num
    else:
        if num < smallest:
            smallest = num
    
    # Largest number
    if i == 1:
        largest = num
    else:
        if num > largest:
            largest = num

    # Sum
    sum += num

    # Average
    average = int(sum / (x))

print ('The smallest number is', smallest)  
print ('The largest number is', largest)
print ('Sum of all numbers is', sum)
print ('The average of all numbers is', average)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p24.py =========
x = 14
num  1 = 44
num  2 = 26
num  3 = 34
num  4 = 35
num  5 = 43
num  6 = 23
num  7 = 22
num  8 = 44
num  9 = 26
num 10 = 44
num 11 = 23
num 12 = 40
num 13 = 46
num 14 = 41
The smallest number is 22
The largest number is 46
Sum of all numbers is 491
The average of all numbers is 35
'''
