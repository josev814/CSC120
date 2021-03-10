"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 8
Assignment: Homework
Date: 2021-03-07
"""

"""
Write a Python program which performs the following tasks, using the selected methods from the table below.

(1) create a string variable my_string and assign '*1a@B2@cA@3##' to it. Print the original my_string.
(2) use the proper method(s) to strip off the * symbol(s) on the left end and the # symbol(s) on the right end of my_string. 
    Assign the resulted string to my_string and print it.
(3) use the proper method to decide whether my_string contains only alphabetic letters or digits. 
    Print the returned result (True or False).
(4) use the proper method to decide whether all alphabetic letters in my_string are uppercase. 
    If not (implemented with decision structure), call the proper method to convert lowercase alphabetic letters to uppercase, then assign the resulted string to my_string and print it.
Select the proper methods to use from the table below:

isalnum()	isalpha()	isdigit()	islower()
isspace()	isupper()	lower()	lstrip()
lstrip(char)	rstrip()	rstrip(char)	strip()
strip(char)	upper()	
"""

"""
my_string = '*1a@B2@cA@3##'
print('The original my_string is', my_string)
my_string = my_string.lstrip('*').rstrip('#')
print('After stripping', my_string)
print('Does my_string contain only letters and digits:', my_string.isalnum())
if not my_string.isupper():
    my_string = my_string.upper()
print('After capitalization:', my_string)
"""

"""
Write a Python program which performs the following tasks, using the selected methods from the table below.

(1) create a variable my_string, and assign '#12a#43a5#6a9a#32' to it. 
Print the original my_string.
(2) use the proper method to search for the index of '@' symbol in my_string. 
    If not found (implemented with decision structure), 
    use the proper method to replace all '#' symbols in my_string with '@' symbols, 
    then assign the resulted string to my_string and print it.
(3) use the proper method to decide whether my_string starts with '@' symbol. 
    If so (implemented with decision structure), 
    use the proper method to split my_string with '@' symbol as the separator. 
    Print out the returned list. 
Select the proper methods to use from the table below:

startswith(substring)	endswith(substring)	find(substring)
replace(substring, new_substring)	split()	split(substring)
"""
my_string = '#12a#43a5#6a9a#32'
print('Original string', my_string)
if '@' not in my_string:
    my_string = my_string.replace('#', '@')
print('After replacement:', my_string)
if my_string.startswith('@'):
    my_arr = my_string.split('@')
    print('After split, the returned list is', my_arr)
