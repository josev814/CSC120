"""
Professor: Longfei Wu
Student: Jose' Vargas
Class: CSC 130
Module: 1
Assignment: TakeHome Exercise 4-2
Date: 2021-01-30
"""
"""Question 1"""
running_total = 0
lower_limit = int(input('What is the lower limit of the range? '))
upper_limit = int(input('What is the upper limit of the range? '))
for i in range(lower_limit, upper_limit + 1):
    running_total += i
print('The total value is {}'.format(running_total))



"""Question 2"""
def get_sqr_val(number):
    num_sqr_val = number**2
    return num_sqr_val


def finished(val):
    if val.strip().lower() == 'finish':
        return True
    return False


finish = False
question = 'Enter a Number or finish to stop: '
while not finish:
    get_number = input(question)
    finish = finished(get_number)
    if not finish:
        print('The square of {} is {:.0f}'.format(get_number, get_sqr_val(int(get_number))))


"""Question 3"""
"""
Write a Python program that takes one test score entered by the user. 
Use input validation loop to check the validity of user input. 
A valid score should be within the range of 0 and 100 (inclusive). 
If the entered score is valid, print Your score is accepted; 
otherwise, repeatedly issue warnings to the user and ask the user to re-enter until a valid score is entered.
"""

question = 'Enter your score: '
reenter_question = 'Re-Enter your score: '
score = input(question)
invalid = True
while invalid:
    try:
        score_int = int(score)
        if score_int >= 0 and score_int <= 100:
            print('Your score is accepted')
            invalid = False
        else:
            raise ValueError
    except ValueError:
        print('ERROR: invalid score')
        score = input(reenter_question)


"""Question 4"""
def finished(val):
    if val.strip().lower() == 'finish':
        return True
    return False


finish = False
question = "Enter a Number or 'finish' to stop: "
running_total = 0
while not finish:
    get_score = input(question)
    finish = finished(get_score)
    if not finish:
        running_total += int(get_score)
print('The total is {}'.format(running_total))
