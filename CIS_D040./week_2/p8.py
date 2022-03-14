# p8.py
# Uyen Nguyen
# 01/09/22
# Python 3.10.0
# Description:
'''
Program 8 - Multiplication Table:

Multiplication Table
Write a program to print a multiplication table for float values  0.1, 0.2 and 0.3.

The Output should use the placeholder (%) to control column widths.

Save and submit as p8.py
'''

print("     0.1   0.2   0.3")
print("0.1  %.2f  %.2f  %.2f" %(0.1 * 0.1, 0.1 * 0.2, 0.1 * 0.3))
print("0.2  %.2f  %.2f  %.2f" %(0.2 * 0.1, 0.2 * 0.2, 0.2 * 0.3))
print("0.3  %.2f  %.2f  %.2f" %(0.3 * 0.1, 0.3 * 0.2, 0.3 * 0.3))

'''
========== RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_2/p8.py =========
     0.1   0.2   0.3
0.1  0.01  0.02  0.03
0.2  0.02  0.04  0.06
0.3  0.03  0.06  0.09
'''
