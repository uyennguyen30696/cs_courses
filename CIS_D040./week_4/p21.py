# p21.py
# Uyen Nguyen
# 01/14/22
# Python 3.10.0
# Description:
'''
Program 21:

Which of the below gives you more money?

1) A penny which doubles it's value every day over 30 days, or

2) A million dollars

Write a program which calculates exactly how much more (or less) you can make with the penny on day 30. A loop must be used.
'''

# Calculate how many cents a penny becomes if it doubles itself every day over 30 days
penny = 1
for i in range(1, 31):
  penny = penny * 2
print('After 30 days, a penny becomes', penny, 'cents.')

# Convert total cents after 30 days into dollars
dollars = penny / 100
penny = penny - int(dollars) * 100
print('Total =', int(dollars), 'dollars and', penny, 'cent')

# Compare to a million dollars
difference = int(dollars) - 1000000 

if difference > 0:
  print ("A penny that doubles it's value every day for 30 days is more than a million dollars by", difference, 'dollars.')
elif difference < 0: 
  print ("A penny that doubles it's value every day for 30 days is less than a million dollars by", difference, 'dollars.')
elif difference == 0:
  print ("A penny that doubles it's value every day for 30 days is the same as a million dollars on day 1.")

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_4/p21.py =========
After 30 days, a penny becomes 1073741824 cents.
Total = 10737418 dollars and 24 cent
A penny that doubles it's value every day for 30 days is more than a million dollars by 9737418 dollars.
'''
