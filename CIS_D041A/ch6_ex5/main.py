# ch6_ex5
# Uyen Nguyen
# 05/14/22
# Python 3.10.0
# Description:
'''
Ask the user for their company validate it to be in the database list. If user enters invalid inputs after the second invalid input show the company list in the database 
Ask the user the rate and the hours and validate them to be numeric and positive value
If "hours" is greater than 40, multiply 1.5 to the rate for the overtime
print the pay stub
Use modules and import them to the main file
'''

import sys 
sys.dont_write_bytecode = True

from getInputsFile import getInputs
from computePayFile import computePay
from printPayFile import printPay

'''
This function is to process all other fucntions to get inputs,
calculate and print the pay stub
'''
def payProcess():
    the_company, the_hours, the_rate = getInputs()
    the_pay = computePay(the_hours, the_rate)
    printPay(the_company, the_hours, the_rate, the_pay)


if __name__ == '__main__':
    payProcess()

'''
=== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex5/main.py ==
Please enter your company name: test
Please enter your company name: test
Company list: 
Amazon, Apple, Facebook, Google, Uber
Please enter a valid company name from the database: test
Company list: 
Amazon, Apple, Facebook, Google, Uber
Please enter a valid company name from the database: Uber


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: 30
Enter rate per hour (dollars/hour): 10.5


Company: Uber
Hours:     30.0
Rate:      10.5
Gross pay: 315.0
'''

'''
=== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex5/main.py ==
Please enter your company name: Amazon


Please enter numeric and positive numbers for the following questions. 
Enter your work hours per week: 45.5
Enter rate per hour (dollars/hour): 40.25


Company: Amazon
Hours:     45.5
Rate:      40.25
Gross pay: 1942.06
'''
