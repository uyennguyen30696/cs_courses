# p45.py
# Uyen Nguyen
# 02/23/22
# Python 3.10.0
# Description:
'''
Program 45:

Write a program that calculates and shows all prime numbers between 3 - 100.

Prime numbers can only be evenly (remainder 0) divided by itself and 1.
'''

for i in range(3, 101):
    for j in range(2, i):
        if i % j == 0:
            print (i, 'is not a prime')
            break
        elif i % j != 0 and j == i - 1:
            print (i, 'is a prime')

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_7/p45.py =========
3 is a prime
4 is not a prime
5 is a prime
6 is not a prime
7 is a prime
8 is not a prime
9 is not a prime
10 is not a prime
11 is a prime
12 is not a prime
13 is a prime
14 is not a prime
15 is not a prime
16 is not a prime
17 is a prime
18 is not a prime
19 is a prime
20 is not a prime
21 is not a prime
22 is not a prime
23 is a prime
24 is not a prime
25 is not a prime
26 is not a prime
27 is not a prime
28 is not a prime
29 is a prime
30 is not a prime
31 is a prime
32 is not a prime
33 is not a prime
34 is not a prime
35 is not a prime
36 is not a prime
37 is a prime
38 is not a prime
39 is not a prime
40 is not a prime
41 is a prime
42 is not a prime
43 is a prime
44 is not a prime
45 is not a prime
46 is not a prime
47 is a prime
48 is not a prime
49 is not a prime
50 is not a prime
51 is not a prime
52 is not a prime
53 is a prime
54 is not a prime
55 is not a prime
56 is not a prime
57 is not a prime
58 is not a prime
59 is a prime
60 is not a prime
61 is a prime
62 is not a prime
63 is not a prime
64 is not a prime
65 is not a prime
66 is not a prime
67 is a prime
68 is not a prime
69 is not a prime
70 is not a prime
71 is a prime
72 is not a prime
73 is a prime
74 is not a prime
75 is not a prime
76 is not a prime
77 is not a prime
78 is not a prime
79 is a prime
80 is not a prime
81 is not a prime
82 is not a prime
83 is a prime
84 is not a prime
85 is not a prime
86 is not a prime
87 is not a prime
88 is not a prime
89 is a prime
90 is not a prime
91 is not a prime
92 is not a prime
93 is not a prime
94 is not a prime
95 is not a prime
96 is not a prime
97 is a prime
98 is not a prime
99 is not a prime
100 is not a prime
'''
