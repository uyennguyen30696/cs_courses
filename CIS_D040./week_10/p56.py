# p56.py
# Uyen Nguyen
# 03/06/22
# Python 3.10.0
# Description:
'''
Program 56:
The Caesar Cipher

In this cipher, you encrypt a message by taking each letter in the message and replacing it with a "shifted" letter.

1. Type and run a given program
2. You are given the encrypted sentence: CLGUBA VF TERNG
Using a Shift of 13, what is the original (decyphered) message?
'''

# 1. Type and run a given program

# Write a loop to show the 'Original Alphabet'
alphabet = ''
for i in range (65, 91):
    alphabet += chr(i)
print ('Alphabet = ', alphabet)

# shift = 3
shift = 13
# Show the shift 'key'
print ('Shift = ', shift, 'letters')

# Write a loop to show alphabet shifted by 3
encrypted = ''
for i in range (65, 91):
    if i + shift < 91:
        encrypted += chr(i + shift)
    if i + shift >= 91:
        encrypted += chr(65 + (i + shift - 91))

# Shoe encrypted alphabet
print ('encrypted = ', encrypted)

encrypt = {}        # Make an empty dictionary
decypher = {}
encrypt[' '] = ' '   # Add to dictionary
decypher[' '] = ' '
#         ^^Key ^^Value associated with key

for i in range (0, len(alphabet)):
    encrypt[alphabet[i]] = encrypted[i]
    decypher[encrypted[i]] = alphabet[i]

original_message = "HELLO WORLD"
encrypted_message = ' '

for i in range (0, len(original_message)):
    if original_message[i] == ' ':
        encrypted_message += ' '
    else:
        encrypted_message += encrypt[original_message[i]]

print ('Original sentence: ', original_message)   # HELLO WORLD
print ('Encrypted sentence: ', encrypted_message)
print ('... decyphered: ', end='')
for i in range (0, len(encrypted_message)):
    print (decypher[encrypted_message[i]], end='')

print ('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 2. You are given the encrypted sentence: CLGUBA VF TERNG

# Using a Shift of 13, what is the original (decyphered) message?


'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_10/p56.py ========
Alphabet =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Shift =  3 letters
encrypted =  DEFGHIJKLMNOPQRSTUVWXYZABC
Original sentence:  HELLO WORLD
Encrypted sentence:   KHOOR ZRUOG
... decyphered:  HELLO WORLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alphabet =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Shift =  13 letters
encrypted =  NOPQRSTUVWXYZABCDEFGHIJKLM
Original sentence:  HELLO WORLD
Encrypted sentence:   URYYB JBEYQ
... decyphered:  HELLO WORLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''