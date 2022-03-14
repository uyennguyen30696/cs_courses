# final.py
# Uyen Nguyen
# 03/12/22
# Python 3.10.0
# Description:
'''
Final Exam Program:
You may not use the built-in python functions: sum(), average(), sort(), sorted(), median()
A) Use a loop to make 10 random numbers between 20 and 30, store them in a variable numList.
( Hint: use numList.append(number), where number is a randomint between 20 and 30 )
B) Sort the list using the bubble sort you learned in this class.
C) Show the sorted list and the unsorted list.
D) Find the sum, and average of the numbers in numList . 
E) Find the median of the list.
( Hint for 10 numbers the median is the average of the two numbers in the middle)
F) Show how many numbers are evenly divisible by 2
G) Copy/paste the Output of your program (A-F) as a multiline comment at the bottom of your program.
Save and submit the above program as Final.py
'''

from random import randint

# A) Create list with 10 random numbers
numList = []
for i in range(0, 10):
    num = randint(20, 30)
    numList.append(num)
print ('Unsorted list:', numList)

# B) Sort the list (ascending order) using bubble sort
for i in range(0, len(numList)):
    for j in range(0, len(numList) - 1):
        if numList[j] > numList[j + 1]:
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

# C) Show the sorted list
print ('Sorted list:', numList)

# D) Find sum and average of numbers in the list
sum = 0.0
average = 0.0
for i in range(0, len(numList)):
    sum += numList[i]
average = sum / len(numList)
print ('Sum =', sum)
print ('Average =', average)

# E) Find median of numbers in the list
# Length of list = 10 is even
medianIndex1 = int(len(numList) / 2)
medianIndex2 = int(len(numList) / 2) - 1
median = (numList[medianIndex1] + numList[medianIndex2]) / 2
print ('Median = ', median)

# F) Show how many numbers are evenly divisible by 2
count = 0
for i in range(0, len(numList)):
    if numList[i] % 2 == 0:
        count += 1
print ('There are', count, 'numbers evenly divisible by 2')

'''
===== RESTART: /Users/uyennguyen/Documents/CIS_D040./week_12_final/final.py ====
Unsorted list: [30, 25, 26, 25, 29, 23, 25, 22, 30, 26]
Sorted list: [22, 23, 25, 25, 25, 26, 26, 29, 30, 30]
Sum = 261.0
Average = 26.1
Median =  25.5
There are 5 numbers evenly divisible by 2
'''