# Final
# Uyen Nguyen
# 06/12/22
# Python 3.10.0
# Description:
'''
Rewrite midterm using object oriented programming
'''

# from person import Person, Student, Staff


class Order:
    '''
    This Order class stores burger orders and includes methods to handles bill
    '''

    MENU = {
        1: ['De Anza Burger', 5.25],
        2: ['Bacon Cheese', 5.70],
        3: ['Mushroom Swiss', 5.95],
        4: ['Western Burger', 5.95],
        5: ['Don Cali Burger', 5.95],
    }

    # Item code: quantity
    def __init__(self):
        self._stored_input = {
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0
        }

    def show_menu(self):
        '''
        This method greets and shows the menu to the user
        '''

        print ('Welcome to De Anza Grill!')
        print ('\n')
        print ('MENU')

        # Format menu to print, left align for item numbers and items, right align for values
        for item_number, item_and_price in self.MENU.items():
            print (f'{item_number} {item_and_price[0]:<18} {item_and_price[1]}')
        print ('\n')
        print ('There is no tax for students and a 9% tax for staff.')
        print ('\n')
        print ('To get started, please enter your order, item(s) and quantity, below: ')

    def get_student_or_staff_input(self):
        '''
        This method verifies if the user is a student or a staff member
        '''

        self._ask_again = True
        self._is_student = False
        self._is_staff = False

        # Ask the user whether he/she is a student or a staff
        print ('There is no tax for students and a 9% tax for staff.')
        while self._ask_again:
            try:
                self._student_or_staff = input('Please press 1 if you are a student, press 2 if you are a staff: ')
                if self._student_or_staff == '1':
                    self._is_student = True
                    self._ask_again = False
                elif self._student_or_staff == '2':
                    self._is_staff = True
                    self._ask_again = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid input.') 


    def get_order_inputs(self):
        '''
        This method takes order inputs (burger code) from the user and store these info in _stored_input instance variable
        '''

        MIN_NUMBER_ITEM = 1
        MAX_NUMBER_ITEM = 5

        self._current_number_input = 0
        self._current_quantity = 0
        self._valid_number = True
        self._valid_quantity = True

        while self._valid_number:
            try:
                self._current_number_input = int(input('Please enter the item number to order: '))
                if self._current_number_input >= MIN_NUMBER_ITEM and self._current_number_input <= MAX_NUMBER_ITEM:
                    self._valid_number = False
                else:
                    raise ValueError
            except ValueError:
                print ('Please enter a valid item number.')
        # Keep asking the user until a valid quantity is entered
        while self._valid_quantity:
            try:
                self._current_quantity = int(input('Quantity: '))
                if self._current_quantity >= 0:
                    self._valid_quantity = False
                else:
                    print ('Quantiy can\'t be negative.')
            except:
                print ('Please enter a valid whole number.')
        
        # Store user input (item number and quantity) as pairs in a dictionary
        if self._current_number_input not in self._stored_input.keys():
            self._stored_input[self._current_number_input] = self._current_quantity
        else:
            self._stored_input[self._current_number_input] += self._current_quantity

        return self._stored_input

    def compute_bill(self):
        '''
        This method calculate the total prize
        '''
        TAX_RATE_STAFF = 0.09

        self._tax_per_item = 0.00
        self._total_tax = 0.00
        self._price_pre_tax = 0.00
        self._total_pre_tax = 0.00 
        self._total_bill = 0.00
    
        for self._current_number_input, self._current_quantity in self._stored_input.items():
            # Look up the price of each item from the stored input
            self._current_item_price = float(self.MENU[self._current_number_input][1])
            # Price before tax of each item
            self._price_pre_tax = self._current_item_price * self._current_quantity
            self._total_pre_tax += self._price_pre_tax
        
            # No tax for student, and 9% tax for staff
            if self._is_student:
                self._total_bill += round((self._price_pre_tax), 2)
            elif self._is_staff:
                tax_per_item = TAX_RATE_STAFF * self._price_pre_tax
                self._total_tax += tax_per_item
                self._total_bill += round((self._price_pre_tax + tax_per_item), 2)

        return self._total_bill

    def print_bill(self):
        '''
        This method prints the bill with the name, price of each item, and total cost
        '''
        
        print ('Here\'s your receipt')
        # Format the output
        print ('{:<18} {:<10} {:<18}'.format('Item(s)', 'Qty.', 'Price'))

        for self._current_number_input, self._current_quantity in self._stored_input.items():
            # The food items
            self._item_name = self.MENU[self._current_number_input][0]

            self._item_price_each = float(self.MENU[self._current_number_input][1])
            self._item_price_total = self._item_price_each * self._current_quantity

            if self._current_quantity != 0:
                # Print the food items, quantities, and cost of each
                print (f'{self._item_name:<19} {self._current_quantity:<9} {self._item_price_total:<10}')

        print ('-' * 40)
        # The total before tax
        print ('{:<29}'.format('Total before tax'), round(self._total_pre_tax, 2))
        # Tax amount
        print ('{:<29}'.format('Total tax'), round(self._total_tax, 2))
        # Total price after tax
        print ('{:<29}'.format('Total bill'), round(self._total_bill, 2))

    def save_to_file(self):
        '''
        This method save the bill to a different file
        '''

        with open('outputFile.txt', 'w') as self._outputFile:
            self._outputFile.write('Here\'s your receipt \n')
            self._outputFile.write('{:<18} {:<10} {:<18}'.format('Item(s)', 'Qty.', 'Price') + '\n')
            
            for self._current_number_input, self._current_quantity in self._stored_input.items():
                # The food items
                self._item_name = self.MENU[self._current_number_input][0]

                self._item_price_each = float(self.MENU[self._current_number_input][1])
                self._item_price_total = self._item_price_each * self._current_quantity

                if self._current_quantity != 0:
                    # Print the food items, quantities, and cost of each
                    self._outputFile.write(f'{self._item_name:<19} {self._current_quantity:<9} {self._item_price_total:<10}' + '\n')

            self._outputFile.write('-' * 40 + '\n')
            # The total before tax
            self._total_pre_tax_line = str(round(self._total_pre_tax, 2))
            self._outputFile.write('{:<30}'.format('Total before tax') + self._total_pre_tax_line + '\n')
            # Tax amount
            self._total_tax_line = str(round(self._total_tax, 2))
            self._outputFile.write(str('{:<30}'.format('Total tax')) + self._total_tax_line + '\n')
            # Total price after tax
            self._total_bill_line = str(round(self._total_bill, 2))
            self._outputFile.write(str('{:<30}'.format('Total bill')) + self._total_bill_line + '\n')


# class Student_bill(Order):
#     '''
#     This class is an inheritance of the super class Order
#     '''

#     TAX = 0
#     def __init__(self):
#         super().__init__()
#         print ('You are a student')

# class Staff_bill(Order):
#     '''
#     This class is an inheritance of the super class Order
#     '''
    
#     TAX = 0.09
#     def __init__(self):
#         super().__init__()
#         print ('You are a staff member')
