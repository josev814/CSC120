"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 7
Assignment: Class
Date: 2020-10-07
"""

"""
While/For loops

Write a program that will prompt the user to enter a value that is greater than 20 but less than 45.
first case
"""


value = float(input('Enter a number between 20 and 45: '))
while value <= 20 and value >= 45:
    value = float(input('Wrong value entered, enter a number between 20 and 45: '))
print(value)


"""
The range function (built-in) create a range object.
    A range object is a linear sequence of integers.
    The arguments in the range function are integers not floats
    range(n) will result in 0,1,2,3,4,5 until n-1 is reached
    range(start=x,end=y) will start at x and stop at y-1
    range(end=y, step=2) will start at 0 and increment every 2 ints, 0, 2, 4, 6 until y-1 is reached
        The list here is an increment of step
"""


a = range(9)
for idx in a:
    print(idx)


"""
Use the list function to display the element in a range object
"""

print(list(a))

a = range(3, 20)
print(list(a))

a = range(3, 45, 5)
print(list(a))

"""
the for loops can be used for the following
    running total
    for sequences that are linear in nature

a string object is an iterable object
a range object is an iterable object
"""

a = 'Hello World'
for char in a:
    print(char)


"""
Write a program that will calculate the sum of odd integers between 45 and 1000
"""

# more efficient approach
sum = 0
for x in range(45, 1000, 2):
    sum += x
print('Total: {}'.format(sum))

# alternative ex
# more expensive
sum = 0
for x in range(45, 1000):
    if x % 2 == 1:
        sum += x
print('Total: {}'.format(sum))

"""
It's better to use while loops for input validation
"""

"""
Nested Loop is a loop within another loop
"""
"Write a program that will display the multiplication table"

for i in range(1, 10):
    for m in range(1, 10):
        print(i * m, end=' ')
    print()

mt = []
for i in range(1, 10):
    for m in range(1, 10):
        mt.append(i * m)
    print(mt)
    mt.clear()


"Exercise 12: Page 205"

factor = 0
while factor == 0:
    try:
        factor = int(input('What number would you like to get the nonnegative factoral of: '))
        if factor < 1:
            raise ValueError
    except ValueError:
        print('Value must be an integer greater than 0')
        factor = 0

total = 1
for i in range(1, factor+1):
    total = total * i
print(total)

"""
Exercise 14: page 206
"""

for i in range(7, 0, -1):
    print('*' * i)

"""
Exercise 18: page 207
"""
from turtle import Turtle, Screen

trtle = Turtle()
ts = Screen()

distance = 2.5
for i in range(0, 1000, int(distance)):
    trtle.fd(i + distance)
    trtle.left(90)

ts.exitonclick()

