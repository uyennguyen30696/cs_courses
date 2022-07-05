# midterm.py
# Uyen Nguyen
# 05/06/22
# Python 3.10.0
# Description:
'''
Write a menu-driven program for De Anza College Food Court.
    Display the food menu to a user (5 options with names and prices).
    Use numbers for the options and example "6" to exit.
    Ask the user what he/she wants and how many of it.
    Keep asking the user until he/she chooses the exit option.

    Calculate the price.
    Ask the user whether he/she is a student or a staff. There is no tax for students and a 9% tax for staff. Add the tax price to the total price.
    Display the bill to the user. The bill includes:
        The food items
        The quantities
        The cost of them
        The total before tax
        Tax amount
        Total price after tax
'''

# Store menu in a dictionary
MENU = {
    1: ['De Anza Burger', '5.25'],
    2: ['Bacon Cheese', '5.70'],
    3: ['Mushroom Swiss', '5.95'],
    4: ['Western Burger', '5.95'],
    5: ['Don Cali Burger', '5.95'],
}
MIN_NUMBER_ITEM = 1
MAX_NUMBER_ITEM = 5
TAX_RATE_STAFF = 0.09

# Display the food menu to user 
def show_menu():
    print ('Welcome to De Anza Grill!')
    print ('\n')
    print ('MENU')

    # Format menu to print, left align for item numbers and items, right align for values
    for item_number, item_and_price in MENU.items():
        print (f'{item_number} {item_and_price[0]:<18} {item_and_price[1]}')
    print ('\n')

# Ask the user what he/she wants, how many of it, and store the input as pairs (item number, quantity)
def get_inputs():
    stored_input = {}    # {current_number_input: current_quantity}
    is_student = False
    is_staff = False
    ask_again = True
    order_again = True

    # Ask the user whether he/she is a student or a staff
    print ('There is no tax for students and a 9% tax for staff.')
    while ask_again:
        try:
            student_or_staff = input('Please press 1 if you are a student, press 2 if you are a staff: ')
            if student_or_staff == '1':
                is_student = True
                ask_again = False
            elif student_or_staff == '2':
                is_staff = True
                ask_again = False
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid input.')

    print ('\n')
    print ('To get started, please enter your order, item(s) and quantity, below: ')
    while order_again:
        current_number_input = 0
        current_quantity = 0
        valid_number = True
        valid_quantity = True

        # Keep asking the user until a valid item number is entered
        while valid_number:
            try:
                current_number_input = int(input('Please enter the item number to order: '))
                if current_number_input >= MIN_NUMBER_ITEM and current_number_input <= MAX_NUMBER_ITEM:
                    valid_number = False
                else:
                    raise ValueError
            except ValueError:
                print ('Please enter a valid item number.')
        # Keep asking the user until a valid quantity is entered
        while valid_quantity:
            try:
                current_quantity = int(input('Quantity: '))
                if current_quantity >= 0:
                    valid_quantity = False
                else:
                    print ('Quantiy can\'t be negative.')
            except:
                print ('Please enter a valid whole number.')
              
        # Keep asking the user until he/she chooses the exit option
        exit = input('Press any key to add another item or press 0 to exit. ')
        if exit == '0':
            print ('Thank you. Come back soon!')
            print ('\n')
            order_again = False

        # Store user input (item number and quantity) as pairs in a dictionary
        if current_number_input not in stored_input.keys():
            stored_input[current_number_input] = current_quantity
        else:
            stored_input[current_number_input] += current_quantity

    return is_student, is_staff, stored_input

# Calculate the price
def compute_bill(is_student, is_staff, stored_input):
    tax_per_item = 0.00
    total_tax = 0.00
    price_pre_tax = 0.00
    total_pre_tax = 0.00    
    total_bill = 0.00
  
    for current_number_input, current_quantity in stored_input.items():
        # Look up the price of each item from the stored input
        current_item_price = float(MENU[current_number_input][1])
        # Price before tax of each item
        price_pre_tax = current_item_price * current_quantity
        total_pre_tax += price_pre_tax
      
        # No tax for student, and 9% tax for staff
        if is_student:
            total_bill += round((price_pre_tax), 2)
        elif is_staff:
            tax_per_item = TAX_RATE_STAFF * price_pre_tax
            total_tax += tax_per_item
            total_bill += price_pre_tax + tax_per_item

    return total_pre_tax, total_tax, total_bill

# Display the bill to the user
def print_bill(stored_input, total_pre_tax, total_tax, total_bill):
    print ('Here\'s your receipt')
    # Format the output
    print ('{:<18} {:<10} {:<18}'.format('Item(s)', 'Qty.', 'Price'))

    for current_number_input, current_quantity in stored_input.items():
        # The food items
        item_name = MENU[current_number_input][0]

        item_price_each = float(MENU[current_number_input][1])
        item_price_total = item_price_each * current_quantity

        # Print the food items, quantities, and cost of each
        print (f'{item_name:<19} {current_quantity:<9} {item_price_total:<10}')

    print ('-' * 40)
    # The total before tax
    print ('{:<29}'.format('Total before tax'), round(total_pre_tax, 2))
    # Tax amount
    print ('{:<29}'.format('Total tax'), round(total_tax, 2))
    # Total price after tax
    print ('{:<29}'.format('Total bill'), round(total_bill, 2))

def main():
    show_menu()

    student_validate, staff_validate, the_stored_input = get_inputs()
    the_total_pre_tax, the_total_tax, the_bill = compute_bill(student_validate, staff_validate, the_stored_input)
    print_bill(the_stored_input, the_total_pre_tax, the_total_tax, the_bill)
  
if __name__ == "__main__":
    main()

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/midterm.py =====
Welcome to De Anza Grill!


MENU
1 De Anza Burger     5.25
2 Bacon Cheese       5.70
3 Mushroom Swiss     5.95
4 Western Burger     5.95
5 Don Cali Burger    5.95


There is no tax for students and a 9% tax for staff.
Please press 1 if you are a student, press 2 if you are a staff: 3
Please enter a valid input.
Please press 1 if you are a student, press 2 if you are a staff: 1


To get started, please enter your order, item(s) and quantity, below: 
Please enter the item number to order: one
Please enter a valid item number.
Please enter the item number to order: 7
Please enter a valid item number.
Please enter the item number to order: -1
Please enter a valid item number.
Please enter the item number to order: 1
Quantity: 2.5
Please enter a valid whole number.
Quantity: -2
Quantiy can't be negative.
Quantity: two
Please enter a valid whole number.
Quantity: 2
Press any key to add another item or press 0 to exit. k
Please enter the item number to order: three
Please enter a valid item number.
Please enter the item number to order: 3
Quantity: 4
Press any key to add another item or press 0 to exit. n
Please enter the item number to order: 5
Quantity: 2
Press any key to add another item or press 0 to exit. 0
Thank you. Come back soon!


Here's your receipt
Item(s)            Qty.       Price             
De Anza Burger      2         10.5      
Mushroom Swiss      4         23.8      
Don Cali Burger     2         11.9      
----------------------------------------
Total before tax              46.2
Total tax                     0.0
Total bill                    46.2
'''

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/midterm.py =====
Welcome to De Anza Grill!


MENU
1 De Anza Burger     5.25
2 Bacon Cheese       5.70
3 Mushroom Swiss     5.95
4 Western Burger     5.95
5 Don Cali Burger    5.95


There is no tax for students and a 9% tax for staff.
Please press 1 if you are a student, press 2 if you are a staff: 2


To get started, please enter your order, item(s) and quantity, below: 
Please enter the item number to order: 4
Quantity: 1
Press any key to add another item or press 0 to exit. n
Please enter the item number to order: 2
Quantity: 8
Press any key to add another item or press 0 to exit. n
Please enter the item number to order: 2
Quantity: 3
Press any key to add another item or press 0 to exit. 0
Thank you. Come back soon!


Here's your receipt
Item(s)            Qty.       Price             
Western Burger      1         5.95      
Bacon Cheese        11        62.7      
----------------------------------------
Total before tax              68.65
Total tax                     6.18
Total bill                    74.83
'''