"""
Write a Python program that can perform the following operations on list:

(1) Create a list named num1 that contains the elements below:

     1, 2, 3, 4, 5, 6

     then, print out list num1.

(2) Make a copy of the list num1, name the new list num2. Print out list num2.

(3) Modify the last element of list num2 to 0. Print out the lists num1 and num2.
"""

num1 = [1, 2, 3, 4, 5, 6]
print('The original num1:', num1)
num2 = [] + num1
print('The original num2:', num2)
num2[-1] = 0
print('The current num1:', num1)
print('The current num2:', num2)
