# p57.py
# Uyen Nguyen
# 03/06/22
# Python 3.10.0
# Description:
'''
Program 57:

In a weighted alphabet, every symbol is assigned a positive real number called a weight.
A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.
The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

1) The mass of each possible amino acid is given in the file aa.txt Download aa.txt
- Put the contents of the above file into a dictionary:  dictionary [ 'Letter' ] = value

2) Ask the user to enter an amino acid string consisting of only the letters shown in file aa.txt
- if the user enters an incorrect letter, then the program asks for another string

3) Calculate the total weight of the amino acid
 a) use characters of the string as keys for the dictionary from (1)
 b) sum the weights for all letters and show the total weight
'''

# 1. Put the contents of the above file into a dictionary

# Read the data from file into a list
dataFile = open('week_10/aa.txt', 'r')
fileAsListOfLines = dataFile.read().splitlines()
dataFile.close()

dictData = {}  
dictID = ''                                   # Create an empty dictionary for data
aminoAcidList = []                            # For use in part 2
for i in range (0, len(fileAsListOfLines)):
    # Each list item is a new line from the file
    listData = fileAsListOfLines[i].split()   # Split each line by spaces
    
    # Each letter is the ID for each item in the dictionary
    dictID = listData[0]
    dictData[dictID] = ''.join(listData[1])

    aminoAcidList.append(dictID)              # Each ID is the amino acid name (for part 2)

print ('Dictionary: ', dictData, '\n')

# 2. Ask the user to enter an amino acid string consisting of only the letters shown in file aa.txt
# - if the user enters an incorrect letter, then the program asks for another string

match = False
while match == False:
  print ('A list of possible amino acid: ')
  print ('A C D E F G H I K L M N P Q R S T V W Y')
  listUser = input('Enter an amino acid string consisting of only the amino acid shown above: ')
  listUser = listUser.upper()   # To upper case
  
  # Compare the user answer to the amino acid list
  longStr = ''
  shortStr = ''
  if len(aminoAcidList) > len(listUser):
    longStr = ''.join(aminoAcidList)
    shortStr = ''.join(listUser)
  else:
    longStr = ''.join(listUser)
    shortStr = ''.join(aminoAcidList)
  
  count = 0
  for i in range (0, len(longStr)):
    for j in range (0, len(shortStr)):
      if shortStr[j] == longStr[i]:
        count += 1
  
  if count == len(listUser) and len(listUser) > 0:
    match = True
    
  if match == False:
    print ('\n')
    print ('Your input is invalid')

# 3. Calculate the total weight of the amino acid

totalWeight = 0
for i in range (0, len(listUser)):
  totalWeight += float(dictData[listUser[i]])
print ('Total weight = %.3f' %totalWeight)

'''
========= RESTART: /Users/uyennguyen/Documents/CIS_D040./week_10/p57.py ========
Dictionary:  {'A': '71.03711', 'C': '103.00919', 'D': '115.02694', 'E': '129.04259', 'F': '147.06841', 'G': '57.02146', 'H': '137.05891', 'I': '113.08406', 'K': '128.09496', 'L': '113.08406', 'M': '131.04049', 'N': '114.04293', 'P': '97.05276', 'Q': '128.05858', 'R': '156.10111', 'S': '87.03203', 'T': '101.04768', 'V': '99.06841', 'W': '186.07931', 'Y': '163.06333'} 

A list of possible amino acid: 
A C D E F G H I K L M N P Q R S T V W Y
Enter an amino acid string consisting of only the amino acid shown above: qaMNyV
Total weight = 706.311
'''