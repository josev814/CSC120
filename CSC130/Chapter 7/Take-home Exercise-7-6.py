"""
Write a Python program which performs the following tasks:

(1) Define the avg function which has one parameter my_list. It calculates the average value of the elements in the parameter my_list (a list object). The average value is returned.
(2) Define the main function which firstly creates a list with the following numbers as elements: 3, 6, 7, 2, 5, 2, 9, 1, 8, 4.
    Then, it calls the avg function and pass over this list.
    The returned value will be printed in the main function.
(3) Execute the program by calling the main function.
"""


def avg(calc_list):
    list_count = len(calc_list)
    run_total = 0
    for item in calc_list:
        run_total += item
    return run_total / list_count


def main():
    mylist = [3, 6, 7, 2, 5, 2, 9, 1, 8, 4]
    list_avg = avg(mylist)
    print('The average value of all the elements in the list is', list_avg)


main()
