# ch3_ex2.py
# Uyen Nguyen
# 04/21/22
# Python 3.10.0
# Description:
'''
Write a program to prompt the user for hours and rate per hour to compute gross pay. 
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
'''

HOUR_PER_WEEK = 40
OVERTIME_RATE_EXTRA = 1.5
hours = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour: '))

if hours > HOUR_PER_WEEK:
    overtime_hours = hours - HOUR_PER_WEEK
    overtime_rate = rate_per_hour * OVERTIME_RATE_EXTRA
    total = round(HOUR_PER_WEEK * rate_per_hour + overtime_hours * overtime_rate, 2)
else:
    total = round(hours * rate_per_hour, 2)

print ('Gross pay =', total)

'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/exercises/ch3_exercise_2.py
Enter hours: 50
Enter rate per hour: 20
Gross pay = 1100.0

Enter hours: 40
Enter rate per hour: 15
Gross pay = 600.0

Enter hours: 35.5
Enter rate per hour: 20.25
Gross pay = 718.88

Enter hours: 30
Enter rate per hour: 10
Gross pay = 300.0
'''