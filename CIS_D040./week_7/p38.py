# p38.py
# Uyen Nguyen
# 02/11/22
# Python 3.10.0
# Description:
'''
Program 38:

Write a program that asks the user to enter a sentence.

The program then finds the longest word in the sentence, and shows it.

Note: The use of python functions max() and sorted() is not permitted!
'''

sentence = input('Enter a sentence: ')
# Remove special characters in sentence
# sentence = ''.join(filter(str.isalnum, sentence))
words = sentence.split()

longest = words[0]

for i in range(1, len(words)):
  # Compare longest to every other words
  if len(words[i]) > len(longest):
    longest = words[i]

print ('The longest word is', "'", longest, "'")
print ('which has', len(longest), 'characters')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p38.py =========
Enter a sentence: This is a sentence
The longest word is ' sentence '
which has 8 characters
'''