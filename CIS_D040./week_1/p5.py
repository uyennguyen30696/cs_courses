# p5.py
# Uyen Nguyen
# 01/07/22
# Python 3.10.0
# Description: Write a program which computes the sum and product of two numbers entered by the user.

# Ask the user to enter two numbers:
# Store those two numbers in 2 variables, num1, num2
num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))

# Make two new variables: total and product
total = num1 + num2
product = num1 * num2

# Output the sum and product
print ('The sum of', num1, 'and', num2, 'is:')
print (num1, '+', num2, '=', total)

print ('The product of', num1, 'and', num2, 'is:')
print (num1, 'x', num2, '=', product)

'''
============= RESTART: /Users/uyennguyen/Documents/CIS_D040A/p5.py =============
Please enter number 1: 1
Please enter number 2: 2
The sum of 1 and 2 is:
1 + 2 = 3
The product of 1 and 2 is:
1 x 2 = 2
'''