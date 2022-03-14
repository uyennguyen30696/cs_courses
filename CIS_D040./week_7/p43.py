# p43.py
# Uyen Nguyen
# 02/11/22
# Python 3.10.0
# Description:
'''
Program 43:

The function returns the sorted list in ascending order if parameter 'reverse' is False.
The function returns the sorted list in descending order if parameter 'reverse' is True.
'''

# Bubble sort

aList = [5,1,4,3,2]
reverse = True

def sort(aList, reverse):
  if reverse:
    for i in range(0, len(aList)):
      for j in range(0, len(aList) - 1):
        if aList[j] < aList[j + 1]:
          temp = aList[j]
          aList[j] = aList[j + 1]
          aList[j + 1] = temp
    return aList
  elif reverse == False:
    for i in range(0, len(aList)):
      for j in range(0, len(aList) - 1):
        if aList[j] > aList[j + 1]:
          temp = aList[j]
          aList[j] = aList[j + 1]
          aList[j + 1] = temp
    return aList

print ('Ascending:  ', sort(aList, False))
print ('Descending: ', sort(aList, True))

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p43.py =========
Ascending:   [1, 2, 3, 4, 5]
Descending:  [5, 4, 3, 2, 1]
'''