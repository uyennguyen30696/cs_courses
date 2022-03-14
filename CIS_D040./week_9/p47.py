# p47.py
# Uyen Nguyen
# 03/01/22
# Python 3.10.0
# Description:
'''
Program 47:

Write a program which :

Writes a random number (50 to 55) of numbers (0 to 100) in a file
Opens the file and reads the numbers from it into a list
Sorts the list and Shows it.
Calculates the median.
Note: You may NOT use the Python built in functions: sort(), sorted(), sum(), median()

Hint to calculate median:
If there is an odd number of data values then the median will be
the value in the middle.
For the data set: 1, 1, 2, 5, 6, 6, 9  the median is 5.

If there is an even number of data values then the median will be
the average of the two data values in the middle.

For the data set: 1, 1, 2, 6, 6, 9  the median is 4.
The middle two values are 2 and 6, so (2+6) / 2 = 8  /2 = 4
'''

# Writes a random number (50 to 55) of numbers (0 to 100) in a file
from random import randint
totalNum = randint(50, 55)

newFile = open('randomNum.txt', 'w')

for i in range(0, totalNum):
  newFile.write( str(randint(0, 100)) + '\n')
newFile.close()

# Opens the file and reads the numbers from it into a list
newFile = open('randomNum.txt', 'r')
fileAsListOfLines = newFile.read().splitlines()
print ('File as list of lines: \n', fileAsListOfLines)
newFile.close()

# Sorts the list and Shows it
# Bubble sort
for i in range(0, len(fileAsListOfLines)):
  for j in range(0, len(fileAsListOfLines) - 1):
    if int(fileAsListOfLines[j]) > int(fileAsListOfLines[j + 1]):
      temp = fileAsListOfLines[j]
      fileAsListOfLines[j] = fileAsListOfLines[j + 1]
      fileAsListOfLines[j + 1] = temp
print ('Sorted file: \n', fileAsListOfLines)

# Calculates the median
# Convert each string in the list fileAsListOfLines to int for easy access
for i in range(0, len(fileAsListOfLines)):
  fileAsListOfLines[i] = int(fileAsListOfLines[i])
  
# Odd number of numbers
if len(fileAsListOfLines) % 2 != 0:
  medianIndex = int(len(fileAsListOfLines) / 2)
  median = fileAsListOfLines[medianIndex]
  print ('Median = ', median)
  
# Even number of numbers
elif len(fileAsListOfLines) % 2 == 0:
  medianIndex1 = int(len(fileAsListOfLines) / 2)
  medianIndex2 = int(len(fileAsListOfLines) / 2) - 1
  median = (fileAsListOfLines[medianIndex1] + fileAsListOfLines[medianIndex2]) / 2
  print ('Median = ', median)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_9/p47.py =========
File as list of lines: 
 ['80', '21', '18', '76', '11', '26', '27', '78', '31', '77', '54', '100', '85', '50', '87', '79', '72', '92', '89', '58', '74', '72', '42', '90', '63', '21', '49', '84', '88', '3', '84', '89', '44', '93', '26', '57', '56', '50', '51', '31', '92', '20', '36', '41', '1', '82', '4', '48', '50', '35']
Sorted file: 
 ['1', '3', '4', '11', '18', '20', '21', '21', '26', '26', '27', '31', '31', '35', '36', '41', '42', '44', '48', '49', '50', '50', '50', '51', '54', '56', '57', '58', '63', '72', '72', '74', '76', '77', '78', '79', '80', '82', '84', '84', '85', '87', '88', '89', '89', '90', '92', '92', '93', '100']
Median =  55.0
'''
