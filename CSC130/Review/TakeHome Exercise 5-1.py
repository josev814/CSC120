"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 1
Assignment: TakeHome Exercise 5-1
Date: 2021-02-01
"""
"""Question 1"""
"""result = subtract(8, 5)"""


"""Question 2"""
"""def calc_avg(num1, num2, num3):
    avg = (num1, num2, num3)/3
    print(avg)
"""

"""Question 3"""
def mul(num1, num2):
    prod = num1 * num2
    print(prod)

def main():
    n1 = int(input('Input a number: '))
    n2 = int(input('Input another number: '))
    mul(n1, n2)

main()

"""Question 4"""
def mul(num1, num2):
    prod = num1 * num2
    return prod

def main():
    n1 = int(input('Input a number: '))
    n2 = int(input('Input another number: '))
    prod = mul(n1, n2)
    print(prod)

main()