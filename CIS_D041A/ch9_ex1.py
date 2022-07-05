# ch9_ex1
# Uyen Nguyen
# 06/01/22
# Python 3.10.0
# Description:
'''
Change the "rate-hours" exercise before based on object-oriented programming
'''

class PayClass:
    HOUR_PER_WEEK = 40
    OVERTIME = 1.5
    name = ''
    def __init__(self, theName):
        self.name = theName
        print('The object', theName, 'has been created!')
    def getInputs(self):
        self.rate = float(input('Enter the rate: '))
        self.hours = float(input('Enter the hours: '))
        print ('Rate per hour:', self.rate)
        print ('Hours:', self.hours)
 
pay1 = PayClass('Jimmy')
pay1.getInputs()
pay2 = PayClass('Jeniffer')
pay2.getInputs()

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch9_ex1.py =====
The object Jimmy has been created!
Enter the rate: 20.5
Enter the hours: 35
Rate per hour: 20.5
Hours: 35.0
The object Jeniffer has been created!
Enter the rate: 32
Enter the hours: 45
Rate per hour: 32.0
Hours: 45.0
'''