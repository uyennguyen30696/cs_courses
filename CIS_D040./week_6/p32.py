# p32.py
# Uyen Nguyen
# 02/10/22
# Python 3.10.0
# Description:
'''
Program 32:

Write a function multAdd(a,b,c)  that Returns a*b+c.

Write a main() function which calls the multAdd(a,b,c) function.

Pass the three arguments such as 1, 2, 3 from the call in the main()
'''

a = int(input('Enter integer a: '))
b = int(input('Enter integer b: '))
c = int(input('Enter integer c: '))

def multAdd(a, b, c):
  return a * b + c

def main():
  print (multAdd(a, b, c))

main()

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_6/p32.py =========
Enter integer a: 1
Enter integer b: 2
Enter integer c: 3
5
'''