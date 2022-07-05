# Final
# Uyen Nguyen
# 06/12/22
# Python 3.10.0
# Description:
'''
Rewrite midterm using object oriented programming
'''

class Person:
    '''
    This Person class categorizes the user into Student or Staff based on their input answer
    '''
    def __init__(self):
        self._ask_again = True
        self._is_student = False
        self._is_staff = False

        # Ask the user whether he/she is a student or a staff
        print ('There is no tax for students and a 9% tax for staff.')
        while self._ask_again:
            try:
                student_or_staff = input('Please press 1 if you are a student, press 2 if you are a staff: ')
                if student_or_staff == '1':
                    self._is_student = True
                    self._ask_again = False
                elif student_or_staff == '2':
                    self._is_staff = True
                    self._ask_again = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid input.')
        
        return self._is_student, self._is_staff

class Student(Person):
    '''
    This Student class is an inheritant of Person class
    '''
    def __init__(self):
        super().__init__()
    
    def is_student(self):
        self._student = super()._is_student
        self._tax = 0
        print ('You are a student')
        return self._student

class Staff(Person):
    '''
    This Staff class is an inheritant of Person class
    '''
    def __init__(self):
        super().__init__()
    
    def is_staff(self):
        self._staff = super()._is_staff
        self._tax = 0.09
        print ('You are a staff member')
        return self._staff
