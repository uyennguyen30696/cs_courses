# ch5_ex3.py
# Uyen Nguyen
# 05/02/22
# Python 3.10.0
# Description:
'''
Rewrite your Chapter 5 - Exercise 2
Check your code for any invalid inputs: string inputs and also negative numbers
Rewrite your code to validate the inputs and keep asking the user to enter valid inputs for the hours and the rate value.
'''

from random import randint

HOUR_PER_WEEK = 40
OVERTIME_RATE_EXTRA = 1.5

def get_input():
    hours = 0.00
    rate_per_hour = 0.00
    repeat_hour = True
    repeat_rate = True

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
    
    while repeat_rate:
        try:
            rate_per_hour = float(input('Enter rate per hour (dollars/hour): '))
            if rate_per_hour >= 0:
                repeat_rate = False
            else:
                print ('Error! Please enter a positive number!')
        except:
            print ('Error! Please enter a numberic value!')

    return company, hours, rate_per_hour

def compute_pay(hours, rate_per_hour):
    if hours > HOUR_PER_WEEK:
        overtime_hours = hours - HOUR_PER_WEEK
        overtime_rate = rate_per_hour * OVERTIME_RATE_EXTRA
        total = round(HOUR_PER_WEEK * rate_per_hour + overtime_hours * overtime_rate, 2)
    else:
        total = round(hours * rate_per_hour, 2)
    return total

def get_document_number(total):
    document_number = 0
    if total >= 0:
        document_number = randint(1000, 2000)
    return document_number

def print_output(company, hours, rate_per_hour, total, document_number):
    print ('\n')
    print ('Company:', company)
    print ('Hours:    ', round(hours, 2))
    print ('Rate:     ', round(rate_per_hour, 2))
    print ('Gross pay:', total)
    print ('******************************')
    print ('Your document number is:', document_number)

def main():
    the_company, the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    the_document_number = get_document_number(the_pay)
    print_output(the_company, the_hours, the_rate, the_pay, the_document_number)

main()

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch5_ex3.py =====
Please enter your company's name:       Future Corp.


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: -35
Error! Please enter a positive number!
Enter your work hours per week: Thirty five
Error! Please enter a numberic value!
Enter your work hours per week: 35
Enter rate per hour (dollars/hour): Twenty
Error! Please enter a numberic value!
Enter rate per hour (dollars/hour): 20.25


Company: Future Corp.
Hours:     35.0
Rate:      20.25
Gross pay: 708.75
******************************
Your document number is: 1590


Please enter your company's name: Future Corp.


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: 40.00
Enter rate per hour (dollars/hour): 41.5


Company: Future Corp.
Hours:     40.0
Rate:      41.5
Gross pay: 1660.0
******************************
Your document number is: 1259


Please enter your company's name: Future Corp.


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: 46.5
Enter rate per hour (dollars/hour): 30.75


Company: Future Corp.
Hours:     46.5
Rate:      30.75
Gross pay: 1529.81
******************************
Your document number is: 1663
'''
