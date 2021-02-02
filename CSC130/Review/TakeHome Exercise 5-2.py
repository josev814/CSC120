"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 1
Assignment: TakeHome Exercise 5-2
Date: 2021-02-02
"""
"""Question 1"""
"""Write a Python program which performs the following tasks:

(1) define the calculate function which has one parameter num. 
    It calls the math module's sqrt function to calculate the square root value of the parameter num, 
    then it returns the result.
(2) define the main function which firstly calls the random module's randint function to generate a random integer number between 10 and 99 (inclusive). 
    Then, it calls the calculate function and pass over the generated integer number as argument. 
    The returned value should be printed out in the main function.
(3) Execute the program by calling the main function.
"""
from math import sqrt
from random import randint


def calculate(num):
    return sqrt(num)


def main1():
    integer = randint(10, 99)
    print('The generated number is ', integer)
    print('The returned square root value is ', calculate(integer))


main1()

"""Question 2"""
"""
Write a Python program which performs the following tasks:
(1) Define the determine_grade function which has one parameter score. 
    It will determine the letter grade based on the parameter score using the following grading scale. 
    The letter grade should be returned.
        Score	Letter Grade
        90-100	A
        80-89	B
        70-79	C
        60-69	D
        Below 60	F
(2) Define the main function 
    which firstly calls the random module's randint function to generate a random score between 0 and 100 (inclusive). 
    Then, it calls the determine_grade function and pass over the generated score as argument. 
    The returned value should be printed out in the main function.
(3) Execute the program by calling the main function.
"""
def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def main():
    score = randint(0, 100)
    grade = determine_grade(score)
    print('The generated score is ', score)
    print('The corresponding letter grade is ', grade)


main()
