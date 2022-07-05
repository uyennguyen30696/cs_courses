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

# Calculate pay
def computePay(hours, rate_per_hour):
    HOUR_PER_WEEK = 40
    OVERTIME_RATE_EXTRA = 1.5

    if hours > HOUR_PER_WEEK:
        overtime_hours = hours - HOUR_PER_WEEK
        overtime_rate = rate_per_hour * OVERTIME_RATE_EXTRA
        total = round(HOUR_PER_WEEK * rate_per_hour + overtime_hours * overtime_rate, 2)
    else:
        total = round(hours * rate_per_hour, 2)
        
    return total
