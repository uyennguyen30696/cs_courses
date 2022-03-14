# p40.py
# Uyen Nguyen
# 02/11/22
# Python 3.10.0
# Description:
'''
Program 40:
Ask the user to enter X numbers into a list. Calculate and show the sum, average, min, max of those numbers.
'''

aList = []
x = int(input('How many numbers would you want to enter? '))

# Add X numbers to a list
for i in range(0, x):
  nums = int(input('Please enter number %i: ' %(i + 1)))
  aList.append(nums)
print ('List: ', aList)

# Sum
sumNum = 0
for i in range(0, len(aList)):
  sumNum += aList[i]
print ('Sum =', sumNum)

# Average
avg = sumNum / len(aList)
print ('Average =', avg)

# Min
minNum = aList[0]
for i in range(0, len(aList)):
  if aList[i] < minNum:
    minNum = aList[i]
print ('Min =', minNum)

# Max
maxNum = aList[0]
for i in range(0, len(aList)):
  if aList[i] > maxNum:
    maxNum = aList[i]
print ('Max =', maxNum)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p40.py =========
How many numbers would you want to enter? 5
Please enter number 1: 1
Please enter number 2: 2
Please enter number 3: 3
Please enter number 4: 4
Please enter number 5: 5
List:  [1, 2, 3, 4, 5]
Sum = 15
Average = 3.0
Min = 1
Max = 5
'''