# p12.py
# Uyen Nguyen
# 01/10/22
# Python 3.10.0
# Description:
'''
Program 12:
Write a program to determine if the user can vote. The program will ask the user a series of questions - age, citizenship and registration. The user will receive a message as to whether or not s/he may vote -- yes, no (with a reason - too young, not a citizen, hasn't registered to vote).

Be sure to test your program at least 4 times:

The user can vote
The user can't vote because they are not old enough.
The user can't vote because they are not old enough and not a citizen.
The user can't vote because they are not old enough, not a citizen, not registered.
Note: You must be over 18, registered , and a citizen to vote.
'''

# Ask user for input
age = int(input('Please enter age: '))
citizen = input('Are you citizen? (y/n): ')
registered = input('Are you registered? (y/n): ')

# Check if they can vote
if age >= 18 and citizen == 'y' and registered == 'y':
    print('Congratulations, you can vote!')
else:
    print ('Sorry you can not vote.')
# Tell them why they can't vote
    if age < 18:
        print('You are not old enough.')
    if citizen != 'y':
        print('You are not a citizen.')
    if registered != 'y':
        print('You must register to vote.')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p12.py =========
Please enter age: 20
Are you citizen? (y/n): y
Are you registered? (y/n): y
Congratulations, you can vote!

========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p12.py =========
Please enter age: 16
Are you citizen? (y/n): y
Are you registered? (y/n): n
Sorry you can not vote.
You are not old enough.

========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p12.py =========
Please enter age: 14
Are you citizen? (y/n): n
Are you registered? (y/n): y
Sorry you can not vote.
You are not old enough.
You are not a citizen.

========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p12.py =========
Please enter age: 14
Are you citizen? (y/n): n
Are you registered? (y/n): n
Sorry you can not vote.
You are not old enough.
You are not a citizen.
You must register to vote.
'''