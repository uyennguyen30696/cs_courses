# p25.py
# Uyen Nguyen
# 01/20/22
# Python 3.10.0
# Description:
'''
Program 25:

Write a program that asks the user to input a sentence.

The program will ask the user what two letters are to be counted.

You must use a “for” loop to go through the sentence & count how many times the chosen letter appears in the sentence.

You are not allowed to use python built-in function "count()" or you'll get a Zero!

Output will show the sentence, the letter, and the number of times the letter appears in the sentence.
'''

# Ask the user to input a sentence and two letters to be counted
sentence = input('Please enter a sentence: ')
l1 = input('Please enter letter 1: ')
l2 = input('Please enter letter 2: ')

count1 = 0
count2 = 0
for i in range(0, len(sentence)):
    if sentence[i] == l1:
        count1 += 1
    elif sentence[i] == l2:
        count2 += 1

print ('Letter 1 occurs %i' %count1, 'time(s)')
print ('Letter 2 occurs %i' %count2, 'time(s)')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p25.py =========
Please enter a sentence: hello
Please enter letter 1: l
Please enter letter 2: t
Letter 1 occurs 2 time(s)
Letter 2 occurs 0 time(s)
'''
