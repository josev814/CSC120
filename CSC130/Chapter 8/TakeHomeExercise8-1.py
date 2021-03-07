"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 8
Assignment: Homework
Date: 2021-03-07
"""

"""
Write a program which performs the following tasks:

(1) define a string named string1 and initialize it with the value: '123AB'.

(2) create another string named string2 with the value 'CDE45'.
Then, concatenate string2 to the back of string1 using the + operator.
Print the extended string1.

(3) Use the len function to get the length of string1. Then, print it out.

(4) Print the character with index number -8 in string1.

(5) Use the slicing expression with the corresponding indexes to extract the slice/subsection 'ABCDE' from string1. Print the extracted slice.

(6) Use the in operator to detect if substring 'cd' is in the slice or not, print the result (True/False).
"""
# step 1
string1 = '123AB'

# step 2
string2 = 'CDE45'
string1 += string2
print('The extended string1 is', string1)

# step 3
print('The length is', len(string1))

# step 4
print('The character at index -8 is', string1[-8])

# step 5
find_ind = 'ABCDE'
start_index = string1.index(find_ind)
slice = string1[start_index:start_index + len(find_ind)]

print('The extracted slice is', slice)

# step 6
print('Does the slice contain "cd"?:', 'cd' in slice )


"""
Write a program that performs the following tasks:

(1) Ask user to enter a string.

(2) duplicate each character in the entered string using a loop.

(3) Print the resulted string.
"""
user_input = input('Enter a string: ')
dup_string = ''
for char in user_input:
    dup_string += char*2
print('After Duplication', dup_string)
