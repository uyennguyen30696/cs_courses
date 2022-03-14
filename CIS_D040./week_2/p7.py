# p7.py
# Uyen Nguyen
# 01/09/22
# Python 3.10.0
# Description:
'''
Program 7 - Circumference and Area of a Circle:

Circumference & Area of a Circle
Write a program to compute the circumference and area of a circle.
The user will input the radius of a circle.
Validate Input: Make sure that the radius is positive, or give an error message.
The program will show the circumference and area of a circle with that radius.
The answers should be rounded to the nearest tenth.

Program should run as shown:
What is the radius (in inches) of the circle you want to draw?  12
A circle with radius 12 inches has
circumference:   75.4 inches
area:   452.4 sq. inches

Algorithm
Use 3.1415 as the value of PI.
Enter radius
Circumference of a Circle = 2 * PI * R
Area of a Circle = PI * R*R
'''

# Define variable PI
PI = 3.1415
# Ask the user to enter radius
radius = float(input('Enter radius: '))

# Validate input
if radius < 0:
    print('error, radius can not be negative')
else:  
    # Calculate area
    area = PI * radius * radius
    # Calculate circumference
    circumferance = 2 * PI * radius

# Show results
    print ('A circle with radius %.1f inches has ' %radius)
    print ('Area: %.1f square inches' %area)
    print ('Circumference: %.1f inches' %circumferance)

'''
========== RESTART: /Users/uyennguyen/Documents/CIS_D040A/week_2/p7.py =========
Enter radius: 3
A circle with radius 3.0 inches has 
Area: 28.3 square inches
Circumference: 18.8 inches
'''
