# p11.py
# Uyen Nguyen
# 01/09/22
# Python 3.10.0
# Description:
'''
Program 11 - Rock, Paper, Scissors:

Write a program to simulate rock-paper-scissors game.

Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.

The program then shows the winner on the basis of:
Paper covers Rock
Rock breack Scissors
Scissors cut Paper
Tie
Test your program multiple times to makes sure it works! Submit all 4 of your tests as a comment.

Extra challenge: Have the Player 2 number be randomly generated by the computer (not entered by the user).
'''

# Need this for randint()
import random

# Make the random numbers for p1 or p2
# In this case, assume p2 is the computer generating random numbers
# Syntax: randint(start, end)
p2 = random.randint(1,3)

# Ask user for input
p1 = int(input('p1 enter 1 for rock, 2 for paper, 3 for scissors: '))

# Show the generated values
print('p1 =', p1)
print('p2 =', p2)

# Make variables to store values for rock paper scissors
rock = 1
paper = 2
scissors = 3

# 3 cases when p1 wins
if p1 == rock and p2 == scissors:
    print("p1 wins, rock breaks scissors")
elif p1 == paper and p2 == rock:
    print("p1 wins, paper covers rock")
elif p1 == scissors and p2 == paper:
    print ("p1 wins, scissors cut paper")

# 3 cases when p2 wins
if p2 == rock and p1 == scissors:
    print("p2 wins, rock breaks scissors")
elif p2 == paper and p1 == rock:
    print("p2 wins, paper covers rock")
elif p2 == scissors and p1 == paper:
    print ("p2 wins, scissors cut paper")

# 3 cases when p1 and p2 tie
if p2 == rock and p1 == rock:
    print("tie")
elif p2 == paper and p1 == paper:
    print("tie")
elif p2 == scissors and p1 == scissors:
    print("tie")

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_2/p11.py =========
p1 enter 1 for rock, 2 for paper, 3 for scissors: 2
p1 = 2
p2 = 2
tie
'''
