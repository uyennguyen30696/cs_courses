# p10.py
# Uyen Nguyen
# 01/09/22
# Python 3.10.0
# Description:
'''
Program 10 - Letter Grades with Input Validation:

Write a program which asks the user for a student's grade as a percent, and then returns their letter grade.

Validate the input to make sure that the number is between 0 - 100 . If for any other number, say "ERROR" and ask for another number)

A is 90% or above
B is between 80% and 90%
C is between 70% and 80%
D is between 60% and 70%
F is under 60%

Sample Run:
Please enter a grade in percent: -1
Error, the number must be between 0 to 100.
Please enter a grade in percent: 75
You have a "C"
'''

# Ask the user to enter grade as percent
percent = float(input('Please enter your grade as percent: '))

# Validate input
if percent < 0 or percent > 100:
    print ('Error, percent must be between 0 to 100')
    percent = float(input('Please enter value between 0 to 100:'))

# Show the correct letter grade based on the percent
if percent >= 90 and percent <= 100:
    print('Your grade is "A" ')
elif percent >= 80 and percent <= 90:
    print ('Your grade is "B" ')
elif percent >= 70 and percent <= 80:
    print ('Your grade is "C" ')
elif percent >= 60 and percent <= 70:
    print ('Your grade is "D" ')
elif percent < 60:
    print ('Your grade is "F" ')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_2/p10.py =========
Please enter your grade as percent: 98
Your grade is "A" 
'''
