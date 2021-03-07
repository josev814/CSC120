"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 12
Assignment: Worksheet 2
Date: 2020-11-10
"""

"""
Activity 
    You are provided with two text files names.txt and scores.txt.
    The names.txt contains first names only of players of a table game.
    The scores.txt contains players’ names and scores.
    Players can play game multiple times.
    The goal of the project is to 
        write a program that will read a player’s name from names.txt, 
        search for the player in scores.txt 
        and total the scores for the player 
        and calculate the average score. 
        Write the 
            player’s name, 
            total and 
            average scores to another file, 
            name the file report.txt 

Identify variables that you will need for the program 
    e.g., stdName and playScore 

All your code must be contained in a single function, e.g., studentReports 

Open the three files and use loops to read records in names.txt and scores.text. 
    For every record in names.txt, 
        read each record in scores.txt 
        and using running total to obtain the 
        total scores and number of plays 
        and calculate the average score 
"""
import os

NAMES_FILE = 'names.txt'
SCORES_FILE = 'scores.txt'
REPORT_FILE = 'report.txt'


def generate_student_reports():
    separator = None
    write_header = True
    with open(REPORT_FILE, 'w') as rfh:
        with open(NAMES_FILE, 'r') as nfh:
            for name_line in nfh:
                name = name_line.rstrip('\n')  # get the name of the current user to tabulate the scores for
                total_score = 0
                total_rounds = 0
                with open(SCORES_FILE, 'r') as sfh:
                    for score_line in sfh:
                        if separator is None:  # detecting the file's separator
                            separator = ' '
                            if '\t' in score_line:
                                separator = '\t'
                            elif ',' in score_line:
                                separator = ','
                        score_line_list = score_line.rstrip('\n').split(separator)
                        if score_line_list[0] == name:  # checking that the line is for the current user
                            total_score += int(score_line_list[1])  # round score is the second column in the file
                            total_rounds += 1
                if write_header:
                    rfh.write('Name{}Total{}Average\n'.format(separator, separator))
                    write_header = False
                average_score = total_score / total_rounds
                rfh.write('{}{}{}{}{}\n'.format(name, separator, total_score, separator, average_score))


def main():
    if not os.path.exists(NAMES_FILE):
        print('{} was not found.  Generating it now'.format(NAMES_FILE))
        generate_names_file()
    if not os.path.exists(SCORES_FILE):
        print('{} was not found.  Generating it now'.format(SCORES_FILE))
        generate_scores_file()
    generate_student_reports()


def generate_names_file():
    names = ['Daniel', 'Tyrese', 'Kameron', 'Chan', 'Joshua', 'Vincent', 'Carley', 'Ernie', 'Dejuan', 'Brittney',
             'Aryssa', 'Jefari', 'Tivon', 'Nikole', 'Sean', 'Alyse\'a', 'Marcia', 'Dasia', 'Justice', 'Avalon',
             'Jalea', 'Aliahya', 'Zavion', 'N\'aiyah', 'Jasmine', 'Kyle', 'Stephen', 'Jose', 'Lydia']
    with open(NAMES_FILE, 'w') as nfh:
        for name in names:
            nfh.write('{}\n'.format(name))


def generate_scores_file():
    from random import randint
    rounds = randint(2, 10)
    with open(SCORES_FILE, 'w') as sfh:
        for i in range(rounds):
            with open(NAMES_FILE, 'r') as nfh:
                for name in nfh:
                    played_round = randint(0, 1)
                    if played_round:
                        sfh.write('{}\t{}\n'.format(name.strip(), randint(1, 12)))


if __name__ == '__main__':
    main()
