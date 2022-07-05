# ch6_ex5
# Uyen Nguyen
# 05/14/22
# Python 3.10.0
# Description:
'''
Ask the user for their company validate it to be in the database list. If user enters invalid inputs after the second invalid input show the company list in the database 
Ask the user the rate and the hours and validate them to be numeric and positive value
If 'hours' is greater than 40, multiply 1.5 to the rate for the overtime
print the pay stub
Use modules and import them to the main file
'''

# Ask the user for company name, work hours, and rate
# Validate the input
def getInputs():
    #company database list
    COMPANYLIST = ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']
    hours = 0.00
    rate_per_hour = 0.00
    repeat_hour = True
    repeat_rate = True

    # Ask the user for their company validate it to be in the database list. 
    # If user enters invalid inputs after the second invalid input show the company list in the database 
    found_company = True
    count = 0
    while found_company:
        companyInput = input('Please enter your company name: ').strip()
        if companyInput in COMPANYLIST:
            found_company = False
            count = 0
        while count >= 1:
            print ('Company list: ')
            print (*COMPANYLIST, sep = ', ')
            companyInput = input('Please enter a valid company name from the database: ').strip()
            if companyInput in COMPANYLIST:
                found_company = False
                count = 0
        count += 1

    print ('\n')
    print('Please enter numeric and positive numbers for the following questions. ')

    # Ask the user the rate and the hours and validate them to be numeric and positive value
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

    return companyInput, hours, rate_per_hour
