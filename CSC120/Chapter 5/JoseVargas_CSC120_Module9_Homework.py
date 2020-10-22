"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 9
Assignment: Homework
Date: 2020-10-22
"""

"""
5. Look at the following function definition:
def my_function(a, b, c):
    d = (a+c) / b
a. Write a statement that calls this function and uses keyword arguments to pass 2 into a, 4 into b and 6 into c
b. What value will be displayed when the function call executes?
"""

def my_function(a, b, c):
    d = (a+c) / b
    print(d)

def question_five():
    print('Question 5:')
    #a:
    my_function(a=2, b=4, c=6)
    print("""2.0 is displayed when calling my_function""", end='\n\n')


"""
10. Feet to Inches
One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
of feet as an argument and returns the number of inches in that many feet. Use the function
in a program that prompts the user to enter a number of feet then displays the number of
inches in that many feet.
"""
def feet_to_inches(feet):
    return feet * 12

def get_user_feet():
    user_feet = 0
    while user_feet == 0:
        try:
            user_feet = float(input('How many feet would you like to convert to inches? '))
            if user_feet <= 0:
                raise ValueError
        except ValueError:
            print('Error: You must enter an integer or float to convert')
            user_feet = 0
    return user_feet

def question_ten():
    print('Question 10:')
    feet_to_convert = get_user_feet()
    print('{} is equal to {} inches'.format(feet_to_convert, feet_to_inches(feet_to_convert)), end='\n\n')

"""
11. Math Quiz
Write a program that gives simple math quizzes.
The program should display two random numbers that are to be added, such as:
    247 + 129
The program should allow the student to enter the answer.
If the answer is correct, a message of congratulations should be displayed.
If the answer is incorrect, a message showing the correct answer should be displayed
"""
from random import randrange

def get_random_ints(rangeStart, rangeEnd, qty=2):
    ints = []
    for i in range(qty):
        ints.append(randrange(rangeStart, rangeEnd))
    return ints

def get_user_answer(ints):
    add = ''
    oper = False
    for add_int in ints:
        if oper:
            add += ' + '
        add += '{}'.format(add_int)
        oper = True
    return int(input('What does {} equal? '.format(add)))

def question_eleven():
    print('Question 11:')
    random_add = get_random_ints(1, 255)
    total = sum(random_add)
    user_answer = get_user_answer(random_add)
    if user_answer == total:
        print('Congratulations, you got it right')
    else:
        print('Sorry, the correct answer is', total)

if __name__ == '__main__':
    question_five()
    input('Press Enter to go to the next question')
    question_ten()
    input('Press Enter to go to the next question')
    question_eleven()