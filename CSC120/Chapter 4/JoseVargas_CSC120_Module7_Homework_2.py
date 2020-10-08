"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 7
Assignment: Homework #2
Date: 2020-10-07
"""

"""
Exercise 3, Page 203:
Write a for loop that displays
0, 10, 20 - 1000
"""
print('Algorithm Exercise 3: ')
for i in range(0, 1001, 10):
    print(i, end=' ')
print()

input('Press enter to continue to the next exercise:')
print()

"""
Exercise 6, Page 203:
Rewrite the statements augmented assignment operators.
"""
print('Algorithm Exercise 6: ')
x = 0
x += 1
print('x += 1', x)
x *= 2
print('x *= 2', x)
x /= 10
print('x /= 10', x)
x -= 100
print('x -= 100', x)


input('Press enter to continue to the next exercise:')
print()

"""
Exercise 8, Page 204:
Write code that prompts the user to enter a positive nonzero number and validates the input
"""
print('Algorithm Exercise 8: ')
is_invalid = True
while is_invalid:
    try:
        user_input = float(input('Enter a positive number: '))
        if user_input <= 0:
            raise ValueError
        is_invalid = False
    except ValueError:
        print('ERROR: You must enter a positive nonzero number.')
