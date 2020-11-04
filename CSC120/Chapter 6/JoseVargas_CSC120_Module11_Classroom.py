"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 12
Assignment: Class
Date: 2020-11-04
"""

"""
read data from the keyboard (use the input function) that we would need in our program

we usually write our results (display data) to the screen- use the 
print function to display the results or data from our program

the input data and the output data are not permanent and not available for future use

If you want to use data from the program in the future, you need to save (store) the data to a file (data file)

Types of data files:
 1. text or ascii file, file extension can be .txt
 2. binary file (micros -- extension .dat)

Types of file access:
 1. sequential file access
 2. random(or direct) file access

Steps in involve in file processing
 1. open a file (use open function)
 2. process data in file
 3. close the file (use close function

Python syntax
file_object = open(filename, mode)  # file name is a string
file_object is a variable name used to reference the file
filename is a string reference of the name of the file and sometimes the path to it
the mode is a string specifier that indicates the access modes
there are three access modes
 'r' = read -- the object will allow for access to file for read only.  If the file doesn't exist, the statement will
                throw an exception error
 'w' = write -- the object will allow for access to the file in write mode only.  If the file already exists, the entire
                data in the fill will be erased and the a file will be created.  Use that write mode with caution
 'a' = append -- the append mode is similar to the write mode, but it will append data to the file.
 To use binary then append 'b' to the mode
"""
from random import randint
filename = 'phones.txt'
"""try:
    with open(filename) as fh:
        for line in fh.readline():
            print(line)
except FileNotFoundError:
    print('The file "%s" does not exist' % filename)
"""

# file write example
fObj = open(filename, 'w')
fObj.write('Name' + '\t' + 'Phone Number' + '\n')
phone = ''
for i in range(10):
    phone += str(randint(0, 9))
fObj.write('Jose' + '\t' + phone + '\n') # the data being written to a file must be a string
fObj.close()


# Write a program that will prompt a user to enter the names of 5 students and their ages
"""
def getStudentName(idx):
    return input('What is the name of student {}? '.format(idx))


def getAge(student):
    validAge = False
    while not validAge:
        try:
            age = int(input('What is the age of %s? ' % student))
            if age == 0:
                raise ValueError
            validAge = True
        except ValueError:
            print('ERROR: You must enter an int for the student age')
    return age


filename = 'stdAges.txt'
colSeparator = '\t'
fObj = open(filename, 'w')
fObj.write('Student' + colSeparator + 'Age' + '\n')
for i in range(5):
    name = getStudentName(i+1)
    age = getAge(name)
    fObj.write('{}{}{}\n'.format(name, colSeparator, age))
fObj.close()
"""

"""
Appending data to a file
"""
fObj = open(filename, 'a')
phone = ''
for i in range(10):
    phone += str(randint(0, 9))
fObj.write('Tracy' + '\t' + phone + '\n')  # the data being written to a file must be a string
fObj.close()

"""
Reading data from file ( sequential file access )
We read data from a file a line at a time
"""

fObj = open(filename, 'r')
record = fObj.readline().rstrip('\n') #first record
print(record.rstrip('\n'))
while record != '':
    record = fObj.readline().rstrip('\n')
    print(record)
fObj.close()

#or

fObj = open(filename, 'r')
for line in fObj:
    print(line.rstrip('\n'))
fObj.close()

"""
Combining read and append mode
"""
print('Read/Append Mode')
print('Reading')
fObj = open(filename, 'a+')
print('Setting to the top of the file')
fObj.seek(0)
for line in fObj:
    print(line.rstrip('\n'))
phone = ''
for i in range(10):
    phone += str(randint(0, 9))
print('Writing')
fObj.write('Dan' + '\t' + phone + '\n')  # the data being written to a file must be a string
print('Resetting to top')
fObj.seek(0)
print('Reading')
for line in fObj:
    print(line.rstrip('\n'))
print()
fObj.close()


# write a program that will read and display all records in stdAges.txt
filename = 'stdAges.txt'
fObj = open(filename, 'r')
record = fObj.readline().rstrip('\n') #first record
print(record.rstrip('\n'))
while record != '':
    record = fObj.readline().rstrip('\n')
    print(record)
fObj.close()

"""
Other ways of reading data from a from

The file object which is the variable referencing the file is an interable object
You can use the for loop to iterate through the object to access on line or record at a time
"""
filename = 'stdAges.txt'
fObj = open(filename, 'r')
for line in fObj:
    record = line.rstrip('\n')
    print(record)
fObj.close()

# You can use the read function to read the entire data in the file.
# The larger the file the worst it is for memory utilization
fObj = open(filename, 'r')
all_lines = fObj.read().rstrip(('\n'))  # this is a string
print(all_lines)
fObj.close()

"""
write a program that will read the records in the stdAges.txt
Calculate and display the average age
"""
fObj = open(filename, 'r')
records = 0
ages = 0
header = True
for record in fObj:
    if header:
        header = False
        continue
    record_info = record.rstrip('\n').split('\t')
    records += 1
    ages += int(record_info[1])
average_age = ages / records
print('Average Age:', average_age)
fObj.close()


"""
How to manipulate the records
Use a temporary file for the new data with the record
then use the os.remove to remove the old file
then use os.rename to rename the temp file with the old file name
"""
from os import remove
from shutil import copy

copy('phones.txt', 'phones.txt.swap')
fObj = open('phones.txt.swap', 'r')
wObj = open('phones.txt', 'w')
for line in fObj:
    if 'Tracy' in line:
        continue
    wObj.write(line)
fObj.close()
wObj.close()
remove('phones.txt.swap')

"""
Write a program that will prompt a user for the record to remove from the file stdAges.txt
Your program will remove the record from the file
"""
from os import remove, rename

rename('stdAges.txt', 'stdAges.txt.swap')
fObj = open('stdAges.txt.swap', 'r')
wObj = open('stdAges.txt', 'w')
removeRecord = input('What user record would you like to remove? ')
for line in fObj:
    if line.lower().startswith(removeRecord.lower()):
        continue
    wObj.write(line)
fObj.close()
wObj.close()
remove('stdAges.txt.swap')
