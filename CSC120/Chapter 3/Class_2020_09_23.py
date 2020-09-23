"""
Control Structures
- sequence
    Line after line executed in sequential order
    - ex:
        statement1
        statement2
        statement3
- decision / selection
    3 types of control structures
    - single alternative
      A condition is tested and if the condition is true the program will execute a set of statements
      then the execution returns to the flow of the program
      - ex:
        if a > b: # this is an if clause
          execute statement
    - dual alternative
      A condition is tested and if the condition is true the program will execute a set of statements
      if the condition is not true another section of statements will be executed
      then the execution returns to the flow of the program
      - ex:
        # this is an if, elif clause
        if a > b:
          execute statement
        elif a == b:
          execute other statement
    - multiple alternative
      A condition is tested and if the condition is true the program will execute a set of statements
      Another condition is tested and if that condition is true the program will execute those set of statements
      - this can continue for however many conditions need tested
      if the condition is not true another section of statements will be executed
      then the execution returns to the flow of the program
      - ex:
        # this is an if, elif clause
        if a > b:
          execute statement
        elif a == b:
          execute a different statement
        else:
          execute a statement
- repitition
    for loops and while loops

Today's class is on the decision control structure
LucidChart Diagram:
    https://app.lucidchart.com/invitations/accept/727fb212-aa39-4b54-b0c3-4c8c4dd19469

A Boolean expression (condition) is defined using relational operators).
Relational operators (binary operators - they accept two operands):
less than >
greater than >
greater than or equal to >=
less than or equal to <=
equal to ==
does not equal !=

checking bool of a value
bool(variable)
if the variable = 0 or an empty string it will be False
"""


x, y, z = 9, 87, 45
print(x == z)  # outputs False
print(x != z)  # true
print(5*x == z)  # true
# arithmetic operators take precedence over relational operators

x, y, z = 10, 87, 50
if x != z:  # the condition is True
    print('The condition is True')

if x == y:  # The condition is False
    print('2: The condition is True')

# Write a program that will prompt the user to enter a word
# The program will test if the word entered is Password
# If it's True, the program will display "Your word is a match"
user_val = input('Enter a value? ')
if user_val == 'Password':
    print('Your Word is a match.')

"""
    Write a program that will prompt the user to enter a monthly salary
    The program should calculate the tax using
    The tax is 5% of the salary if it is greater than or equal to 2000
    Otherwise the tax is zero
"""
tax_rate = 0
taxed = 0
salary = float(input('What is your Monthly salary? $'))
if salary >= 2000:
    tax_rate = .05
    taxed = salary * tax_rate
print('The taxed amount of the salary is ', taxed)

##########################
# Dual Alternative Decision Structure
"""
    if..else statement
    if condition:
      True_Block
    else:
      False_Block
"""
##########################
exercise = 'Dual Alternative Decision Structure'
print('Start Exercise:', exercise)
x, y, z = 56, 89, 30
if x > y:
    print(x, 'is greater than', y)
else:
    print(x, 'is not greater than', y)

if x - 26 == z:
    print('True Block')

"""
    Write a program that will prompt the user to enter a word
    The program will display "Your word matches the password"
    otherwise your word does not match
"""

user_val = input('Enter your password? ')
if user_val == 'Broncos':
    print('Your word is a match.')
else:
    print('Your word does not match')


"""
    Write a program that will prompt the user to enter monthly salary
    The program will calculate and display the tax and net pay as follows
    the tax_rate is 5% is the salary is less than 3000
    otherwise the tax rate is 8.75%
"""

tax_rate = .0875
salary = float(input('What is your Monthly salary? $'))
if salary < 3000:
    tax_rate = .05
taxed = salary * tax_rate
net_salary = salary - taxed
print('The taxed amount of the salary is ', taxed)
print('The net pay amount is ', net_salary)
print('Done Activity:', exercise)

"""
    3 Boolean operators
    and operator (binary), has 2 operands
        leftExpression and rightExpression
        if leftExpression and rightExpression is True, then the if expression is True, otherwise it is False
    or operator (binary), has 2 operands
        if leftExpression or rightExpression is False, then the if expression is False, otherwise it is True
    not operator (unary), has 1 operand
        if the rightExpression is False, then the if expression is True, Otherwise it is False
    
    Boolean operators are used to define compound expressions
    The and/or operator uses short circuit evaluation
        if the leftExpression is False in the and evaluation, it's not necessary to evaluate the rightExpression
        if the leftExpression is True in the or evaluation, it's not necessary to evaluate the rightExpression
"""
x, y, z = 4, 5, 45
print(z % 5 == 0 and x < 3)  # False, because x(4) is not less than 3
print(bool(x and y))  # True, because the output is y (5) which is greater than 0
print(z == 9*5 or y == 6)  # True, because 9*5 = z



"""
Multiple alternative decision (nested if statement)
if..elif..else statement
This is an if statement within another if statement
if condition1:
    execute_block_1
elif condition2:
    execute_block_2
elif conditionN:
    execute_block_N
else:
    execute_false_block # executes when all conditions fail
"""
