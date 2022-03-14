# p42.py
# Uyen Nguyen
# 02/11/22
# Python 3.10.0
# Description:
'''
Program 42:

Write the below 5 functions according to the following requirements:

sum (list_parameter) : returns the sum of numbers inside a list
average (list_parameter) : returns the average of numbers inside a list
min (list_parameter) : returns the smallest of all numbers inside a list
max (list_parameter) : returns the largest of all numbers inside a list
main () : calls all the other functions above
'''

aList = []
x = int(input('How many numbers would you want to enter? '))

# Add X numbers to a list
for i in range(0, x):
  nums = int(input('Please enter number %i: ' %(i + 1)))
  aList.append(nums)
print ('List: ', aList)

# Sum
def sumNums(aList):
  sumNum = 0
  for i in range(0, len(aList)):
    sumNum += aList[i]
  return sumNum

# Average
def average(aList):
  avg = sumNums(aList) / len(aList)
  return avg

# Min
def minNums(aList):
  minNum = aList[0]
  for i in range(0, len(aList)):
    if aList[i] < minNum:
      minNum = aList[i]
  return minNum

# Max
def maxNums(aList):
  maxNum = aList[0]
  for i in range(0, len(aList)):
    if aList[i] > maxNum:
      maxNum = aList[i]
  return maxNum

def main(aList):
  print ('Sum =', sumNums(aList))
  print ('Average =', average(aList))
  print ('Min =', minNums(aList))
  print ('Max =', maxNums(aList))

main(aList)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p42.py =========
How many numbers would you want to enter? 3
Please enter number 1: 1
Please enter number 2: 2
Please enter number 3: 3
List:  [1, 2, 3]
Sum = 6
Average = 2.0
Min = 1
Max = 3
'''