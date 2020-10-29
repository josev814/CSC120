"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 9
Assignment: Worksheet
Date: 2020-10-22
"""

# ATM Example

"""
A typical ATM machine will allow a bank customer to perform the following tasks:  

Set the initial balance to $1000  
Display Welcome Greetings  
Display Menu to indicate transaction types-balance inquiry, withdraw, deposit  
Execute balance inquiry by displaying the current balance  
Execute withdraw by asking the user for amount to withdraw and display balance after withdrawal. 
Display INSUFFICIENT FUNDS if the user entered an amount larger than the balance  
Execute deposit by asking the user the amount to deposit and display balance after the deposit  

Identify all functions needed to implement simulate ATM machine  
Write all functions, providing the necessary codes. 
The menu should allow the user to continue to use the ATM until the user decided to exit or quit the program. 
You would need to use a while loop for the menu function. 
The main function should include calls to the function that displays the welcome greetings and the menu function. 
Choose function names following the naming convention. A function should have just few statements. 
Describe what each function does using comment statements.  
Use top-down approach by including relationships amongst all functions. 
For example: the menu will call several functions, for examples, 
    it should call a function that will display the menu text and return the integer that the user entered:  

Enter 0 to Exit  
Enter 1 for Deposit  
Enter 2 for Withdraw  
Enter 3 for Balance Inquiry  
Please, enter number--->2  

and another function that will validate the number the user entered. 
Any number other than 0,1,2,3 will be rejected and if that occurs, 
    the function should display “Oops Invalid Number” and return to the menu.  
"""

balance = 1000.0
MAIN_MENU = {
    0: 'Exit',
    1: 'Deposit',
    2: 'Withdraw',
    3: 'Balance Inquiry'
}

BALANCE_INQ_MENU = {
    0: 'Back'
}


def welcome():
    print("""##########################
Welcome to the UNCFSU ATM
##########################""", end='\n\n')


def bye():
    print(end='\n\n')
    print("""###################################
Thank you for using the UNCFSU ATM
###################################""", end='\n\n')


def display_menu(options):
    for key in options:
        print('{}: {}'.format(key, options[key]))
    print()

def main_menu():
    display_menu(MAIN_MENU)


def get_user_menu_input(valid_options):
    user_entry = -1
    while user_entry < 0:
        try:
            user_entry = int(input('Enter a menu option: '))
            if user_entry < 0 or user_entry not in valid_options:
                user_entry = -1
                raise ValueError
        except ValueError:
            print()
            print('Error: You must enter a valid menu option ({})'.format(valid_options))
    return user_entry


def get_deposit_withdraw_input(method):
    invalid_request = True
    while invalid_request:
        try:
            change = float(input('Enter the amount to {}: '.format(method)))
            if change < 0:
                raise ValueError
            invalid_request = False
        except ValueError:
            print()
            print('Error: You must enter a valid {} amount'.format(method))
    return change


def deposit_menu():
    deposit = get_deposit_withdraw_input('deposit')
    return deposit


def withdrawal_menu():
    withdraw = get_deposit_withdraw_input('withdraw')
    return withdraw


def update_balance(balance, qty, oper='add'):
    if oper == 'add':
        balance += qty
    else:
        if qty > balance:
            print('INSUFFICIENT FUNDS', end='\n\n')
        else:
            balance -= qty
    return balance


def balance_inquiry(balance):
    print('Your current balance is ${:.2f}'.format(balance))
    display_menu(BALANCE_INQ_MENU)
    get_user_menu_input(list(BALANCE_INQ_MENU.keys()))


def run_atm(balance):
    exit_atm = False
    welcome()
    while exit_atm is False:
        main_menu()
        main_menu_input = get_user_menu_input(list(MAIN_MENU.keys()))
        if main_menu_input == 0:
            exit_atm = True
        elif main_menu_input == 1:
            deposit = deposit_menu()
            balance = update_balance(balance, deposit)
            print('Your current balance is {}'.format(balance), end='\n\n')
        elif main_menu_input == 2:
            withdraw = withdrawal_menu()
            balance = update_balance(balance, withdraw, 'sub')
        else:
            balance_inquiry(balance)
    bye()


if __name__ == '__main__':
    run_atm(balance)