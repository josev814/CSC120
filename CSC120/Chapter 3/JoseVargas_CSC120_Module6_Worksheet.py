"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 6
Assignment: Worksheet
Date: 2020-09-28
"""

"""Try to understand the if statement and if..else (single and dual alternatives).  

Write a program that will prompt the user to enter a string and assign to variable astring. 
The program will display “Your” + astring + “did not match the hidden string” if  astring does not match “Module” 

Write a program that will prompt the user to enter a string and assign to variable astring. 
The program will display “Your” + astring + “ matches the hidden string” if  astring does matches  “Module” 

Write a program that will prompt the user to two integers and assign to variables aNum and bNum. 
The program will calculate and display the maximum of the two numbers. Do not use the built-in function, write you own function. 

Write a program that will prompt the user to two integers and assign to variables aNum and bNum. 
The program will calculate and display the minimum of the two numbers. Do not use the built-in function, write you own function. 

Write a program that will prompt the user to enter a string representing the model of a car. 
If the string is “A” or “a”, the program will display $1200 as the price of the car, otherwise, display zero as the price.  

Write a function that will prompt the user to enter a string and assign to variable astring. 
The program will display “Your” + astring + “did not match the hidden string”  if astring matches the string “Module” otherwise, the program will display “Your” + string + “matches with the hidden string” 

Write a program that will prompt the user to enter two integers and assign to variables aNum and bNum. 
The program will display str(aNum) + “ is greater than “ + str(bNum)  
if aNum is greater than bNum, otherwise, the program will display str(aNum) + “ is less than or equal to “ + str(bNum). 
"""


astring = input('2a: Enter a string: ')
if astring != 'Module':
    print('Your {} did not match the hidden string'.format(astring))


astring = input('2b: Enter a string: ')
if astring == 'Module':
    print('Your {} matches the hidden string'.format(astring))


aNum = input('2c: Input integer a: ')
bNum = input('Input integer b: ')
if aNum > bNum:
    print(aNum)
else:
    print(bNum)


aNum = input('2d: Input integer a: ')
bNum = input('Input integer b: ')
if aNum < bNum:
    print(aNum)
else:
    print(bNum)


userCarModel = input('2e: Input the model of a car: ')
if userCarModel.strip()[0].lower() == 'a':
    print('The price of {} is $1200'.format(userCarModel))
else:
    print('The price of {} is $0'.format(userCarModel))


astring = input('2f: Enter a string: ')
if astring != 'Module':
    print('Your {} did not match the hidden string'.format(astring))
else:
    print('Your {} matches with the hidden string'.format(astring))


aNum = input('2g: Input integer a: ')
bNum = input('Input integer b: ')
if aNum > bNum:
    print('{} is greater than {}'.format(aNum, bNum))
else:
    print('{} is less than {}'.format(aNum, bNum))


"""Write a program that will prompt the user to enter raw score on a test and assign value to a variable score. 
Using the grading schedule below, display the user’s letter grade. 

Grade F: if score less than 40 
Grade D: if score between 40 and 59 inclusive 
Grade C: if score between 60 and 74 inclusive 
Grade B: if score between 75 and 89 include 
Grade A: if score greater than or equal to 90
"""

print('Exercise 4:')
testRawScore = float(input('Enter a raw score on a test: '))
if testRawScore < 40:
    print('Grade F')
elif testRawScore <= 59:
    print('Grade D')
elif testRawScore <= 74:
    print('Grade C')
elif testRawScore <= 89:
    print('Grade B')
else:
    print('Grade A')


def letter_grade_to_points(letter):
    smallLetter = letter.strip()[0].lower()
    if smallLetter == 'a':
        gradePoint = 4
    elif smallLetter == 'b':
        gradePoint = 3
    elif smallLetter == 'c':
        gradePoint = 2
    elif smallLetter == 'd':
        gradePoint = 1
    else:
        gradePoint = 0
    return gradePoint

"""
Write a program the will prompt the user to enter a letter grade for a test, assign the value to a variable grade. 
Using the grade, convert to point grade using the conditions as shown below. Display the user’s point grade. 

Point 4: if letter grade of A 
Point 3: if letter grade of B 
Point 2: if letter grade of C 
Point 1: if letter grade of D 
Point 0: if letter grade of F 
"""
print('Exercise 5:')
letterGrade = input('Enter a letter grade for a test: ')
gradePoint = letter_grade_to_points(letterGrade)
print('Point grade is ', gradePoint)


"""
Write a program the will prompt user to enter credits and point grade of three courses. 
Assign values to variables credits1, grade1, credits2, grade2, credit3, grade3. 
The program should calculate the gpa using 
gpa = (credits1*grade1 + credits2*grade2 + credits3*grade3)/(credits1+credit2 +credits3) 

The program should display the gpa in 2 decimal places and also display the ranking using the following: 
Excellent: if gpa is 3.5 and above 
Very Good: if gpa is greater than or equal to 2.75 and less than 3.5 
Good: if gpa is greater than or equal to 2.0 and less than 2.75 
Poor: if gpa is less than 2.0 
"""
print('Exercise 6:')
creditsGrades = []
for i in range(3):
    while True:
        try:
            credit = int(input('Enter credits for class {}: '.format(i)))
            break
        except ValueError:
            print('You must enter an integer')
    while True:
        try:
           grade = input('Enter letter grade for class {}: '.format(i))
           gradePoint = letter_grade_to_points(grade)
           break
        except ValueError:
            print('You must enter a number')
    creditsGrades.append({'credit': credit, 'grade': grade, 'grade_point': gradePoint, 'product': credit * gradePoint})

gpa = (creditsGrades[0]['product'] + creditsGrades[1]['product'] + creditsGrades[2]['product']) / \
      (creditsGrades[0]['credit'] + creditsGrades[1]['credit'] + creditsGrades[2]['credit'])

gpaClean = format(gpa, '3.2f')
if gpa >= 3.5:
    gpaRanking = 'Excellent'
elif gpa >= 2.75:
    gpaRanking = 'Very Good'
elif gpa >= 2.0:
    gpaRanking = 'Good'
else:
    gpaRanking = 'Poor'

print('{}: {}'.format(gpaRanking, gpaClean))
