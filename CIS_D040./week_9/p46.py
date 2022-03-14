# p46.py
# Uyen Nguyen
# 03/01/22
# Python 3.10.0
# Description:
'''
Program 46:

Write a Python program to do the following:

Let the user enter a file name (such as "myMovies.txt").
Let the user enter the titles of 4 of their favorite movies using a loop.
Write using a loop the 4 movie titles to a file, one per line, and closes the file.
Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them in a list, and then shows the list.
Write the titles in reverse order into a file "reverseOrder.txt"
'''

fileName = input('Enter a file name for your movie list (ends with .txt): ')

# Make a file named after the user input
newFile = open(fileName, 'w')

# Let the user enter the titles of 4 of their favorite movies and write the titles into the created file
for i in range(0, 4):
    movie = input('Enter movie title %i: ' %(i + 1))
    newFile.write(movie + '\n')

# Read the 4 movie titles
newFile = open(fileName, 'r')
fileAsListOfLines = newFile.read().splitlines()
print ('File as list of lines: ', fileAsListOfLines)

# Write the titles in reverse order
reverseFile = open('reverseOrder.txt', 'w')
for i in range(3, -1, -1):   # i = 3, 2, 1, 0
    reverseFile.write(fileAsListOfLines[i] + '\n')

reverseFile = open('reverseOrder.txt', 'r')
reverseFileAsListOfLines = reverseFile.read().splitlines()
print ('Reverse file as list of lines: ', reverseFileAsListOfLines)

newFile.close()
reverseFile.close()

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_9/p46.py =========
Enter a file name for your movie list (ends with .txt): myMovies.txt
Enter movie title 1: Fairy tail
Enter movie title 2: Attack on titan
Enter movie title 3: Demon slayer
Enter movie title 4: Death note
File as list of lines:  ['Fairy tail', 'Attack on titan', 'Demon slayer', 'Death note']
Reverse file as list of lines:  ['Death note', 'Demon slayer', 'Attack on titan', 'Fairy tail']
'''
