# ch6_ex5
# Uyen Nguyen
# 05/18/22
# Python 3.10.0
# Description:
'''
Create a table for the medals. (Use lists)
Print the table.
Print the total number of medals.
Print the total number of gold, silver and bronze medals.
Remove countries without a gold medal from the table.
Then print the new table.
Use dictionaries to save the data for the countries and the medals and print it, the key is the country name and the value is a list of medals or a dictionary of the medals name and count. 
(This part is to compare using list vs. dictionaries to save data)
'''

COUNTRIES_COUNT = 7       # Columns
MEDALS_COUNT = 3          # Rows (gold, silver, bronze)

medals = ['Gold', 'Siver', 'Bronze']
countries = ['Canada', 'Italy', 'Germany', 'Japan', 'Russia', 'South Korea', 'United States']
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# Create a table 
ROWS = 3
COLUMNS = 7
table = []
for i in range(ROWS):
    row = [0] * COLUMNS
    table.append(row)

# Print the table
print ('%15s' % ' ', end= '')
for i in range(ROWS):
    print ('%8s' % medals[i], end= '')
print ()
for i in range(COUNTRIES_COUNT):
    print (countries[i].ljust(15), end= '')
    for j in range(MEDALS_COUNT):
        print ('%8d' % counts[i][j], end='')
    print ()
print ()

# Print the total number of medals
medals_num = 0
for i in range(len(counts)):
    for j in range(len(counts[i])):
        if counts[i][j] > 0:
            medals_num += counts[i][j]
print ('Total medals is', medals_num)

# Print the total number of gold, silver and bronze medals
gold = 0
silver = 0
bronze = 0
for i in range(len(counts)):
    gold += counts[i][0]
    silver += counts[i][1]
    bronze += counts[i][2]
print ('Total gold medals is', gold)
print ('Total silver medals is', silver)
print ('Total bronze medals is', bronze)
print ()

# Remove countries without a gold medal from the table and print the table
print ('The countries with at least 1 gold medal are:')
print ('%15s' % ' ', end= '')
for i in range(MEDALS_COUNT):
    print ('%8s' % medals[i], end= '')
print ()
for i in range(COUNTRIES_COUNT):
    if counts[i][0] > 0:
        print (countries[i].ljust(15), end= '')
        for j in range(MEDALS_COUNT):
            print ('%8d' % counts[i][j], end='')
        print ()
print ()

# Use dictionaries to save the data for the countries and the medals and print it
countries_and_medals = {
    'Canada': {
        'Gold': 0,
        'Silver': 3,
        'Bronze': 0
    },
    'Italy': {
        'Gold': 0,
        'Silver': 0,
        'Bronze': 1
    },
    'Germany': {
        'Gold': 0,
        'Silver': 0,
        'Bronze': 1
    },
    'Japan': {
        'Gold': 1,
        'Silver': 0,
        'Bronze': 0
    },
    'Russia': {
        'Gold': 3,
        'Silver': 1,
        'Bronze': 1
    },
    'South Korea': {
        'Gold': 0,
        'Silver': 1,
        'Bronze': 0
    },
    'United States': {
        'Gold': 1,
        'Silver': 0,
        'Bronze': 1
    }
}

print ('Print the table with data from the dictionary')
print ('%15s' % ' ', end= '')
for i in range(MEDALS_COUNT):
    print ('%8s' % medals[i], end= '')
print ()
for country, medal in countries_and_medals.items():
    print (country.ljust(15), end='')
    for medal_type, count in medal.items():
        print ('%8s' % count, end='')
    print ()

'''
===== RESTART: /Users/uyennguyen/Documents/cs_courses/CIS_D041A/ch6_ex4.py =====
                   Gold   Siver  Bronze
Canada                0       3       0
Italy                 0       0       1
Germany               0       0       1
Japan                 1       0       0
Russia                3       1       1
South Korea           0       1       0
United States         1       0       1

Total medals is 14
Total gold medals is 5
Total silver medals is 5
Total bronze medals is 4

The countries with at least 1 gold medal are:
                   Gold   Siver  Bronze
Japan                 1       0       0
Russia                3       1       1
United States         1       0       1

Print the table with data from the dictionary
                   Gold   Siver  Bronze
Canada                0       3       0
Italy                 0       0       1
Germany               0       0       1
Japan                 1       0       0
Russia                3       1       1
South Korea           0       1       0
United States         1       0       1
'''