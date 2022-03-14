# p45.py
# Uyen Nguyen
# 02/24/22
# Python 3.10.0
# Description:
'''
Write the following two function definitions, and call each function appropriately in order to test and show how each function works.
Write and test both functions in the same twoFunctions.py file.
'''

'''
Function 1:
Write a function named "speed" which has 2 PARAMETERS: distance, time.
The functions computes and PRINTS the speed = distance/ time . The value is shown rounded to 2 values to the right of the decimal point.
'''

def speed(distance, time):
    result = float(distance) / float(time)
    return '%.2f' %result

print (speed(730, 12))

'''
= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_8_midterm/twoFunctions.py
60.83
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
Function 2:
Write a function named "middle" which has 3 PARAMETERS: num1, num2, num3.
The function RETURNS the middle/median value of the 3 arguments. Assume 3 different values as parameters.
'''

def middle(num1, num2, num3):
    if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
        return num1
    elif (num2 > num1 and num2 < num3) or (num2 > num3 and num2 < num1):
        return num2
    elif (num3 > num1 and num3 < num2) or (num3 > num2 and num3 < num1):
        return num3

print ( middle(1, 2, 5) )
print ( middle(2, 1, 5) )
print ( middle(1, 5, 2) )

'''
= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_8_midterm/twoFunctions.py
2
2
2
'''
