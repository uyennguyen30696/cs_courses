# # Uyen Nguyen
# # 01/15/22
# # Python 3.10.0
# # Description: Week 4 discussion
# '''
# Use this week's material to write a for loop that happens as many times as the current hour.
# For example, if the current time is 10:38pm, then the loop happens 10 times:

# for i in range(1, 11, 1):
#    print("i = " , i)
# Reply to one of your classmates by rewriting their for loop using a while loop
# For example:

# i = 1
# while i < 11:
#    print("i = " , i)
#    i+=1
# '''

# # Current time: 10:01pm
# num = 0
# for i in range(1, 11, 1):
#     num += 1
#     print ('Num %2i =' %i, num)

# '''
# === RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/week4_discussion.py ==
# Num  1 = 1
# Num  2 = 2
# Num  3 = 3
# Num  4 = 4
# Num  5 = 5
# Num  6 = 6
# Num  7 = 7
# Num  8 = 8
# Num  9 = 9
# Num 10 = 10
# '''

# What hour is it in 24 hour format?

# The for loop that happens "Hour" times
# for i in range(1, 11, 1):
#    print("i = " , i)

# i = 1
# while i < 11:
#    print("i = " , i)
#    i += 1

from datetime import datetime
# Get current date and time
now = datetime.now()

# What hour is it in 24 hour format?
Hour = now.hour
print ("Hour:", Hour)
print (" ")

# The for loop that happens "Hour" times
i = 1
while i < Hour + 1:
   print("i = " , i)
   i += 1

'''
=== RESTART: /Users/uyennguyen/Documents/CIS_D040./week_5/week4_discussion.py ==
Hour: 22
 
i =  1
i =  2
i =  3
i =  4
i =  5
i =  6
i =  7
i =  8
i =  9
i =  10
i =  11
i =  12
i =  13
i =  14
i =  15
i =  16
i =  17
i =  18
i =  19
i =  20
i =  21
i =  22
'''