"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 1
Assignment: TakeHome Exercise 2
Date: 2021-01-27
"""

"""Question: 1"""
speed = int(input('What is your current speed (mph): '))
if speed > 70:
    print('Slow Down!')
elif speed <= 20:
    print('Speed Up!')
else:
    print('Maintain the current speed!')

"""Question: 2"""
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
third_num = int(input('Enter the third number: '))

if first_num < second_num and first_num < third_num:
    smallest = first_num
elif second_num < third_num and second_num < first_num:
    smallest = second_num
else:
    smallest = third_num
print('The smallest number is ' + str(smallest))


"""Question: 3"""
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
third_num = int(input('Enter the third number: '))

if (first_num < second_num and first_num > third_num) or (first_num > second_num and first_num < third_num):
    median = first_num
elif (second_num < third_num and second_num > first_num) or (second_num > third_num and second_num < first_num):
    median = second_num
else:
    median = third_num
print('The median number is ' + str(median))
