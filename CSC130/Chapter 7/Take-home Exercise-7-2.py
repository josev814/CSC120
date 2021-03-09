"""
Write a program that firstly defines a list and initialize it with the following numbers:

1, 2, 3, 4, 5, 6

Then, use a for loop to iterate over each element by their index numbers, and raise each element to the power of 2 (modify each element's value to its square). Finally, print out the modified list.

Q1 - list square.PNG
"""

mylist = [1, 2, 3, 4, 5, 6]
print('The original list is', mylist)
for i in range(len(mylist)):
    mylist[i] = mylist[i]**2

print('The modified list is', mylist)


"""
Write a program which performs the following tasks

(1) define a list named num1 and initialize it with the following values:

'yes', 20, 30, 40, 50, 'no'

(2) modify the first element to 10 using the corresponding positive index, and modify the last element to 60 using the corresponding negative index. Print the modified list num1.

(3) create another list named num2 which has three elements 70, 80, 90. Then, concatenate num2 to the back of num1, so that num1 is extended. Print the extended list num1.

Q2 - list operations part1.PNG
"""

num1 = ['yes', 20, 30, 40, 50, 'no']
print('The original list is', num1)
num1[0] = 10
num1[-1] = 60
print('The modified list is', num1)
num2 = [70, 80]
num1 += num2
print('The extended list is', num1)

"""
Write a program that firstly defines a list and initialize it with the following numbers:

11, -22, 33, -44, 55, -66

Then, use a for loop to find out all elements with a negative numeric value, and change the values of those elements to their respective index numbers. Finally, print out the modified list.
"""
mylist = [11, -22, 33, -44, 55, -66]
print('The original list is', mylist)
for i in range(len(mylist)):
    if mylist[i] < 0:
        mylist[i] = i
print('The modified list is', mylist)
