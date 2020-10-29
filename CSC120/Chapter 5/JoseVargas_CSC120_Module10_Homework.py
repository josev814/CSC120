"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 10
Assignment: Homework
Date: 2020-10-28
"""

"""
Write a program that asks the user to enter 5 test scores
The program should display a letter grade for each score and the average test score.
Write the following function in teh program
calc_average:
    This function should accept five test scores as arguments and return the average of the scores
determine_grade:
    This function should accept a test score as an argument and return a letter grade for the score based on the following scale
    90-100 = A
    80-90 = B
    70-79 = C
    60-69 = D
    <60 = F
"""


def start_grading():
    test_scores = []
    for i in range(5):
        test_scores.append(get_test_grade(i+1))
    for i in range(len(test_scores)):
        print('Test {}: {} - {}'.format(
            i+1,
            determine_grade(test_scores[i]),
            test_scores[i]
        ))
    avg = calc_average(test_scores[0], test_scores[1], test_scores[2], test_scores[3], test_scores[4])
    grade = determine_grade(avg)
    print('The Average of all the grades is {} - {:.0f}'.format(grade, avg))


def get_test_grade(tst):
    graded = False
    while not graded:
        try:
            grade = float(input('Input grade for test {}: '.format(tst)))
            if grade > 100 or grade < 0:
                raise ValueError
            graded = True
        except ValueError:
            print('ERROR: Invalid grade.  The grade must be between 0 - 100')
    return grade


def determine_grade(score):
    grade = 'F'
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    return grade


def calc_average(t1, t2, t3, t4, t5):
    avg = (t1 + t2 + t3 + t4 + t5)/5
    return avg


if __name__ == '__main__':
    start_grading()
