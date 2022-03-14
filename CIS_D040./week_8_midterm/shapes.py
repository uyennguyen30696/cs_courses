# p45.py
# Uyen Nguyen
# 02/24/22
# Python 3.10.0
# Description:
'''
A quadrilateral is a shape with 4 sides and 4 angles.

Write a program that lets the user enter 4 sides and 4 angles into LISTS.
The program checks if the type of quadrilateral is either: 
- Rhombus
- Square
- Rectangle

1)  Input, Validation, Repetition (30 pts) :
 a) The user enters 4 sides into a LIST of type float. (5pts)
 b) The user enters 4 angles into a LIST of type float. (5pts)
 c) The program validates that all 8 numbers are positive. (10pts)
 e) The program can repeat if user choses to. (10pts)

2)  Use the LISTS to identify the Type of Quadrilateral (30 pts) :
 a) Rhombus (all 3 must be true) (10 pts): 
  1. All four sides have the same length. 
  2. Angle 1 equals Angle 3 
  3. Angle 2 equals Angle 4 

 b) Square (both must be true) (10 pts):
  1. All four sides have the same length.
  2. All angles are equal to each other

 c) Rectangle (all 3 must be true) (10 pts):
  1. Side 1 equals Side 3
  2. Side 2 equals Side 4
  3. All angles are equal to each other
'''

sideList = []
angleList = []

# Use the LISTS to identify the Type of Quadrilateral
def isRhombus(side0, side1, side2, side3, angle0, angle1, angle2, angle3):
  # Rhombus (all 3 must be true): 
  # 1. All four sides have the same length. 
  cond1 = False
  # 2. Angle 1 equals Angle 3 
  cond2 = False
  # 3. Angle 2 equals Angle 4 
  cond3 = False
  # 4. Adjacent angles are not equal to each other (to distinguish with square)
  cond4 = False
  
  if side0 == side1 == side2 == side3:
    cond1 = True
  if angle0 == angle2:
    cond2 = True
  if angle1 == angle3:
    cond3 = True
  if angle0 != angle1 and angle2 != angle3:
    cond4 = True

  if cond1 == True and cond2 == True and cond3 == True and cond4 == True:
    return True

# Square (both must be true):
def isSquare(side0, side1, side2, side3, angle0, angle1, angle2, angle3): 
  # 1. All four sides have the same length
  cond1 = False
  # 2. All angles are equal to each other
  cond2 = False
  # 3. All angles are positive and = 90 (positive values are validated in the while loop below)
  cond3 = False
  
  if side0 == side1 == side2 == side3:
    cond1 = True
  if angle0 == angle1 == angle2 == angle3:
    cond2 = True
  if angle0 == 90 and angle1 == 90 and angle2 == 90 and angle3 == 90:
    cond3 = True

  if cond1 == True and cond2 == True and cond3 == True:
    return True

# Rectangle (all 3 must be true):
def isRectangle(side0, side1, side2, side3, angle0, angle1, angle2, angle3):
  # 1. Side 1 equals Side 3
  cond1 = False
  # 2. Side 2 equals Side 4 
  cond2 = False
  # 3. All angles are equal to each other 
  cond3 = False
  # 4. All four sides don't have the same length (to distinguish with square)
  cond4 = False
  # 5. All angles are positive and = 90 (positive values are validated in the while loop below)
  cond5 = False
  
  if side0 == side2:
    cond1 = True
  if side1 == side3:
    cond2 = True
  if angle0 == angle1 == angle2 == angle3:
    cond3 = True
  if side0 != side1 != side2 != side3:
    cond4 = True
  if angle0 == 90 and angle1 == 90 and angle2 == 90 and angle3 == 90:
    cond5 = True

  if cond1 == True and cond2 == True and cond3 == True and cond4 == True and cond5 == True:
    return True

repeat = 'y'
while repeat == 'y' or repeat == 'Y':
  sideList = []
  angleList = []

  # Ask user to enter 4 sides
  for i in range(1, 5):
    sides = float(input('Please enter side %i: ' %i))
    if sides > 0:
      sideList.append(sides)
    while sides <= 0:
      print ('Value must be positive!', end=' ')
      sides = float(input('Please enter side %i: ' %i))
      if sides > 0:
        sideList.append(sides)
  
  # Ask uer to enter 4 angles
  for i in range(1, 5):
    angles = float(input('Please enter angle %i: ' %i))
    if angles > 0:
      angleList.append(angles)
    while angles <= 0:
      print ('Value must be positive!', end=' ')
      angles = float(input('Please enter angle %i: ' %i))
      if angles > 0:
        angleList.append(angles)
  
  # Print results
  if (angleList[0] + angleList[1] + angleList[2] + angleList[3]) > 360:
    print ('Invalid values. Can not form a a shape. Sum of all angles must be 360. \n')
  else :
    if isRhombus(sideList[0], sideList[1], sideList[2], sideList[3], angleList[0], angleList[1], angleList[2], angleList[3]):
      print ('This is a RHOMBUS! \n')
    elif isSquare(sideList[0], sideList[1], sideList[2], sideList[3], angleList[0], angleList[1], angleList[2], angleList[3]):
      print ('This is a SQUARE! \n')
    elif isRectangle(sideList[0], sideList[1], sideList[2], sideList[3], angleList[0], angleList[1], angleList[2], angleList[3]):
      print ('This is a RECTANGLE! \n')
    else:
      print ('Not a rhombus, square, or rectangle \n')

  repeat = input('Would you like to repeat? (y)(n): ')
  
  # Prevent other keys rather than y or n are pressed
  while repeat != 'y' and repeat != 'Y' and repeat != 'n':
    repeat = input('Would you like to repeat? (y)(n): ')
    if repeat == 'y' or repeat == 'Y':
      print ('Here we go again...')

'''
==== RESTART: /Users/uyennguyen/Documents/CIS_D040./week_8_midterm/shapes.py ===
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: 1
Please enter side 4: 1
Please enter angle 1: 60
Please enter angle 2: 120
Please enter angle 3: 60
Please enter angle 4: 120
This is a RHOMBUS! 

Would you like to repeat? (y)(n): y
Please enter side 1: -2
Value must be positive! Please enter side 1: 2
Please enter side 2: 2
Please enter side 3: 2
Please enter side 4: 2
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: 90
Please enter angle 4: 90
This is a SQUARE! 

Would you like to repeat? (y)(n): Y
Please enter side 1: 1
Please enter side 2: 2
Please enter side 3: 1
Please enter side 4: 2
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: 90
Please enter angle 4: 90
This is a RECTANGLE! 

Would you like to repeat? (y)(n): y
Please enter side 1: 1
Please enter side 2: 2
Please enter side 3: 3
Please enter side 4: 5
Please enter angle 1: 80
Please enter angle 2: 100
Please enter angle 3: 30
Please enter angle 4: 150
Not a rhombus, square, or rectangle 

Would you like to repeat? (y)(n): Y
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: 1
Please enter side 4: 1
Please enter angle 1: 60
Please enter angle 2: 130
Please enter angle 3: 60
Please enter angle 4: 130
Invalid values. Can not form a a shape. Sum of all angles must be 360.

Would you like to repeat? (y)(n): c
Would you like to repeat? (y)(n): n

'''