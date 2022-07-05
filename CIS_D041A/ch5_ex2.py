# ch5_ex2.py
# Uyen Nguyen
# 05/02/22
# Python 3.10.0
# Description:
'''
Rewrite your pay computation with time-and-a-half for overtime and create a function called compute_pay which takes two parameters ( hours and rate).
'''

HOUR_PER_WEEK = 40
OVERTIME_RATE_EXTRA = 1.5

def get_input():
    hours = float(input('Enter hours: '))
    rate_per_hour = float(input('Enter rate per hour: '))
    return hours, rate_per_hour

def compute_pay(hours, rate_per_hour):
    if hours > HOUR_PER_WEEK:
        overtime_hours = hours - HOUR_PER_WEEK
        overtime_rate = rate_per_hour * OVERTIME_RATE_EXTRA
        total = round(HOUR_PER_WEEK * rate_per_hour + overtime_hours * overtime_rate, 2)
    else:
        total = round(hours * rate_per_hour, 2)
    return total

def print_output(total):
    print ('Gross pay =', total)

def main():
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)

main()

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch5_ex2.py =====
Enter hours: 35
Enter rate per hour: 10.25
Gross pay = 358.75

Enter hours: 45.5
Enter rate per hour: 20.5
Gross pay = 989.12
'''