# p14.py
# Uyen Nguyen
# 01/10/22
# Python 3.10.0
# Description:
'''
Program 14:
Write a program that asks the user for day and month of a birthday.

The program then tells the Zodiac signs that will be compatible with that birthday.
'''

# User enter day and month of birth
day = int(input('Please enter day of birth: '))
month = int(input('Please enter month of birth: '))

# Check for Zodiac signs
if ( month == 3 and day >= 21 ) or ( month == 4 and day <= 19 ):
    print('You are Aries the Ram')
elif ( month == 4 and day >= 20 ) or ( month == 5 and day <= 20 ):
    print('You are Taurus the Bull')
elif ( month == 5 and day >= 21 ) or ( month == 6 and day <= 21 ):
    print('You are Gemini the Twins')
elif ( month == 6 and day >= 22 ) or ( month == 7 and day <= 22 ):
    print('You are Cancer the Crab')
elif ( month == 7 and day >= 23 ) or ( month == 8 and day <= 22 ):
    print('You are Leo the Lion')
elif ( month == 8 and day >= 23 ) or ( month == 9 and day <= 22 ):
    print('You are Virgo the Virgin')
elif ( month == 9 and day >= 23 ) or ( month == 10 and day <= 23 ):
    print('You are Libra the Balance')
elif ( month == 10 and day >= 24 ) or ( month == 11 and day <= 21 ):
    print('You are Scorpio the Scorpion')
elif ( month == 11 and day >= 22 ) or ( month == 12 and day <= 21 ):
    print('You are Satittarius the Archer')
elif ( month == 12 and day >= 22 ) or ( month == 1 and day <= 19 ):
    print('You are Capricorn the Goat')
elif ( month == 1 and day >= 20 ) or ( month == 2 and day <= 18 ):
    print('You are Aquarius the Water Bearer')
elif ( month == 2 and day >= 19 ) or ( month == 3 and day <= 20 ):
    print('You are Pisces the Fishes')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_3/p14.py =========
Please enter day of birth: 30
Please enter month of birth: 6
You are Cancer the Crab
'''
