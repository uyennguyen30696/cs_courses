# ch3_ex3.py
# Uyen Nguyen
# 04/20/22
# Python 3.10.0
# Description:
'''
Write a program to prompt the user for hours and rate per hour to compute gross pay. 
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.
'''

HOUR_PER_WEEK = 40
OVERTIME_RATE_EXTRA = 1.5

print('Please enter numeric and positive numbers: ')
repeat_hour = True
while repeat_hour:
    try:
        hours = float(input('Enter hours: '))
        if hours > 0:
            repeat_hour = False
        else:
            print ('Error! Please enter a positive number!')
    except:
        print ('Error! Please enter a numberic value!')

repeat_rate = True
while repeat_rate:
    try:
        rate_per_hour = float(input('Enter rate per hour: '))
        if rate_per_hour >= 0:
            repeat_rate = False
        else:
            print ('Error! Please enter a positive number!')
    except:
        print ('Error! Please enter a numberic value!')

if hours > HOUR_PER_WEEK:
    overtime_hours = hours - HOUR_PER_WEEK
    overtime_rate = rate_per_hour * OVERTIME_RATE_EXTRA
    total = round(HOUR_PER_WEEK * rate_per_hour + overtime_hours * overtime_rate, 2)
else:
    total = round(hours * rate_per_hour, 2)

print ('Gross pay =', total)

'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/exercises/ch3_exercise_3.py
Please enter numeric and positive numbers: 
Enter hours: forty-seven
Error! Please enter a numberic value!
Enter hours: forty seven
Error! Please enter a numberic value!
Enter hours: -2
Error! Please enter a positive number!
Enter hours: 47
Enter rate per hour: -1
Error! Please enter a positive number!
Enter rate per hour: ten dollars
Error! Please enter a numberic value!
Enter rate per hour: 10.5
Gross pay = 530.25

Please enter numeric and positive numbers: 
Enter hours: 40
Enter rate per hour: 30.25
Gross pay = 1210.0

Please enter numeric and positive numbers: 
Enter hours: 35.75
Enter rate per hour: 22.5
Gross pay = 804.38
'''