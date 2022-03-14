# p1.py
# Uyen Nguyen
# 01/07/22
# Python 3.10.0
# Description: Program to show output in Python

print('hello world') # single quote
print("hello world") # double quote
print("he\nllo") # \n insert a new line (same as pressing Enter)

# VARIABLES are named storage locations for numbers, strings, lists
# STRING is anything enclosed in quotes "Hello World", that's a string
# NUMBER can be either a FLOAT (Ex: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Uyen", "Nguyen"]
myName = "Uyen" # declare/initialize string variable myName
Weight = 125.1234 # declare/initialize float variable Weight
Age = 25 # declare/initialize int variable Age
Grades = [90,95,89] # list
nameZ = ["Uyen", "Nguyen"] # list

print ("Hello", myName)
print ("Your weight is", Weight, "and your age is", Age)
print ("Your weight is %.2f and your age is %i" %(Weight, Age)) # f in %.2f = float, round off to 2 decimals, i in %i = int
print ("Lists: grades =", Grades, "nameZ =", nameZ)
print ("This is how you print", end =' ') # end=' ' prevents new line
print ("on the same line")

'''
============= RESTART: /Users/uyennguyen/Documents/CIS_D040A/p1.py =============
hello world
hello world
he
llo
Hello Uyen
Your weight is 125.1234 and your age is 25
Your weight is 125.12 and your age is 25
Lists: grades = [90, 95, 89] nameZ = ['Uyen', 'Nguyen']
This is how you print on the same line
'''
