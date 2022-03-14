# p9.py
# Uyen Nguyen
# 01/09/22
# Python 3.10.0
# Description:
'''
Program 9 - User Height Message:

Write a program to compute a person's height and print out a message.

The user will input their height in feet and inches.

The program will convert the feet and inches into total_inches, and then print a message.

If the total inches is greater than 72, the message should be something like, "You're tall."
If the total inches is between 5' and 6', a different message should appear, like "You are average"
If the total inches is less than 60, another message should appear, like "You are vertically challenged"
Save and submit as p9.py
'''

# Ask the user for height, feet and inches
print('Please enter your height: ')
feet = float(input('feet: '))
inches = float(input('inches: '))

# Calculate the total inches
totalInches = feet * 12 + inches

# Show results
print ('%.0f feet %.0f inch(es) = %.0f inches'
       %(    feet,     inches,         totalInches)
      )

# Use relational operators for selection
if totalInches > 72:
    print ('You are tall!')
elif totalInches <= 72 and totalInches >= 60:
    print ('You are average')
elif totalInches < 60:
    print ('You are short')

'''
========== RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_2/p9.py =========
Please enter your height: 
feet: 6
inches: 0
6 feet 0 inch(es) = 72 inches
You are average
'''
