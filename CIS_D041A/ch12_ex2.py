# ch12_ex2
# Uyen Nguyen
# 06/12/22
# Python 3.10.0
# Description:
'''
Write a Python program to create Fibonacci numbers (1, 1, 2, 3, 5, 8, etc.) using an iterator and a generator (Both)
'''

def fib(n):
    current, next = 0, 1
    counter = 0
    while counter <= n:
        yield current
        current, next = next, current + next
        counter += 1

f = fib(7)
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch12_ex2.py ====
0
1
1
2
3
5
8
'''
