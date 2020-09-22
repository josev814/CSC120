"""
Student: Jose' Vargas
Activity:
1. Define a list object that hold the grade point averages of 5 students 3.4, 4, 2.8. 3, 3.85
2. Change the gpa of the second student of the list object in (1) to 2.75
3. Change the gpa of the last student of the list object in (1) to 3.99. Use the negative index
4. Define a list object that will hold 20 random numbers ranging from 0 to 6
5. Use a for loop to display the list object in (4)
6. Use a for loop to count and display the number of times 5 appears in the list object in (4)
7. Define a list object to hold the items 29,23,34,23,45,67,23,12,34,56,23 and answer the following questions:
 a. Write a statement to display items with index between 3 and 7
 b. Write a statement to display the last three items using negative index
 c. Write a statement to display the first 3 items
 d. Write a statement to display all the items
 e. Write a statement to display items whose index values are odd
 f. Write a statement to display items whose index values are even
 g. Write a for loop to display items whose index values are divisible by 3
"""

import random
gradePointAverages = [3.4, 4, 2.8, 3.85]

gradePointAverages[1] = 2.75
gradePointAverages[-1] = 3.99
print('New GPAs are {}'.format(gradePointAverages))
randomList = [random.randint(0, 6) for i in range(20)]

for i in randomList:
    print(i)

fiveCount = 0
if 5 in randomList:
    for i in randomList:
        if i == 5:
            fiveCount += 1

print('The number 5 appeared {} time(s) in the randomList {}'.format(fiveCount, randomList))

newItems = [29, 23, 34, 23, 45, 67, 23, 12, 34, 56, 23]
print('Items between 3 and 7 in the list are {}'.format(newItems[3:7]))

print('The last 3 items in the list are {}'.format(newItems[-3:]))

print('The first 3 items in the list are {}'.format(newItems[:3]))
print('The list has these values {}'.format(newItems))
print('The odd index values in the list are {}'.format(newItems[::2]))
print('The even index values in the list are {}'.format(newItems[1::2]))
divisibleBy3 = []
temp = [divisibleBy3.append(val) for val in newItems if val % 3 == 0]
temp = None
print('The index values divisible by 3 in the list are {}'.format(divisibleBy3))
