"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 8
Assignment: Class
Date: 2020-10-14
"""

"""
We're covering Functions and variable scopes today
"""

"""
Function Syntax
General syntax is
def function_name(params):
    statements to execute

the void function does not return a value to the caller function

General form for calling (invoking) the void function:
function_name(args)

a value-returning function returns a value to the caller function
the function-body must contain a return statement.
A return statement begins with the keyword return

calling or invoking a value-returning function
The varables to the left must match the qty of return values from the function
rvar1, rvar2, ... = function_name(arguments list)


the function_name is the name you give to the function.
The name must begin with a letter, must not contain special characters including spaces
Python is case-sensitive whe calling function names
the parameter list consists of input variables to the function, listed
individually and separated using commas.
The line of the function definition is the header.
the function-body is a group of consistently indented statements.

Syntax 1: (void function with no parameters)
def function_name():
    statement1
    statement2
    ...
none of the statements is a return statement


Syntax 2 (void function with 1 or more params (input variables)
def function_name(param1, param2, param3, ....):
    statement1
    statement2
    ...
none of the statements is a return statement


Syntax 3 (value-returning function with no parameters)
def function_name():
    statement1
    statement2
    ...
    return value_to_return, value_to_return_2, ...
Return statements can exist anywhere in the function

Syntax 4 (value-returning function with parameters)
def function_name(param1, param2, param3, ....):
    statement1
    if param1 > 0:
        return None
    statement2
    ...
    return value_to_return, value_to_return_2, ...
Return statments can exist anywhere in the function

Defining a function assigns space in memory for the function.
"""


def welcome_input():
    name = input('Please, enter your name: ')
    msg = 'Hello {},\r\nWelcome to this class.'.format(name)
    return msg


def welcome(name):  # parameter variable is name
    msg = 'Hello {},\r\nWelcome to this class.'.format(name)
    return msg


def get_name():
    name_str = input('Please, enter your name: ')
    return name_str



string = welcome_input()
name_input = get_name()
string = welcome(name_input)  # the argument is the value of a variable name
# the value of the argument is assigned to the parameter at function call or execution
print(string)


"""
write a function that will accept an integer value
the function will display whether or not the int is divisible by 5 
"""


def divisible_by_five(integer):
    if integer % 5 == 0:
        print('{} is divisible by {}'.format(integer, 5))
    else:
        print('{} is NOT divisible by {}'.format(integer, 5))


def divisible_by_x(integer, divisor):
    if integer % divisor == 0:
        print('{} is divisible by {}'.format(integer, divisor))
    else:
        print('{} is NOT divisible by {}'.format(integer, divisor))


"""
every python file is a treated as a module in python
"""
import random
divisible_by_five(random.randint(0, 100))
divisible_by_x(random.randint(0, 100), 7)


def calc_int_sums(inta, intb):
    """
    Write a function that will accept 2 ints
    the function will calculate and display the sum of the ints
    """
    calc_sum = inta + intb
    calc_diff = inta - intb
    print('The sum of {} and {} is {}'.format(inta, intb, calc_sum))
    print('The diff of {} and {} is {}'.format(inta, intb, calc_diff))


def x_y_z_calc(x):
    """
    Write a function that will accept a float(x) and calculate and display the following
    y = x**5 + x
    z = x + y + x*y
    """
    y = x ** 5 + x
    z = x + y + x * y
    print('y: {}'.format(y))
    print('z: {}'.format(z))


"""
positional arguments: the arguments will be matched correspondingly with the parameter variables
the first arg matches param 1
the second arg matches param 2
"""
calc_int_sums(2, 5)  # the value of inta = 2, the value of intb = 5
x_y_z_calc(5)


"""
keyword arguments: the arguments will be matched correspondingly with the argument name used
the function param is matched to the arg
"""
calc_int_sums(intb=5, inta=2)


def count_os(my_str, find_char):
    """
    Write a function that will accept a string literal
    the function will calculate the number of times the find_char appears
    """
    tmp_str_count = len(my_str.replace(find_char, ''))
    char_count = len(my_str) - tmp_str_count
    """
    char_count = 0
    for char in my_str:
        if find_char == char:
            char_count += 1
    """
    print('{} contains the letter "{}" {} times'.format(my_str, find_char, char_count))


count_os('hello world', 'o')

"""
global and local scope variables, variable scope
Variable scope is part of the program in which the variable is accessible
A local variable is one that is accessible to a function
    This has a function scope and is only available in the function
    These variables are typically defined within the function
A global variable is one that is accessible everywhere in the program.
    Global variables are defined outside of the function in the main script
The parameter variables defined in the function header are local to the function
"""

accum = 0  # global var


def add():
    a = float(input('Enter a value to add: '))  # local var
    # accum += a  #this will not work to update the accum var since accum isn't defined locally
    total = accum + a
    print(total)


def subtract():
    a = float(input('Enter a value to subtract: '))
    total = accum - a
    print(total)


add()
subtract()


"""
To modify the global variable in a function, use the global statement
"""
def glob_add():
    global accum
    a = float(input('Enter a value to add: '))  # local var
    accum += a
    print(accum)


def glob_subtract():
    global accum
    a = float(input('Enter a value to subtract: '))
    accum -= a
    print(accum)


glob_add()
glob_subtract()
