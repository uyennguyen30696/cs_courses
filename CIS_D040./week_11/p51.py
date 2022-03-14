# p51.py
# Uyen Nguyen
# 03/11/22
# Python 3.10.0
# Description:
'''
Program 51:

1) Create a Date class.
1a) The class should have 3 properties (instance variables) 
month
day
year

1b) The class should have 2 actions (functions / methods) :
setDate()  - allows the user to enter a date in 12/31/02 format 
showDate() - displays the date. 

2) Create an instance of the Date class.

3) Test the object's setDate() and showDate() methods.

4) Submit your program code, including the test run at the bottom of your code.
'''

class Date:
    def __init__(self, newMonth = 3, newDay = 11, newYear = 2022):
        self.month = newMonth
        self.day = newDay
        self.year = newYear

    # Method to set/change the instance variables month, day, year
    def setDate(self, newMonth, newDay, newYear):
        self.month = newMonth
        self.day = newDay
        self.year = newYear

    #  Method to display the date
    def show(self):
        print (self.month, '/', self.day, '/', self.year)

# Create instances of the Date class
monthInput = int(input('Enter month: '))
dayInput = int(input('Enter day: '))
yearInput = int(input('Enter year: '))

# Call default constructor
today = Date()

today.setDate(monthInput, dayInput, yearInput)
today.show()

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_11/p51.py ========
Enter month: 6
Enter day: 30
Enter year: 1996
6 / 30 / 1996
'''
