"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 7
Assignment: Worksheet
Date: 2020-10-07
"""

"""
Write a while loop that will accept 5 integers from the user, display each number and its cube. 
"""
print('Exercise 1:')
increment = 1
while increment <= 5:
    user_int = int(input('{}: Enter an integer: '.format(increment)))
    print(user_int, ' cubed is ', user_int**3)
    increment += 1

input('Press enter to go to the next exercise')
print()


"""
Use a while loop to validate that an input value entered by a user is always between 0 and 100. 
"""
print('Exercise 2:')
is_valid = 'y'

while is_valid == 'y':
    try:
        user_int = int(input('Enter a number between 0 and 100: '))
        if user_int < 0 or user_int > 100:
            raise ValueError
    except ValueError:
        print("Error: Value wasn't between 0 and 100")
        is_valid = 'n'


input('Press enter to go to the next exercise')
print()


"""
Use a while loop to display the first 100 integers, their squares and cubes. 
"""
print('Exercise 3:')
last_int = 100
this_int = 0
while this_int <= last_int:
    print(this_int, 'has a square of', this_int**2, 'and a cube of', this_int**3)
    this_int += 1

input('Press enter to go to the next exercise')
print()



"""
Write a while loop that will display the first 20 Fibonacci numbers: 1,1,2,3,5,8,13, etc., 
where a number in the sequence (except the first two) is the sum of the two numbers before it. 
2= 1+1, 3=1+2, 5= 2+3, 8= 3+5, 13 = 5+8, etc. 
"""
print('Exercise 4:')
prev_int = 0
this_int = 1
loops = 0
fibonacci_numbers = []
while loops < 20:
    int_sum = prev_int + this_int
    fibonacci_numbers.append(prev_int + this_int)
    prev_int = this_int
    this_int = int_sum
    loops += 1
print('First 20 Fibonacci Numbers: ', fibonacci_numbers)
