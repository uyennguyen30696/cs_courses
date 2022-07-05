# ch2_ex3.py
# Uyen Nguyen
# 04/18/22
# Python 3.10.0
# Description:
'''
Write a program which prompts the user to enter the
    width
    height of the graphics window
    The radius of a circle
    outline color and
    fill color of the circle
 
Then draws the circle at the center of the graphics window and prints out 
    the circumference and
    the area of the circle.
'''

from ezgraphics import GraphicsWindow
from colour import Color   # In terminal, run 'pip3 install colour'
import math

# Only accept user input as number
def input_isNum(prompt):
    repeat = True
    while repeat:
        input_value = input(prompt)
        try:
            input_value = float(input_value)
            if input_value > 0:
                repeat = False
                return input_value
            else:
                print ('Error! Please enter a positive number!')
        except:
            print ('Error! Please enter a numeric value only!')

# Only accept user input as valid color
def input_isColor(prompt):
    repeat = True
    while repeat:
        input_value = input(prompt)
        try:
            input_value = input_value.replace(' ', '')   # Color does not count space as valid color (ex: dark green = darkgreen)
            if Color(input_value):
                return input_value
        except:
            print ('Error! Please enter a valid color!')

# Get input from user
user_name = input('Please enter your name: ')

width = input_isNum('Graphics window width = ')
height = input_isNum('Graphics window height = ')
radius_circle = input_isNum('Circle radius = ')

outlineColor = input_isColor('Outline color: ')
fillColor = input_isColor('Fill color: ')

# Create the window and access the canvas
win = GraphicsWindow(width, height)
canvas = win.canvas()

# Title of the canvas window
win.setTitle("CIS41A - Ch2 Ex3")

# Print the name of user on the canvas window
# canvas.setTextAnchor("nw")  # "nw" = north-west
canvas.setTextFont('arial', 'bold', 30)
canvas.drawText(50, 50, 'From ' + user_name + ' with ❤️')

# Set outline and fill circle color
canvas.setOutline(outlineColor)
canvas.setLineWidth(10)
canvas.setFill(fillColor)

# Calculate starting point (x, y) to position the circle in the middle of the window
diameter_circle = radius_circle * 2
x = width / 2 - radius_circle
y = height / 2 - radius_circle

# Draw the circle on canvas in the middle of the graphics window
canvas.drawOval(x, y, diameter_circle, diameter_circle)

# Calculate the circumference and area of the circle
circumference = round((2 * math.pi * radius_circle), 2)
area = round(math.pi * (radius_circle ** 2), 2)
print ('Circle circumference =', circumference)
print ('Circle area =', area)

# Wait for the user to close the window
win.wait()

'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/exercises/ch2_exercise_3.py
Please enter your name: Uyen
Graphics window width = 800
Graphics window height = test
Please enter a number only!
Graphics window height = number
Please enter a number only!
Graphics window height = 700
Circle radius = 150
Outline color: Blac
Please enter a valid color!
Outline color: black
Fill color: hot pink
Circle circumference = 942.48
Circle area = 70685.83

Please enter your name: Uyen
Graphics window width = 850
Graphics window height = 750
Circle radius = 200
Outline color: olive
Fill color: light green
Circle circumference = 1256.64
Circle area = 125663.71
'''
