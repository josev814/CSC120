"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 11
Assignment: Worksheet
Date: 2020-11-07
"""

from math import sin, tan, cos, exp, log, pi, acos, asin


def print_exercise(exercise):
    print(end='\n\n')
    print('#' * 10, 'Exercise', exercise, '#' * 10)


"""
For x=0.5, 1.0, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, what are the values of sin(x), tan(x), cos(x), exp(x), log(x)
"""

print_exercise(1)
num = None
for x in range(8):
    for i in range(2):
        if i == 1 and x < 7:
            num = float(x + .5)
        elif x > 0:
            num = x
        if num:
            print('num: {}, sin: {}, tan: {}, cos: {}, exp: {}, log: {}'.format(
                num, sin(num), tan(num), cos(num), exp(num), log(num))
            )
        if x == 7:
            break

input('Press enter to continue: ')


"""
For x = -1 + k*0.02, for k =0, 1, 2, …, 100, plot acos(x) and asin(x) using turtle graphics. 
Set the world coordinates to -1, -pi/2, 1,  pi. 
"""
print_exercise(2)

import turtle
trtle = turtle.Turtle()
scr = turtle.setworldcoordinates(-1, -(pi/2), 1, pi)
trtle.hideturtle()
trtle.speed(0)
trtle.pensize(2)
trtle.hideturtle()
trtle.pu()
for k in range(101):
    x = -1 + k * 0.02
    y = acos(x)
    trtle.goto(x, y)
    if k == 0:
        trtle.pd()

trtle.pu()
trtle.goto(.75, 3)
trtle.write('ACOS')

trtle.goto(.75, 2.9)
trtle.pencolor('blue')
trtle.write('ASIN')
trtle.pu()
for k in range(101):
    x = -1 + k * 0.02
    y = asin(x)
    trtle.goto(x, y)
    if k == 0:
        trtle.pd()

input('Press enter to continue: ')


"""
An engineer of a construction company is interested in finding at least one value of x that will make the function 
    f(x) = x**2   - sin(x) to be zero. 
The engineer knows that one such value of x is close to pi/2.  
Using that as a guess, the engineer decided to find a more accurate value by iteratively computing: 

Formula 1: x_new = x_old – f(x_old) 
or 
Formula 2: x_new = x_old – f(x_old)/ (2*x_old   - cos(x_old)). 

Where x_new is the new value of x. 
We replace the old value  (x_old) with the new value (x_new) in subsequent iterations (that is assign x_new to x_old). 
The first x_old is pi/2.  

The engineer uses x_new that will satisfy the |x_new-x_old|/|x_old|<1.0e-6 where |a| is the absolute value of a. 
Here, 1.0e-6 is called error tolerance – the margin of error that the engineer is willing to accommodate in the estimated value. 

Write a program that will compare both formulas by counting how many iterations needed to arrive at the desired result.
Try other values for the error tolerance, like 1.0e-8, 1.0e-9, etc. 
"""


print_exercise(3)


def run_formula(x, run_formula):
    """
    Runs x within the formula passed as a string
    :param x:
    :param run_formula: The string formula that gets evaled
    :return x_new, x: the new x value and the old_x value
    """
    x_new = eval(run_formula)
    return x_new, x


def get_x_abs_diff(x, x_old):
    """
    diffs the x val from the old x val and returns the absolute value of the diff
    :param x:
    :param x_old:
    :return: float
    """
    return abs(x - x_old)


def get_x_satisfaction(x, x_old):
    """
    Returns the engineers x calc to compare with the tolerance level
    :param x:
    :param x_old:
    :return:
    """
    return get_x_abs_diff(x, x_old) / abs(x_old)


def zero_func(x):
    """
    The function that checks if the result is 0
    :param x:
    :return:
    """
    return x**2 - sin(x)


def run_formula_tests(x, formula):
    """
    Runs the formula tests and returns the amount of iterations to reach the tolerance level and the value of x
    :param x: the starting x value
    :param formula: the formula to run for this test
    :return loops, x: returns the amount of iterations used and the new x value
    """
    loops = 0
    valid_tolerance = False
    while not valid_tolerance:
        x, old_x = run_formula(x, formula)
        if get_x_satisfaction(x, old_x) < TOLERANCE:
            valid_tolerance = True
        loops += 1
    return loops, x


TOLERANCE = 1.0e-6
FORMULA_ONE = 'x - zero_func(x)'
FORMULA_TWO = 'x - zero_func(x)/(2*x - cos(x))'

for i in range(2):
    x = pi / 2
    formula = FORMULA_ONE
    if i > 0:
        formula = FORMULA_TWO
    loops, x = run_formula_tests(x, formula)
    print("""
Forumla {} "{}" took {} iterations to get to a valid tolerance.
    The value of {} should be used which gives an error tolerance less than {}""".
          format(i+1, formula, loops, x, TOLERANCE)
          )
