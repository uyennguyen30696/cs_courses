# p20.py
# Uyen Nguyen
# 01/14/22
# Python 3.10.0
# Description:
'''
Program 20:

Write a program that reads in X whole numbers and outputs (1) the sum of all positive numbers, (2) the sum of all negative numbers, and (3) the sum of all positive and negative numbers. 
The user can enter the X numbers in any different order every time, and can repeat the program if desired. 
'''

repeat = 'y'
while repeat == 'y':
  numCount = int(input('How many numbers would you like to enter? '))
  
  sumAll = 0    # Sum of all numbers
  sumPos = 0    # Sum of all positive numbers
  sumNeg = 0    # Sum of all negative numbers

  for i in range(1, numCount + 1):                    # Ask user to enter each number according to the count of numbers above
    num = int(input('Please enter number %i: ' %i))
    sumAll += num
    if num >= 0:
      sumPos += num
    if num < 0:
      sumNeg += num

  print('Sum of all numbers is:', sumAll)
  print('Sum of all positive numbers is:', sumPos)
  print('Sum of all negative numbers is:', sumNeg)

  repeat = input('Would you like to repeat? (y)(n): ')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_4/p20.py =========
How many numbers would you like to enter? 4
Please enter number 1: -1
Please enter number 2: -2
Please enter number 3: 5
Please enter number 4: 4
Sum of all numbers is: 6
Sum of all positive numbers is: 9
Sum of all negative numbers is: -3
Would you like to repeat? (y)(n): y
How many numbers would you like to enter? 5
Please enter number 1: 1
Please enter number 2: 3
Please enter number 3: -4
Please enter number 4: -1
Please enter number 5: 0
Sum of all numbers is: -1
Sum of all positive numbers is: 4
Sum of all negative numbers is: -5
Would you like to repeat? (y)(n): n
'''
