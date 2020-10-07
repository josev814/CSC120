"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 6
Assignment: Homework
Date: 2020-09-28
"""

print('Algorithm Workbench: 1')
z = 0
y = 0
x = int(input('Type an integer to assign to variable x: '))
if x > 100:
    y = 20
    z = 40
print('y: {}, z: {}'.format(y, z), end='\n\n')

print('Algorithm Workbench: 2')
b = 1
c = 0
a = int(input('Type an integer to assign to variable a: '))
if a < 10:
    b = 0
    c = 1
print('b: {}, c: {}'.format(b, c), end='\n\n')

print('Algorithm Workbench: 5')
amount1 = int(input('Input the amount for 1: '))
amount2 = int(input('Input the amount for 2: '))
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)

print('Algorithm Workbench: 7')
points = float(input('What is the value of points? '))
if points >= 9 and points <= 51:
    print('Valid points')
else:
    print('Invalid points')


print('Programming Exercise: 15')
seconds = float(input('Enter a number of seconds: '))
if seconds > 86400:
    days = int(seconds / 86400)
    hours_remain = int(seconds % 86400)
    hours = int(hours_remain / 3600)
    minutes_remain = int((seconds % 3600))/60
    minutes = int(minutes_remain)
    newsec = int(seconds % 60)
    print('{}d {}:{}:{}'.format(days, hours, minutes, newsec))
elif seconds > 3600:
    hours = int(seconds / 3600)
    minutes_remain = int((seconds % 3600)) / 60
    minutes = int(minutes_remain)
    newsec = int(seconds % 60)
    print('{}:{}:{}'.format(hours, minutes, newsec))
elif seconds > 60:
    minutes = int(seconds / 60)
    newsec = int(seconds % 60)
    print('{}:{}'.format(minutes, newsec))
else:
    print(seconds)