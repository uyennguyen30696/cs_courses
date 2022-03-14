# p52.py
# Uyen Nguyen
# 03/11/22
# Python 3.10.0
# Description:
'''
Program 52:

Create a class Item which has
- instance variables: itemName, itemCost
- class variable: numberItems (gets increased every time a new Item is created)
- a default constructor that allows the user to set itemName and itemCost
( the default constructor sets itemName="apple" itemCost=2.49 if the user does not specify them)
- function to show() the item name and cost
- function to get() and set() the item name and cost

Create a list named groceryBag to store the objects:
- Fill the list with several Item's such as eggs, milk, carrots, bread, apples, each with different price.
- use Item.numberItems to show how many items you have created.
- use a loop to calculate and show the totalCost for all the items in the bag
'''

class Item:
    # Class variable
    numberItems = 0

    # Default constructor
    def __init__(self, newName = 'apple', newCost = 2.49):
        self.itemName = newName
        self.itemCost = newCost

        # Increase every time a new item is added
        Item.numberItems += 1
    
    # Method to show the instance variable item name and cost
    def show(self):
        print ('Item:', self.itemName)
        print ('Cost:', self.itemCost)
        print ('Total item:', Item.numberItems, '\n')
    
    # Method to set/change the instance variable item name and cost
    def setItem(self, newName, newCost):
        self.itemName = newName
        self.itemCost = newCost

    # Method to get the instance variable item name and cost
    def getName(self):
        return self.itemName
    def getCost(self):
        return self.itemCost

# Empty list to store items
groceryBag = []

def add():
  # Create instances of the Item class
  addName = input('Enter an item: ')
  addCost = float(input('How much does it cost? '))
  
  # Call default constructor
  newItem = Item()
  
  newItem.setItem(addName, addCost)
  newItem.show()

  # Add items to the grocery bag
  groceryBag.append(newItem)
  
add()

repeat = input('Do you want to add another item? (y/n) ')
while repeat == 'y' or repeat == 'Y':
  add()
  repeat = input('Do you want to add another item? (y/n) ')

# Calculat total cost
totalCost = 0
for i in range(0, len(groceryBag)):
  totalCost += groceryBag[i].getCost()
print ('Total cost =', totalCost)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_11/p52.py ========
Enter an item: egg
How much does it cost? 3.24
Item: egg
Cost: 3.24
Total item: 1 

Do you want to add another item? (y/n) y
Enter an item: milk
How much does it cost? 5.25
Item: milk
Cost: 5.25
Total item: 2 

Do you want to add another item? (y/n) Y
Enter an item: bread
How much does it cost? 3.50
Item: bread
Cost: 3.5
Total item: 3 

Do you want to add another item? (y/n) n
Total cost = 11.99
'''