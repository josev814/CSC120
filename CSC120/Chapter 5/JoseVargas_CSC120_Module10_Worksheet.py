"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 10
Assignment: Worksheet
Date: 2020-10-28
"""

"""
Activity 

In this Activity, you will write a program to play the Game of Craps. 
The game of craps is played as follows: 
    a player rolls two dice. 
    If the sum is 2, 3, or 12, the player loses; 
    if the sum is either a 7 or an 11, the player wins. 
    If the outcome is anything else, the player continues to roll the dice until he rolls either the initial outcome or a 7. 
    If the 7 comes first the player loses, whereas if the initial outcome reoccurs before the 7 appears, the player wins. 
    Display how many times the player wins after playing for 200 times. 

Use functions and global variables as needed. Steps involved: 
roll two dice and add their values to a variable dice. 
if dice is 2, 3 or 12, 
    the player loses 
    and the game ends unless the player wants to play again. 
if the dice is 7 or 11, 
    the player wins 
    and the game ends unless the player wants to play again 
if the dice is 4,5,6,8,9 or 10, repeatedly do the following: 
    roll two dice and add their values to a variable point 
    if point is equal to dice, the player wins and the game ends 
    if point is equal to 7, the play loses and the game ends 

Here is sample output after the player has played 39 times. 
You played 39 times, and you won 18 times 
"""

import random

ROUNDS = 200


def start_craps():
    won = 0
    played = 0
    while played < ROUNDS:
        roll = roll_dies()
        if player_won(roll):
            won += 1
        elif player_lost(roll):
            pass
        else:
            new_roll = point_rolls(roll)
            if new_roll:
                won += 1
        played += 1
    print('You won {} out of {} games.'.format(won, ROUNDS))


def point_rolls(match_roll):
    new_roll = 0
    while new_roll != match_roll and new_roll != 7:
        new_roll = roll_dies()
    if new_roll == match_roll:
        return True
    return False


def roll_dies():
    d1 = roll_die()
    d2 = roll_die()
    return d1 + d2


def roll_die():
    return random.randint(1, 6)


def player_lost(die_val):
    if die_val in [2, 3, 12]:
        return True
    return False


def player_won(die_val):
    if die_val in [7, 11]:
        return True
    return False


if __name__ == '__main__':
    start_craps()
