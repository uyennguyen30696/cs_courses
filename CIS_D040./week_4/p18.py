# p18.py
# Uyen Nguyen
# 01/14/22
# Python 3.10.0
# Description:
'''
Program 18:

Write a program that displays the characters in the ASCII character table from ! to ~.

Display ten characters per line.

The characters are separated by exactly one space.
'''

count = 0 
for i in range(33, 127):        # ascii characters 33 to 126
    print (chr(i), end = ' ')
    count += 1                  # To count every character shown
    if count % 10 == 0:         # Every 10 characters
        print()                 # Start a new line

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_4/p18.py =========
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
'''
