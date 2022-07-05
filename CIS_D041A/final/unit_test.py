# Final
# Uyen Nguyen
# 06/12/22
# Python 3.10.0
# Description:
'''
Rewrite midterm using object oriented programming
This unit test file is to test the compute_bill() method of the class Order, including student case and staff case
'''

from order import Order

def test_compute_student_bill():
    print ('TEST STUDENT BILL, enter 1')

    # Order 2x burger #1 (tax rate = 0)
    expected_student_bill = 10.5

    order_again = True

    order = Order()
    order.show_menu()
    order.get_student_or_staff_input()

    print ('\n')

    while order_again:
        order.get_order_inputs()

        # Keep asking the user until he/she chooses the exit option
        exit = input('Press any key to place another order or press 0 to exit. ')
        if exit == '0':
            print ('Thank you. Come back soon!')
            print ('\n')
            order_again = False

    # Student bill
    actual_student_bill = order.compute_bill()

    assert actual_student_bill == expected_student_bill, 'The actual student bill is not the same as the expected student bill'

def test_compute_staff_bill():
    print ('TEST STAFF BILL, enter 2')

    # Order 2x burger #1 (tax rate = 0.09)
    expected_staff_bill = 11.45

    order_again = True

    order = Order()
    order.show_menu()
    order.get_student_or_staff_input()

    print ('\n')

    while order_again:
        order.get_order_inputs()

        # Keep asking the user until he/she chooses the exit option
        exit = input('Press any key to place another order or press 0 to exit. ')
        if exit == '0':
            print ('Thank you. Come back soon!')
            print ('\n')
            order_again = False

    # Staff bill
    actual_staff_bill = order.compute_bill()

    assert actual_staff_bill == expected_staff_bill, 'The actual staff bill is not the same as the expected staff bill'

if __name__ == '__main__':
    test_compute_student_bill()
    test_compute_staff_bill()
    print ('Everything passed')

'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/final/unit_test.py =
TEST STUDENT BILL, enter 1
Welcome to De Anza Grill!


MENU
1 De Anza Burger     5.25
2 Bacon Cheese       5.7
3 Mushroom Swiss     5.95
4 Western Burger     5.95
5 Don Cali Burger    5.95


There is no tax for students and a 9% tax for staff.


To get started, please enter your order, item(s) and quantity, below: 
There is no tax for students and a 9% tax for staff.
Please press 1 if you are a student, press 2 if you are a staff: 1


Please enter the item number to order: 1
Quantity: 2
Press any key to place another order or press 0 to exit. 0
Thank you. Come back soon!


TEST STAFF BILL, enter 2
Welcome to De Anza Grill!


MENU
1 De Anza Burger     5.25
2 Bacon Cheese       5.7
3 Mushroom Swiss     5.95
4 Western Burger     5.95
5 Don Cali Burger    5.95


There is no tax for students and a 9% tax for staff.


To get started, please enter your order, item(s) and quantity, below: 
There is no tax for students and a 9% tax for staff.
Please press 1 if you are a student, press 2 if you are a staff: 2


Please enter the item number to order: 1
Quantity: 2
Press any key to place another order or press 0 to exit. 0
Thank you. Come back soon!


Everything passed
'''
