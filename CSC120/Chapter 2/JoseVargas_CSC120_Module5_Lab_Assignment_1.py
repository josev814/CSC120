"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 5
Assignment: Lab Assignment 1
Date: 2020-09-22
"""


"""
In this programming assignment, you will write program that determine the price of circulate pizza and display the total price and tax. 
The radius of the pizza is equal to the size (1 for small, 2 for medium and 3 for large) multiplied by a factor of 1.15. 
The area of the pizza is 3.1414 multiplied by the square of the radius. 
The pizza area price is area multiplied by unit area price multiplied by the quantity ordered. 
The toppings price is the number of toppings multiplied by the price per topping multiplied by quantity ordered. 
The sale price is the sum of pizza area price and the toppings price. 
The total price is equal to the sale price plus tax. """

"""Your program should have the following (document each statement). Use your own variable names, preferably the camelCase style. 
Define a variable for the price per unit area and assign $0.55 to it. 
Define a variable for the price per topping and assign $1.25 to it. 
Define a variable for the constant in area and assign 3.1414 to it. 
Define a variable for the tax rate and assign 8.5% to it. 
Define a variable for the radius constant and assign 1.15 to it. 
Prompt the user to enter the pizza size (an integer) and assign to a variable. 
Write an expression for the pizza radius and assign to a variable. 
Write an expression for the pizza area and assign to a variable. 
Prompt the user to enter the number of toppings (an integer) and assign to a variable. 
Prompt the user to enter the quantity of pizza ordered (an integer) and assign to a variable. 
Write an expression for the pizza area price and assign to a variable. 
Write an expression for the toppings price and assign to a variable. 
Write an expression for the sale price and assign to a variable. 
Write an expression for the tax and assign to variable. 
Write an expression for the total price and assign to variable. 
Display the pizza area price (to two decimal places). 
Display the toppings price (to two decimal places. 
Display the sale price (to two decimal places). 
Display the tax (to two decimal places). 
Display the total price (to two decimal places). 
"""
PRICE_PER_UNIT = .55
PRICE_PER_TOPPING = 1.25
CONSTANT_IN_AREA = 3.1414
TAX_RATE = 8.5 / 100
RADIUS_CONSTANT = 1.15

while True:
    try:
        pizzaSize = int(input('Enter the size of pizza [1=small, 2=medium, 3=large]: '))
        break
    except ValueError:
        print('Please enter an integer for your pizza size')

pizzaRadius = pizzaSize * RADIUS_CONSTANT
pizzaArea = CONSTANT_IN_AREA * pizzaRadius**2

while True:
    try:
        numberOfToppings = int(input('Enter the number of toppings on your pizza: '))
        break
    except ValueError:
        print('Please enter an integer the number of toppings on your pizza toppings')

while True:
    try:
        pizzaCount = int(input('Enter the number of pizzas to order: '))
        break
    except ValueError:
        print('Please enter an integer for the number of pizzas to order')

pizzaAreaPrice = pizzaCount * pizzaArea * PRICE_PER_UNIT

toppingsPrice = numberOfToppings * PRICE_PER_TOPPING * pizzaCount

salesPrice = toppingsPrice + pizzaAreaPrice

taxPrice = salesPrice * TAX_RATE
totalPrice = taxPrice + salesPrice

print('The Pizza Area Price is $', round(pizzaAreaPrice, 2), sep='')
print('The price for the toppings is $', round(toppingsPrice, 2), sep='')
print('The sale price is $', round(salesPrice, 2), sep='')
print('The tax cost is $', round(taxPrice, 2), sep='')
print('The total is $', round(totalPrice, 2), sep='')
