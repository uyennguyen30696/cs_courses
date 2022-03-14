# p45.py
# Uyen Nguyen
# 02/24/22
# Python 3.10.0
# Description:
'''
Debug the program below so that it works as shown in the test run.
'''

num = int(input("Please enter a number: "))

def isEven(num): # should have a parameter
  if num % 2 == 0:
    return True 
  elif num % 2 != 0:
    return False

def main(num): # needs to be called first
   print ("The number %i is even: %s" %(num, isEven(num)))

main(num)

'''
==== RESTART: /Users/uyennguyen/Documents/CIS_D040./week_8_midterm/debug.py ====
Please enter a number: 6
The number 6 is even: True
'''
