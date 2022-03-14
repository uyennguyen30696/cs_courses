# p39.py
# Uyen Nguyen
# 02/11/22
# Python 3.10.0
# Description:
'''
Program 39:

Write a program that asks the user to enter a sentence.
Your program will:

Show how many words are in the sentence 
Show the last word of the sentence
Ask the user to enter their own word, and count how many times their word appears in the sentence
'''

sentence = input('Enter a sentence: ')
words = sentence.split()
last = words[len(words) - 1]

# Show how many words are in the sentence
print ('There are', len(words), 'word(s) in this sentence')

# Show the last word of the sentence
print ('The last word in this sentence is',  "'", last, "'")

# Ask the user to enter their own word
word = input('Enter a word to search: ')
# Count how many times their word appears in the sentence
count = 0
for i in range (0, len(words)):
  if words[i] == word:
    count += 1

print ('The word', "'", word, "'", 'appears', count, 'time(s) in the sentence')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p39.py =========
Enter a sentence: This is a sentence
There are 4 word(s) in this sentence
The last word in this sentence is ' sentence '
Enter a word to search: is
The word ' is ' appears 1 time(s) in the sentence
'''
