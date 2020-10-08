"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 7
Assignment: Homework
Date: 2020-10-07
"""

"""
Exercise 2, Page 203:
2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute.
Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25 and 30 minutes.
"""


print('Calories Burned (Exercise 2):')
calPerMin = 4.2
for min in range(10, 31, 5):
    print('At {} minutes, {} calories have been burned'.format(
        min, calPerMin * min
    ))

input('Press enter to continue to the next exercise:')
print()

"""
Exercise 3, Page 203:
Budget Analysis:
Write a program that asks the user to enter the amount that he or she has budgeted for a month.
A loop should then prompt the user to enter each of their expenses for the month and keep a running total.
When the loop finishes, the program should display the amount that the user is over or under budget.
"""


print('Budget Analysis (Exercise 3):')
TOTAL_EXPENSES = 0
monthly_budget = 0
while monthly_budget <= 0:
    try:
        monthly_budget = float(input('What is your monthly budget? $'))
        if monthly_budget <= 0:
            raise ValueError
        break
    except ValueError:
        monthly_budget = 0
        print('Bad value.  Use a positive float')

sentinel_end = 1
print('To stop entering expenses enter 0 are your expense.')
while sentinel_end != 0:
    try:
        expense = float(input('Enter an expense: $'))
        if expense == 0:
            sentinel_end = 0
        elif expense <= 0:
            raise ValueError
        TOTAL_EXPENSES += expense
    except ValueError:
        print('Bad value.  Use a positive float')

ou = ''
if TOTAL_EXPENSES > monthly_budget:
    ou = 'over'
else:
    ou = 'under'

print()
print('You have spent ${:.2f} of your ${:.2f} budget.  You are {} your budget. Remaining Budget: ${:.2f}.'.format(
    TOTAL_EXPENSES, monthly_budget, ou, monthly_budget - TOTAL_EXPENSES
))
input('Press enter to continue to the next exercise:')
print()

"""
Exercise 5, Page 204:
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
The program should first ask for the number of years.
The outer loop will iterate once for each year.
The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display 
    the number of months
    the total inches of rainfall 
    the average rainfall per month for the entire period
"""
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
print('Average Rainfall (Exercise 5):')
TOTAL_RAINFALL = 0
years = 0
while years <= 0:
    try:
        years = int(input('How many years would you like to calculate rainfall for? '))
        if years < 1:
            raise ValueError
    except ValueError:
        print('ERROR: Enter an integer for years')
        years = 0

for year in range(1, years+1):
    for m_idx in range(12):
        while True:
            try:
                rainfall = float(input('Enter the inches rainfall in year {} for {} '.format(year, MONTHS[m_idx])))
                if rainfall < 0:
                    raise ValueError
                TOTAL_RAINFALL += rainfall
                break
            except ValueError:
                print('ERROR: Bad value.  You must enter a positive integer or float')
                pass

print('The total inches of rainfall over {} months is {}".  The average rainfall per month for that period was {}"'.format(
    years*12,
    TOTAL_RAINFALL,
    TOTAL_RAINFALL / (years*12)
))
