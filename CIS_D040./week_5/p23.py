# p23.py
# Uyen Nguyen
# 01/20/22
# Python 3.10.0
# Description:
'''
Program 23:

Write a program to let a child practice arithmetic skills.

The program should first ask for what kind of practice is wanted: addition(1), subtraction(2), or multiplicatio(3)... (no division).

Then, the program will have a loop for each of the the desired operations that lets the user repeat the practice as many times as desired,

Two random numbers will be generated (0 - 9), and the child will have to add, subtract or multiply them.

If the child answers the question correctly, congratulate them, and give them two different numbers to try.

If the child answers incorrectly, the problem should be repeated (with the two same numbers).

Note: You are not allowed to use the eval() or sum() functions!
'''

from random import randint

num1 = randint(0, 9)
num2 = randint(0, 9)

operation = input('Would you like to add (+), subtract (-), or multiply (*)? ')

# Add
while True:
    if operation == '+':
        ans = int(input('%i + %i = ? ' %(num1, num2)))
        # Ask the user again if the answer is incorrect
        while ans != num1 + num2:
            ans = int(input('That is incorrect! %i + %i = ? ' %(num1, num2)))
        if ans == num1 + num2:
            repeat = input('Correct! Would you like to try again? (1 for Yes, 2 for No): ')
            print ()
            if repeat == '1':
                operation = input('Would you like to add (+), subtract (-), or multiply (*)? ')
            elif repeat == '2':
                print ('\nThank you for playing!')
                break

# Subtract
    elif operation == '-':
            ans = int(input('%i - %i = ? ' %(num1, num2)))
            # Ask the user again if the answer is incorrect
            while ans != num1 - num2:
                ans = int(input('That is incorrect! %i - %i = ? ' %(num1, num2)))
            if ans == num1 - num2:
                repeat = input('Correct! Would you like to try again? (1 for Yes, 2 for No): ')
                print ()
                if repeat == '1':
                    operation = input('Would you like to add (+), subtract (-), or multiply (*)? ')
                elif repeat == '2':
                    print ('\nThank you for playing!')
                    break

# Multiply
    elif operation == '*':
            ans = int(input('%i * %i = ? ' %(num1, num2)))
            # Ask the user again if the answer is incorrect
            while ans != num1 * num2:
                ans = int(input('That is incorrect! %i * %i = ? ' %(num1, num2)))
            if ans == num1 * num2:
                print ()
                repeat = input('Correct! Would you like to try again? (1 for Yes, 2 for No): ')
                if repeat == '1':
                    operation = input('Would you like to add (+), subtract (-), or multiply (*)? ')
                elif repeat == '2':
                    print ('\nThank you for playing!')
                    break

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p23.py =========
Would you like to add (+), subtract (-), or multiply (*)? +
4 + 6 = ? 9
That is incorrect! 4 + 6 = ? 10
Correct! Would you like to try again? (1 for Yes, 2 for No): 1

Would you like to add (+), subtract (-), or multiply (*)? -
4 - 6 = ? -2
Correct! Would you like to try again? (1 for Yes, 2 for No): 1

Would you like to add (+), subtract (-), or multiply (*)? *
4 * 6 = ? 24

Correct! Would you like to try again? (1 for Yes, 2 for No): 2

Thank you for playing!
'''
