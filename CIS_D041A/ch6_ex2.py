# ch6_ex2.py
# Uyen Nguyen
# 05/10/22
# Python 3.10.0
# Description:
'''
Dictionaries
Create a dictionary of your friends that you found in 2017 and 2018. So, the keys are '2017' and '2018
Print the friend's name
Ask the user to enter a name of the friends.
Then show the friend you found in 2017 or 2018.
Ask the user to add a new friend name to 2017 or 2018 lists (You need also to ask the user what year they want to add the friend name).
Then add the entered friend name to the dictionary(2017 or 2018  value)  
Print the friends' dictionary on the screen.
'''

friendsList = {
    '2017': ['Levi', 'Eren', 'Mikasa', 'Reiner', 'Armin'],
    '2018': ['Erza', 'Natsu', 'Gray', 'Lucy', 'Mira']
}

# Print the friends' name
for year, friends in friendsList.items():
    print (year)
    print (*friends, sep = ', ')

# Look up a name of a friend
friendInput = input('Look up a name of a friend: ').strip()
if friendInput in friendsList['2017']:
    print (friendInput, 'is in the 2017 friend list.')
elif friendInput in friendsList['2018']:
    print (friendInput, 'is in the 2018 friend list.')
else:
    print (friendInput, 'is not in 2017 or 2018 friend list. ')
    
# Add a name of a new friend
newFriend = input('Enter the name of a new friend you want to add to your friend list: ').strip()
addYear = input('What year would you like to add this friend name to? ').strip()
if addYear == '2017':
    friendsList['2017'].append(newFriend)
elif addYear == '2018':
    friendsList['2018'].append(newFriend)
    
# Print the friends' name after updated
for year, friends in friendsList.items():
    print (year)
    print (*friends, sep = ', ')

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex2.py =====
2017
Levi, Eren, Mikasa, Reiner, Armin
2018
Erza, Natsu, Gray, Lucy, Mira
Look up a name of a friend: Mikasa
Mikasa is in the 2017 friend list.
Enter the name of a new friend you want to add to your friend list: Icy
What year would you like to add this friend name to? 2018
2017
Levi, Eren, Mikasa, Reiner, Armin
2018
Erza, Natsu, Gray, Lucy, Mira, Icy
'''

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex2.py =====
2017
Levi, Eren, Mikasa, Reiner, Armin
2018
Erza, Natsu, Gray, Lucy, Mira
Look up a name of a friend: Icy
Icy is not in 2017 or 2018 friend list. 
Enter the name of a new friend you want to add to your friend list: Icy
What year would you like to add this friend name to? 2017
2017
Levi, Eren, Mikasa, Reiner, Armin, Icy
2018
Erza, Natsu, Gray, Lucy, Mira
'''