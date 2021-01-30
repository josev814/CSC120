"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 1
Assignment: TakeHome Exercise 4-1
Date: 2021-01-30
"""
"""Question 1"""
from math import sqrt


def get_sqrt(number):
    num_sqrt = sqrt(number)
    return num_sqrt


def is_true(val):
    if val.strip().lower()[0] in ['t', '1', 'y']:
        return True
    return False

contin = True
question = 'Enter a Number: '
continue_question = 'Do you want to continue? answer yes/no '
while contin:
    get_number = int(input(question))
    print('The square root of the entered number is {:.0f}'.format(get_sqrt(get_number)))
    continue_input = input(continue_question)
    contin = is_true(continue_input)

"""Question 2"""
lower_limit = int(input('What is the lower limit of the range? '))
upper_limit = int(input('What is the upper limit of the range? '))
for i in range(lower_limit, upper_limit + 1):
    print(i, end=' ')

"""Question 3"""
lower_limit = int(input('What is the lower limit of the range? '))
upper_limit = int(input('What is the upper limit of the range? '))
for i in range(lower_limit, upper_limit + 1):
    if i % 2 == 0:
        print(i, end=' ')