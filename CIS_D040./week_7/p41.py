# p41.py
# Uyen Nguyen
# 02/11/22
# Python 3.10.0
# Description:
'''
Program 41:

Write a function which outputs as many crosses
as the parameter 'numCrosses' indicates.
'''

numCrosses = int(input('Enter number of row for crosses to be printed: '))

def stars(numCrosses):
  for row in range(0, numCrosses):
    print (' * ', end= ' ')    # show a star, but no new line yet
    for j in range(0, row):
      print (' * ', end= ' ')
    print ( )

stars(numCrosses)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p41.py =========
Enter number of row for crosses to be printed: 5
 *  
 *   *  
 *   *   *  
 *   *   *   *  
 *   *   *   *   *  
'''
