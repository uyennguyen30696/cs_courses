# ch2_ex1.py
# Uyen Nguyen
# 04/10/22
# Python 3.10.0
# Description:
'''
Write a program to prompt the user for hours and rate per hour to compute gross pay.
'''

hours = float(input('Enter hours: '))
ratePerHour = float(input('Enter rate per hour: '))

total = round(hours * ratePerHour, 2)

print ('Gross pay =', total)

'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/exercises/exercise_1.py
Enter hours: 8
Enter rate per hour: 31.5
Gross pay = 252.0

Enter hours: 6.5
Enter rate per hour: 21.25
Gross pay = 138.12
'''