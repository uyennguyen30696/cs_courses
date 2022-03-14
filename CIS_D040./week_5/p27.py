# p27.py
# Uyen Nguyen
# 01/20/22
# Python 3.10.0
# Description:
'''
Program 27:

Write a program that generates a random list of letters.

# start with an
empty_list = [ ]
# and use
empty_list.append(Letter) # to add letters to the list

The length of the list of letters changes every time you run the program.

There can be a random number of X  letters on the list, where X is a random number between 50 to 75.

Each of the letters on the list is a random letter between A to F (uppercase).

Use a loop to generate the list and then Show the generated list of letters to the user.

Count and then show to the user how many times the letter B appears.
'''

from random import randint

# Create an empty list x
x = []
# Generate random length of the list
len = randint(50, 75)
# To count how many times the letter B appears
countB = 0

# Append random letter between A to F to the list (use ascii table)
for i in range(0, len):
    asciiNum = randint(65, 70)
    letter = chr(asciiNum)
    x.append(letter)

    if x[i] == 'B':
        countB += 1

print ('Make a list of', len, 'letters: ')
print (x)
print('Letter B appears', countB, 'time(s)')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p27.py =========
Make a list of 58 letters: 
['E', 'B', 'F', 'F', 'A', 'F', 'F', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'D', 'F', 'E', 'A', 'B', 'C', 'E', 'D', 'D', 'A', 'B', 'E', 'B', 'D', 'B', 'A', 'F', 'D', 'E', 'D', 'D', 'E', 'D', 'A', 'E', 'F', 'B', 'B', 'F', 'F', 'E', 'E', 'A', 'B', 'B', 'B', 'C', 'F', 'C', 'D', 'D', 'F', 'F', 'C']
Letter B appears 12 time(s)
'''
