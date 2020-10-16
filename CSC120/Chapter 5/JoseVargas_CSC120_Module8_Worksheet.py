"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 8
Assignment: Worksheet
Date: 2020-10-15
"""

import turtle


def is_divisible_by_x(num, divisor):
    if 100*num % divisor == 0:
        return True
    return False


def get_user_dollars():
    dollars = 0
    while dollars <= 0:
        try:
            dollars = float(input('Enter you dollar amount: $'))
            if dollars <= 0 or not is_divisible_by_x(dollars, 50):
                dollars = 0
                raise ValueError
        except ValueError:
            print('You must enter an integer or float dollar amount that is divisible by 50')
    return dollars


class DollarsToChange(object):
    dollars = 0

    def __init__(self, dollars):
        self.dollars = dollars

    def convert_to_pennies(self):
        pennies = self.dollars / .01
        return pennies

    def convert_to_nickels(self):
        nickels = self.dollars / .05
        return nickels

    def convert_to_dimes(self):
        dimes = self.dollars / .1
        return dimes

    def convert_to_quarters(self):
        quarters = self.dollars / .25
        return quarters


def calculate_change_qty(user_dollars):
    currencies = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}
    for currency_name in currencies:
        dollar_in_currency = user_dollars / currencies[currency_name]
        print('Your ${:,.2f} is equal to {:,.0f} {}'.format(user_dollars, dollar_in_currency, currency_name))


def question_one():
    """
    Write a function that will ask the user to enter a value in dollars.
    The function should calculate and display the equivalent number of pennies, nickels, dimes, and quarters.
    Acceptable values are those which when multiplied by 100 will be exactly divisible by 50 (100*value must be exactly divisible by 50).
    Write a caller main function to call your function.
    """
    print('Question 1:')
    user_dollars = get_user_dollars()
    calculate_change_qty(user_dollars)
    """
    print('The same process but using a class now')
    change_calculator = DollarsToChange(user_dollars)
    print('Your ${:,.2f} is equal to {:,.0f} quarters'.format(user_dollars, change_calculator.convert_to_quarters()))
    print('Your ${:,.2f} is equal to {:,.0f} dimes'.format(user_dollars, change_calculator.convert_to_dimes()))
    print('Your ${:,.2f} is equal to {:,.0f} quarters'.format(user_dollars, change_calculator.convert_to_nickels()))
    print('Your ${:,.2f} is equal to {:,.0f} quarters'.format(user_dollars, change_calculator.convert_to_pennies()))
    """

def get_user_radius():
    radius = 0
    while radius <= 0:
        try:
            radius = float(input('Enter a radius for a circle: '))
            if radius <= 0:
                raise ValueError
        except ValueError:
            print('You must enter an integer or float radius greater than 0')
    return radius


def get_user_fill_color():
    color = ''
    colors = ['red', 'green', 'yellow', 'black', 'blue']
    while color not in colors:
        try:
            color = input('Enter a color to fill the circle {}: '.format(colors)).lower()
            if color not in colors:
                raise ValueError
        except ValueError:
            print('You must enter a valid color {}'.format(colors))
    return color


def question_two():
    """
    Write a function that will ask the user to enter
        the radius (in pixels) of circle
        the color (only red, green, yellow, black and blue are allowed)
    and using the turtle graphics,
        display the circle filled with the color the user entered.
        Write a caller main function that will call your function.
    """
    radius = get_user_radius()
    color = get_user_fill_color()
    trtl = turtle.Turtle()
    trtl.hideturtle()
    trtl.pensize(0)  # making the border not visible
    trtl.pencolor(color)
    scr = turtle.Screen()
    trtl.fillcolor(color)
    trtl.begin_fill()
    trtl.circle(radius)
    trtl.end_fill()
    scr.exitonclick()


def get_loan_amount():
    loan_amount = 0
    while loan_amount <= 0:
        try:
            loan_amount = float(input('Enter a loan amount: $'))
            if loan_amount <= 0:
                raise ValueError
        except ValueError:
            print('You must enter an integer or float loan amount greater than 0')
    return loan_amount


def get_apr():
    apr = 0
    while apr <= 0:
        try:
            apr = float(input('Enter a loan annual percentage interest rate: '))
            if apr <= 0:
                raise ValueError
        except ValueError:
            print('You must enter an integer or float annual percentage interest rate greater than 0')
    return apr


def get_loan_month_length():
    months = 0
    while months <= 0:
        try:
            months = float(input('Enter how many months the loan is for: '))
            if months <= 0:
                raise ValueError
        except ValueError:
            print('You must enter an integer greater than 0 for how many months the loan is for')
    return months


def question_three():
    """
    Write a loan function that will ask the user to enter the loan amount (a),
    the annual percentage interest rate (r),
    the number of months for the loan (n).
    The function will calculate and display the monthly payment (p) in 2 decimal places using the formula below:
    p= a ∗ b / (1−(b+1)^−n)
    b=r/1200
    """
    a = get_loan_amount()
    r = get_apr()
    n = get_loan_month_length()
    b = r/1200
    p = a * b / (1 - (b+1)**-n)
    print('The loan monthly payment is {:.2f}'.format(p))


def next_question():
    print()
    print(input('Press enter to go to the next question'), end='\r\n')


def main():
    question_one()
    next_question()
    question_two()
    next_question()
    question_three()


main()

