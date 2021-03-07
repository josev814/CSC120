"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 12
Assignment: Homework
Date: 2020-11-10
"""

"""
Algorithm Workbench Exercise #1 (page 339) 
    Write a program that 
        opens an output file with the filename my_name.txt, 
        writes your name to the file, 
        then closes the file 

Programming Exercise #1 (page 340) 
    File Display: Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
    Write a program that displays all of the numbers in the file. 
"""


def algorithm_workbench_1():
    print('Generating my_name.txt')
    with open('my_name.txt', 'w') as fh:
        fh.write("""Jose' Vargas""")
    # no need for fh.close since the with clause handles that gracefully


def programming_exercise_1():
    from os.path import exists as file_exists
    numbers_file = 'numbers.txt'
    if not file_exists(numbers_file):
        create_numbers_file(numbers_file)
    with open(numbers_file, 'r') as nfh:
        for line in nfh:
            print(line.rstrip('\n'))


def create_numbers_file(filename):
    from random import randint
    with open(filename, 'w') as fh:
        for i in range(10):
            fh.write('{}'.format(randint(1, 100)))


def main():
    algorithm_workbench_1()
    programming_exercise_1()


if __name__ == '__main__':
    main()
