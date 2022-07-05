# ch7_ex1.py
# Uyen Nguyen
# 05/25/22
# Python 3.10.0
# Description:
'''
Ask the user to enter the backend error log file name ("ErrorLog.txt")
Read and print lines that match some specific criteria
'''

# Ask the user to enter the backend error log file name ("ErrorLog.txt" or "ch7_ex1/ErrorLog.txt" if file in ch7_ex1 folder)
fname = input('Enter the file name: ')
# Read the file (hand = handle)
try:
    fhand = open(fname, 'r')
except:
    print ('File can not be opened:', fname)
    quit()
# Report error file
rFile = open('reportError.txt', 'w')

count = 0
errorLineCount = 0
for line in fhand:
    line = line.strip()
    # Count how many lines are in the file
    if line != '':
        count += 1
    # Print the lines which have a word "error", "Error" and "ERROR" and count them
    if 'error' in line or 'Error' in line or 'ERROR' in line:
        print (line)
        rFile.write(line + '\n')
        errorLineCount += 1
    
# Print the line count
print ('Total Line count:', count)
# Write line count in a report file (name the report file "reportError.txt")
rFile.write('Total line count: ' + str(count) + '\n')
# Print the error line count
print ('Error line count:', errorLineCount)
# Write the error lines in the report file
rFile.write('Error line count: ' +  str(errorLineCount))

fhand.close()
rFile.close()

'''
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A
Total line count: 108
Error line count: 5
'''
