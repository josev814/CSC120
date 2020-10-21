"""Programming Exercise #20 (page 263)"""
import random


def number_to_guess():
    return random.randint(1, 100)


def get_user_guess():
    user_guess = 0
    while user_guess < 1 or user_guess > 100:
        try:
            user_guess = int(input('Guess the number(int) between 1 and 100: '))
        except ValueError:
            print('You must enter an integer between 1 and 100')
            user_guess = 0
    print(user_guess)
    return user_guess


def check_guess(guess, num):
    if guess > num or guess < num:
        if guess > num:
            print('Your guess was too high')
        else:
            print('Your guess was too low')
        return False
    else:
        print('You got it!!')
    return True


def keep_playing():
    while True:
        try:
            cont = input('Would you like to keep playing? [y|n] ')
            if cont == 'y':
                cont = True
                break
            elif cont == 'n':
                cont = False
                break
            else:
                raise ValueError
        except ValueError:
            print('You must enter y or n')
    return cont


def game():
    playgame = True
    while playgame:
        guessed_int = False
        guesses = 0
        num = number_to_guess()
        while guessed_int is False:
            user_guess = get_user_guess()
            guessed_int = check_guess(user_guess, num)
            guesses += 1
        print('It took you {} guesses to get the number'.format(guesses))
        playgame = keep_playing()
        print(playgame)


if __name__ == '__main__':
    game()
