# p6.py
# Uyen Nguyen
# 01/09/22
# Python 3.10.0
# Description:
'''
Program 6 - Compute Height:

Write a program to compute a person's height.

INPUT: User will enter two whole numbers: feet and inches.
OUTPUT: Values input & total in inches.
INPUT VALIDATION: Make sure that feet and inches are positive values
Your program must run as shown below:

Please enter the number of feet:  4
Please enter the number of inches:  10
4 feet 10 inch(es) = 58 inches
'''

# Ask the user for height, feet and inches
print ('Please enter your height')
feet = float(input('feet: '))
inches = float(input('inches: '))

# Calculate the total inches
totalInches = feet * 12 + inches

# Show results
print ('%.0f feet %.0f inch(es) = %.0f inches'
       %(    feet,     inches,         totalInches)
      )

'''
========== RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_2/p6.py =========
Please enter your height
feet: 5
inches: 3
5 feet 3 inch(es) = 63 inches
'''
