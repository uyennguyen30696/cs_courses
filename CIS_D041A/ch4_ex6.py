# ch4_ex6.py
# Uyen Nguyen
# 04/26/22
# Python 3.10.0
# Description:
'''
Ask the user to enter an email address.
Check that it is a valid email address => it should have "@"  and "."  (for example: if '@' and '.' in user_input:      )
Find the domain name of the email address and print it
'''

# Plan
# Count the number of '@', should have only 1
# No white space in prefix and domain
# Must contain a minimum of one '.' in the domain (after '@')
# Keep asking user until a valid email address is entered
# Find the domain name: a substring after the '@' and before the '.'

repeat = True
while repeat:
    email = input('Please enter a valid email address: ')
    try:
        # List of valid conditions
        one_at_sign = False         # Only one '@' sign
        index_at_sign = -1
        one_dot_minimum = False     # Minimum one '.'
        index_dot = -1
        dot_after_at_sign = False   # Minimum one '.' must be after the '@' sign
        no_white_space = True       # No white space
        
        count_at_sign = 0           # Count '@' symbol
        count_dot = 0               # Count '.'
        
        domain = ''                 # Substring right after '@' and before '.'
        
        for character in email:
            if character == '@':
                count_at_sign += 1 
                index_at_sign = email.find(character)
            if character == '.':
                count_dot += 1
                index_dot = email.rfind(character)   # Last occurence of '.'
            if character == ' ':
                no_white_space = False
              
        # Count the number of '@', should have only 1  
        if count_at_sign == 1:
            one_at_sign = True
        # Must contain a minimum of one '.' in the domain (after '@')
        if count_dot >= 1:
            one_dot_minimum = True
        if index_dot > index_at_sign:
          dot_after_at_sign = True
        
        # If the email is valid, find the domain
        if (one_at_sign == True 
            and one_dot_minimum == True
            and dot_after_at_sign == True
            and no_white_space == True):
                print ('Your email address is valid.')
                domain = email[index_at_sign+1:index_dot]
                print ('Domain:', domain)
                repeat = False
    except:
        print ('Please enter a valid email address.')
                 
'''
= RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/exercises/ch4_exercise_6.py
Please enter a valid email address: uyen
Please enter a valid email address: Uyen@gmail@com
Please enter a valid email address: uyen.nguyen@gmail
Please enter a valid email address: uyen.nguyen88@gmail.com
Your email address is valid.
Domain: gmail

Please enter a valid email address: UYEN08
Please enter a valid email address: UYEN08@example
Please enter a valid email address: UYEN+08@example.edu
Your email address is valid.
Domain: example
'''
