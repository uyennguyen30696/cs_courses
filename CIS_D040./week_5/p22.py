# p22.py
# Uyen Nguyen
# 01/20/22
# Python 3.10.0
# Description:
'''
Program 22:

Write a Dice Game program that generates two random dice values between 1 and 6 for you, and 2 for the computer.

You get to roll as many times as you like (if you don't like your 2 dice), 
while the computer only rolls once, after you have decided that you like your two dice. 

Determine who wins, you or the computer.
'''

from random import randint

print ('Beat the computer!\n')

# Random rolls for the user
keep = 'n'
while keep == 'n':
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print ('You rolled a %i and a %i (total = %i)' %(d1, d2, d1 + d2))
    keep = input('Do you want to keep those? (y or n): ')

    # Run loop until the user chooses 'y'
    if keep == 'y':
        break
    elif keep == 'n':
        print ('\nRolling again...')

    # Prevent other keys rather than y or n are pressed
    while keep != 'n' and keep != 'y':
        keep = (input('Plese enter y or n: '))
        if keep == 'n':
            print ('\nRolling again...')

# Random rolls for computer
pc1 = randint(1, 6)
pc2 = randint(1, 6)
print ('\nThe computer rolled a %i and a %i (total = %i)' %(pc1, pc2, pc1 + pc2))

# Compare the total of 2 rolls from user to those from computer
if d1 + d2 > pc1 + pc2:
    print ('Yay you win!')
elif d1 + d2 < pc1 + pc2:
    print ('Sorry, you lose!')
else:
    print ('It is a tie')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p22.py =========
Beat the computer!

You rolled a 5 and a 2 (total = 7)
Do you want to keep those? (y or n): n

Rolling again...
You rolled a 5 and a 6 (total = 11)
Do you want to keep those? (y or n): s
Plese enter y or n: n

Rolling again...
You rolled a 6 and a 5 (total = 11)
Do you want to keep those? (y or n): y

The computer rolled a 5 and a 3 (total = 8)
Yay you win!
'''

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p22.py =========
Beat the computer!

You rolled a 6 and a 2 (total = 8)
Do you want to keep those? (y or n): y

The computer rolled a 6 and a 3 (total = 9)
Sorry, you lose!
'''

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/p22.py =========
Beat the computer!

You rolled a 1 and a 4 (total = 5)
Do you want to keep those? (y or n): y

The computer rolled a 3 and a 2 (total = 5)
It is a tie
'''
