# p17.py
# Uyen Nguyen
# 01/14/22
# Python 3.10.0
# Description:
'''
Program 17:

Suppose that the tuition for a university is $10,000 this year and increases 5% every year.

Write a program that computes the tuition in ten years and displays a table of the years and tuition costs. A loop must be used.
'''

tuition = 10000 
for i in range(1, 11):
  print("Year %2i     Tuition %i" %(i, tuition))
  tuition += tuition * 0.05
  
'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_4/p17.py =========
Year  1     Tuition 10000
Year  2     Tuition 10500
Year  3     Tuition 11025
Year  4     Tuition 11576
Year  5     Tuition 12155
Year  6     Tuition 12762
Year  7     Tuition 13400
Year  8     Tuition 14071
Year  9     Tuition 14774
Year 10     Tuition 15513
'''
