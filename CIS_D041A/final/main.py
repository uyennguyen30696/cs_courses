# Final
# Uyen Nguyen
# 06/12/22
# Python 3.10.0
# Description:
'''
Rewrite midterm using object oriented programming
'''

from order import Order

def main():
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
    
    order.compute_bill()
    order.print_bill()
    order.save_to_file()

if __name__ == '__main__':
    main()

'''
==== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/final/main.py ===
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
Please press 1 if you are a student, press 2 if you are a staff: 3
Please enter a valid input.
Please press 1 if you are a student, press 2 if you are a staff: one
Please enter a valid input.
Please press 1 if you are a student, press 2 if you are a staff: 1


Please enter the item number to order: two
Please enter a valid item number.
Please enter the item number to order: -2
Please enter a valid item number.
Please enter the item number to order: 2
Quantity: three
Please enter a valid whole number.
Quantity: -3
Quantiy can't be negative.
Quantity: 3
Press any key to place another order or press 0 to exit. y
Please enter the item number to order: 4
Quantity: 2
Press any key to place another order or press 0 to exit. y
Please enter the item number to order: 1
Quantity: 6
Press any key to place another order or press 0 to exit. 0
Thank you. Come back soon!


Here's your receipt
Item(s)            Qty.       Price             
De Anza Burger      6         31.5      
Bacon Cheese        3         17.1      
Western Burger      2         11.9      
----------------------------------------
Total before tax              60.5
Total tax                     0.0
Total bill                    60.5
'''

'''
==== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/final/main.py ===
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


Please enter the item number to order: 4
Quantity: 2
Press any key to place another order or press 0 to exit. y
Please enter the item number to order: 2
Quantity: 4
Press any key to place another order or press 0 to exit. 0
Thank you. Come back soon!


Here's your receipt
Item(s)            Qty.       Price             
Bacon Cheese        4         22.8      
Western Burger      2         11.9      
----------------------------------------
Total before tax              34.7
Total tax                     3.12
Total bill                    37.82
'''