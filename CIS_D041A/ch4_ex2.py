# ch4_ex2.py
# Uyen Nguyen
# 04/26/22
# Python 3.10.0
# Description:
'''
You wrote a program to prompt the user for hours and rate per hour to compute gross pay. Also your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.
Rewrite your code to validate the inputs and keep asking the user to enter valid inputs for the hours and the rate value.
'''

from random import randint

HOUR_PER_WEEK = 40
OVERTIME_RATE_EXTRA = 1.5
hours = 0.00
rate_per_hour = 0.00
document_number = 0
repeat_hour = True
company = input('Please enter your company\'s name: ').strip()

print ('\n')
print('Please enter numeric and positive numbers for the following questions. ')

while repeat_hour:
    try:
        hours = float(input('Enter your work hours per week: '))
        if hours >= 0:
            repeat_hour = False
        else:
            print ('Error! Please enter a positive number!')
    except:
        print ('Error! Please enter a numberic value!')
repeat_rate = True
while repeat_rate:
    try:
        rate_per_hour = float(input('Enter rate per hour (dollars/hour): '))
        if rate_per_hour >= 0:
            repeat_rate = False
        else:
            print ('Error! Please enter a positive number!')
    except:
        print ('Error! Please enter a numberic value!')
if hours > HOUR_PER_WEEK:
    overtime_hours = hours - HOUR_PER_WEEK
    overtime_rate = rate_per_hour * OVERTIME_RATE_EXTRA
    total = round(HOUR_PER_WEEK * rate_per_hour + overtime_hours * overtime_rate, 
2)
else:
    total = round(hours * rate_per_hour, 2)

document_number = randint(1000, 2000)

print ('\n')
print ('Company:', company)
print ('Hours:    ', round(hours, 2))
print ('Rate:     ', round(rate_per_hour, 2))
print ('Gross pay:', total)
print ('******************************')
print ('Your document number is:', document_number)

'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/exercises/ch4_exercise_2.py
Please enter your company's name: Future Corp


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: forty
Error! Please enter a numberic value!
Enter your work hours per week: forty dollars
Error! Please enter a numberic value!
Enter your work hours per week: 40
Enter rate per hour (dollars/hour): -30
Error! Please enter a positive number!
Enter rate per hour (dollars/hour): thirty
Error! Please enter a numberic value!
Enter rate per hour (dollars/hour): 30


Company: Future Corp
Hours:     40.0
Rate:      30.0
Gross pay: 1200.0
******************************
Your document number is: 1946


Please enter your company's name: Future Corp


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: 46.30
Enter rate per hour (dollars/hour): 30.25


Company: Future Corp
Hours:     46.3
Rate:      30.25
Gross pay: 1495.86
******************************
Your document number is: 1205


Please enter your company's name: Future Corp


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: 30
Enter rate per hour (dollars/hour): 25.5


Company: Future Corp
Hours:     30.0
Rate:      25.5
Gross pay: 765.0
******************************
Your document number is: 1036
'''
