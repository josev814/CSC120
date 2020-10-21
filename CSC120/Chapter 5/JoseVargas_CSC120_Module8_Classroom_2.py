"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 8
Assignment: Class
Date: 2020-10-21
"""

"""
Covering value-returning Functions and 
python libraries that have value-returning functions

Some libraries are integrated in Python interpreter: functions
in these libraries are called built-in functions examples are
print, range, input, str, float, type, bool, int, etc
These built-in functions are called directly in the program
Void build-in functions:
    print
Value-returning built-in functions:
    range, input, str, float, type, bool, int

Two ways to call a value-returning function:
1. Call the function and assign the returned value to a variable
2. Insert the function in an expression

ex 1:
v = int(35.8)  # returned value is assigned to variable v

ex 2:
print(23 + int(35.8))  # using a value-returning function in an expression

Calling a value-returning function without assigning it to a variable or passing it to the print function, 
    the value returned isn't captured
    
There are several libraries that come with Python that are not integrated into the Interpreter.
These are standard libraries.
How to use the function implemented in the standard libraries.  These libraries are stored in modules (script files).
To use the module you must import the module first
To import only a specific function or class of a module use from module import function/class

Currently we're going to focus on the random and math modules
If you want to use the module, you shouldn't have a file with the same name in your project.  If you have a file with
the same module name it will override the default library

ex: random.py or math.py will override the random/math Python Libraries

Random module contains functions for generating random numbers
Applications: gaming, simulations, encryption and statistics

The import statement loads the module and associate functions into the memory
"""
import random  # import statement


"""
commonly used functions in random module are:
    randint, random, randrange and uniform

To call a function within the module, we us the dot notation to associate the function with the module

General form for randint
    random.randint(a, b) where a and b are integers.
    b must be greater than a.
    This will return a random number between a and b and include a,b

General form for randrand:
    random.randrange(a) # will return a value between 0 and a-1.
    random.randrange(a, b) # a represents start, b represents end - 1
    random.randrange(a, b, step)  # returns a random number in the sequence start, start+step, start+k*step
        where start+k*step<=end-1

General form for random
    random.random()  # will return a random floating-point value between 0 and 1

General form for uniform
    random.uniform(a, b)  # will return a random floating-point random number between a and b
        a and b are floats
"""

start_range = 1
end_range = 50
print(random.randint(start_range, end_range))
print(random.randrange(start_range, end_range))
print(random.randrange(start_range, end_range, step=2))
print(random.random())
print(random.uniform(start_range, end_range))

"""
Write a program that will display 20 random integers between 45 and 125
"""
for i in range(20):
    print(random.randint(45, 125), end=' ')

"""
Write a program that will generate random integers between 125 and 800
"""
for i in range(100):
    print(random.randint(125, 800), end=' ')

"""
Write a program that will roll a 6 sided die 100 times and count how many times the number 5 appears
"""
accum = 0
for i in range(100):
    if random.randint(1, 6) % 5 == 0:
        accum += 1
print('The number 5 displayed {} times'.format(accum))

"""
Write a program that will generate a positive random integer that is less than 25
"""
print(random.randrange(0, 25))
print(random.randrange(23, 99))  # between 23 and 99
print(random.randrange(23, 100, 5))  # between 23 and 99 with a step of 5
print(random.random())  # float between 0 - 1
print(random.uniform(2, 9))  # float between 2 and 9

"""
To generate a pseudorandom number requires a seed.
The default seed that python uses for the random module is the system time
To always generate the same random number use the seed function in random
"""
random.seed(5)
print(random.random())  # The random number will always be the same
for i in range(20):
    print(random.randint(45, 125), end=' ')
print()

"""
You can import the function individually to your code or all of the functions in the module
Use the from import statement
This allows you to call the function in your code without the dot notation and reference of the parent module
"""
from random import randint  # this will import randint only

for i in range(60):
    print(randint(1, 6), end=' ')
print()

from random import randint, getrandbits  # import a list of functions
"""
Use the wildcard to include all functions in the module in the program, 
    so you can call the function directory without dot notation
"""
from random import *
for k in range(60):
    print(randrange(1, 7), end=' ')
print()

"""
The math module has several mathematical functions and named constants (pi, e)
Commonly used math functions are listed on page 263:
    acos, asin, atan, ceil, cos, degrees, exp, floor, hypot, log, log10, radians,
    sin, sqrt, tan
Each function accepts a float argument.  If an integer is used, it is converted to a float
Each function returns a float except for floor and ceil.  Those return an int.
"""
import math
print('pi = ', math.pi, 'e=', math.e)
print(math.sin(12.5))

"""
Use turtle graphics to draw sin function between 0 and 6*pi
"""
import math
import turtle

turtle.setworldcoordinates(0, -1, 6*math.pi, 1)
scr = turtle.Screen()
trtle = turtle.Turtle()
trtle.hideturtle()

step = 6*math.pi/100

for i in range(101):
    x = i*step  # points on the x-axis (0, 6*pi)
    y = math.sin(x)
    trtle.penup()
    trtle.goto(x, y)
    trtle.pendown()
    trtle.dot()
#scr.exitonclick()

"""
Write a program that will plot the cos function using turtle
"""
#import math
#import turtle
import random

#turtle.setworldcoordinates(0, -1, 6*math.pi, 1)
scr = turtle.Screen()
trtle = turtle.Turtle()
trtle.hideturtle()
step = 6*math.pi/100

colors = ['blue', 'red', 'green', 'black']

for i in range(101):
    x = i*step  # points on the x-axis (0, 6*pi)
    y = math.cos(x)
    trtle.penup()
    trtle.goto(x, y)
    trtle.pencolor(colors[random.randrange(len(colors))])
    trtle.pendown()
    trtle.dot()
scr.exitonclick()

"""
Syntax 1 (value-returning function with no parameters)
def function_name():
    statement1
    statement2
    ...
    return value_to_return, value_to_return_2, ...
Return statements can exist anywhere in the function

Syntax 2 (value-returning function with parameters)
def function_name(param1, param2, param3, ....):
    statement1
    if param1 > 0:
        return None
    statement2
    ...
    return value_to_return, value_to_return_2, ...
Return statments can exist anywhere in the function

Syntax 3 (value-returning function with parameters and default values)
def function_name(param1=-5, param2='test', param3=4.556, ....):
    statement1
    if param1 > 0:
        return None
    statement2
    ...
    return value_to_return, value_to_return_2, ...
Return statments can exist anywhere in the function

Note that non-default value parameters must appear before default value parameters
"""

"""Programming Exercise #20 (page 263)"""
# Open the ProgrammingEx20.py file