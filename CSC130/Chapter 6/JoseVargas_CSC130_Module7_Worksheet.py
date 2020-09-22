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
