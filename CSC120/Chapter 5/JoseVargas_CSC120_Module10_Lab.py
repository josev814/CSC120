"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 10
Assignment: Lab
Date: 2020-10-29
"""

"""
Let us write a simple game that involve rolling two six-sided dice.  
Each player takes a turn to roll two dice. 
At each turn, the sum of the two numbers rolled is added to the player’s bank. 
The player whose bank reaches the maximum value= 100 first wins.  
Assume that there are two players and that they are both computers 
    (i.e., when it is a player’s turn to play, the program should roll two dice and add to the player’s bank). 
The banks are initially set to 0. 
The players can play as many rounds as they desire, 
    where round is group of turns until one of the player wins and which point, 
    the banks are reinitialized to 0. 
You should keep counts of how many rounds and how many times each player wins. 


Identify all the functions: 
    A function that will generate two random numbers between 1 and 6 and return their sum. 
    A function that will accept as input the player’s code 
        (0 for computer and 1 for player) 
        and return True if a player wins and False otherwise. 
        Be sure to update player’s win counts 
    A function that will update the bank by adding the sum of rolled dice. 
    A function that will return a string that welcomes the player to the game: 
        Welcome to the Game of DICE. 
        When it is your turn to roll dice, you only need to press Enter key. 
        The values of the rolled dice and your current bank balance will display. Enjoy!” 
    A function to play the game. 
        This function will use a while loops for ending the game and for ending each round. 
    A function main that will serve as a driver for the program if needed 
Use other functions as needed. 

Identify the global variables and constants 

MAXIMUM_BANK_VALUE = 100 
Bank_0, Bank_1 for bank balances 
Wins_0, Wins_1 for win counts 

Identify local variables for each function (if any).  
Identify inputs (if any), describe the process and the output (if any). 

For example, 

die_1 and die_2 are local variables in rollDice function, 
compute the sum of the two dice (process) and return the sum as output 

def rollDice(): 
    die_1 = randint(1,6) 
    die_2 = randint(1,6) 
    return die_1 + die_2 

Include documentation as necessary. 
"""
import random

MAX_BANK_VAL = 100
players = [
    {'bank': 0, 'wins':0},
    {'bank': 0, 'wins':0}
]


def play_game(players):
    """
    The main function that plays the game
    :param players:
    :return:
    """
    display_welcome()
    keep_playing = is_true(get_play_input())
    while keep_playing:
        players = play_rounds(players)
        keep_playing = play_again()
        players = reset_banks(players)
    display_results(players)


def display_welcome():
    """
    Prints the welcome message
    :void:
    """
    print("""Welcome to the Game of DICE.""", '\n\n')


def play_rounds(players):
    """
    This will play the user turn rounds until a user has reached the max bank val
    :param players:
    :return list:
    """
    winner = False
    while not winner:
        players = play_round(players)
        if players[0]['bank'] > MAX_BANK_VAL:
            # player 1 won
            display_round_winner('Player 1')
            winner = True
            update_wins(players[0])
        elif players[1]['bank'] > MAX_BANK_VAL:
            # player 2 won
            display_round_winner('Player 2')
            winner = True
            update_wins(players[1])
    return players


def play_round(players):
    """
    loop over the users playing and perform a turn
    we return the updated player results
    :param players:
    :return dict:
    """
    for idx in range(len(players)):
        players[idx] = user_turn(players[idx])
    return players


def user_turn(user):
    """
    Perform a user turn of rolling the dice and updating the bank balance
    :param user:
    :return dict:
    """
    dice_val = roll_dice()
    user = update_bank(user, dice_val)
    return user


def display_round_winner(user):
    """
    This function displays the winner of the round
    :param user:
    :return:
    """
    print('{} reached {} first.'.format(user, MAX_BANK_VAL))


def play_again():
    """
    This function checks if we should play again or not
    :return bool:
    """
    keep_playing = get_play_input(again=True)
    if is_true(keep_playing):
        return True
    return False


def display_results(players):
    """
    This function displays the win result of all the rounds played by the users
    :param players:
    :return:
    """
    played = False
    for idx in range(len(players)):
        if players[idx]['wins'] > 0:
            played = True
            break
    if played:
        print(end='\n\n\n')
        print('###  RESULTS ###')
        for idx in range(len(players)):
            times = 'time'
            if players[idx]['wins'] > 1:
                times = 'times'
            print('Player {} won {} {}.'.format(idx, players[idx]['wins'], times))
        print('', """Thank you for Playing""", sep='\n')
    else:
        print("""Maybe next time""")


# Getters
def roll_dice():
    """
    Rolls 2 die and returns the sum of the die
    :local_variables rolls:
    :return int:
    """
    rolls = []
    for i in range(0, 2):
        rolls.append(roll_die())
    return sum(rolls)

def roll_die():
    """
    Rolls a die and returns the value
    :return int:
    """
    return random.randint(1,6)


def is_true(check):
    """
    Checks if the check param is set to our definition of True
    :param check:
    :return bool:
    """
    if check == True or check.lower() in ['y', 'yes']:
        return True
    return False

def get_play_input(again=False):
    """
    Gets user input on whether to play a round or not and returns the value entered
    :local_variables play valid_input:
    :return string:
    """
    valid_input = False
    while not valid_input:
        try:
            if not again:
                play = input('Would you like to play a round [y|n]? ')
            else:
                play = input('Would you like to play another round [y|n]? ')
            if play.lower() not in ['y','n']:
                raise ValueError
            valid_input = True
        except ValueError:
            print('\n\n')
            print('ERROR: You must enter either y or n', end='\n\n')
    del valid_input
    return play


# Setters
"""
Functions that set/update data
"""
def reset_banks(players):
    """
    Resets each players bank
    :param players:
    :return:
    """
    for idx in range(len(players)):
        players[idx]['bank'] = 0
    return players


def update_bank(banker, dice_value):
    """
    Updates the banker's balance with the rolled dice value
    :param banker:
    :param dice_value:
    :return dict:
    """
    banker['bank'] += dice_value
    return banker


def update_wins(player):
    """
    updates the player's win count
    :param player:
    :return dict:
    """
    player['wins'] += 1
    return player


"""
if __main__ is called invoke the game
"""

if __name__ == '__main__':
    play_game(players)