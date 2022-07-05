# ch6_ex1.py
# Uyen Nguyen
# 05/10/22
# Python 3.10.0
# Description:
'''
Lists
Create two lists of your friends that you found in 2017 and 2018. 
Concatenate the two lists and then show to the user.
Ask the user to enter a name of a friend.
Then show that you found the friend in 2017 or 2018, or they don't have any friend with this name in their friends list.
Ask the user to enter a new friend name to be added to 2017 or 2018 lists (Also, you need to ask the user what year they want to add the friend name).
Then append the entered friend name to the related list (2017 or 2018 friend lists)  
Print 2017 friends list and also 2018 friends list on the screen.
'''

friends2017 = ['Levi', 'Eren', 'Mikasa', 'Reiner', 'Armin']
friends2018 = ['Erza', 'Natsu', 'Gray', 'Lucy', 'Mira']

allFriends = friends2017 + friends2018
print ('Friends from 2017 and 2018 are:')
print (*allFriends, sep = ', ')

# Look up a name of a friend
friendInput = input('Look up a name of a friend: ').strip()
if friendInput in friends2017:
    print (friendInput, 'is in the 2017 friend list.')
elif friendInput in friends2018:
    print (friendInput, 'is in the 2018 friend list.')
else:
    print (friendInput, 'is not in 2017 or 2018 friend list. ')
    
# Add a name of a new friend
newFriend = input('Enter the name of a new friend you want to add to your friend list: ').strip()
addYear = input('What year would you like to add this friend name to? ').strip()
if addYear == '2017':
    friends2017.append(newFriend)
elif addYear == '2018':
    friends2018.append(newFriend)

print ('2017 friend list:')
print (*friends2017, sep = ', ')

print ('2018 friend list:')
print (*friends2018, sep = ', ')

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex1.py =====
Friends from 2017 and 2018 are:
Levi, Eren, Mikasa, Reiner, Armin, Erza, Natsu, Gray, Lucy, Mira
Look up a name of a friend: Gray
Gray is in the 2018 friend list.
Enter the name of a new friend you want to add to your friend list: Icy
What year would you like to add this friend name to? 2018
2017 friend list:
Levi, Eren, Mikasa, Reiner, Armin
2018 friend list:
Erza, Natsu, Gray, Lucy, Mira, Icy
'''

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex1.py =====
Friends from 2017 and 2018 are:
Levi, Eren, Mikasa, Reiner, Armin, Erza, Natsu, Gray, Lucy, Mira
Look up a name of a friend: Icy
Icy is not in 2017 or 2018 friend list. 
Enter the name of a new friend you want to add to your friend list: Icy
What year would you like to add this friend name to? 2017
2017 friend list:
Levi, Eren, Mikasa, Reiner, Armin, Icy
2018 friend list:
Erza, Natsu, Gray, Lucy, Mira
'''
