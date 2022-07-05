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

# Print the pay stub
def printPay(companyInput, hours, rate_per_hour, total):
    print ('\n')
    print ('Company:', companyInput)
    print ('Hours:    ', round(hours, 2))
    print ('Rate:     ', round(rate_per_hour, 2))
    print ('Gross pay:', total)
