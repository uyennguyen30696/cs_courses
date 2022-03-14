# p48.py
# Uyen Nguyen
# 03/01/22
# Python 3.10.0
# Description:
'''
Program 48:

Write a program which reads the data from file sunspots.txt  Download sunspots.txt:
...and computes the average for each year, writing them one per line to a file averages.txt (as shown below):
'''

file = open('week_9/sunspots.txt', 'r')
# Read the data from file into a list
fileAsListOfLines = file.read().splitlines()
file.close()

# Write data result in a new file
newFile = open('average.txt', 'w')
newFile.write('Year Avg \n')

# print ('Year Avg')
# Each list item is a new line from the file
for i in range(0, len(fileAsListOfLines)):
  listData = fileAsListOfLines[i].split() # Split each line by spaces

  # Get each year
  year = listData[0]

  # Calculate average of data from each year
  sum = 0
  for j in range(1, len(listData)):
    sum += float(listData[j])
  avg = sum / (len(listData) - 1)

  # print (year, '%.2f' %avg)

  newFile.write('%s %.2f \n' %(year, avg))

newFile.close()

'''
Year Avg 
1945 32.29 
1946 99.88 
1947 170.93 
1948 166.61 
1949 174.08 
1950 103.70 
1951 64.42 
1952 30.53 
1953 12.46 
1954 3.36 
1955 34.59 
1956 125.92 
1957 168.32 
1958 172.12 
1959 144.99 
1960 102.11 
1961 44.68 
1962 29.81 
1963 22.17 
1964 7.44 
1965 12.07 
1966 38.66 
1967 86.25 
1968 97.49 
1969 104.59 
1970 107.38 
1971 66.48 
1972 67.33 
1973 36.69 
1974 32.34 
1975 14.40 
1976 11.58 
1977 26.01 
1978 86.90 
1979 145.80 
1980 149.07 
1981 146.48 
1982 115.14 
1983 64.63 
1984 43.60 
1985 16.15 
1986 11.08 
1987 28.84 
1988 100.67 
1989 162.39 
1990 144.89 
1991 144.39 
1992 93.72 
1993 54.70 
1994 30.98 
1995 18.27 
1996 8.40 
1997 20.27 
1998 61.58 
1999 95.98 
2000 123.33 
2001 123.24 
2002 109.47 
2003 65.76 
2004 43.32 
2005 31.03 
2006 15.33 
2007 8.67 
2008 2.42 
'''