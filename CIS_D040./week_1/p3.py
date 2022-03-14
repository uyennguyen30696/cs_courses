# p3.py
# Uyen Nguyen
# 01/07/22
# Python 3.10.0
# Description: Program to take input in Python

name = input ("Please enter Your Name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age = int(input ("Please enter your age (whole number): " )) # an integer
weightKg = weightLbs * 0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print ( weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end = ' ') # end=' ' prevents new line
print ("kilograms ")

'''
============= RESTART: /Users/uyennguyen/Documents/CIS_D040A/p3.py =============
Please enter Your Name: Uyen
Please enter Your weight in lbs: 125
Please enter your age (whole number): 25
Hello Human Uyen your weight is
125.0 lbs
which equals = 56.70 kilograms 
'''
