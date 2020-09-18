import turtle  # needed for problem 2

"""
Problem 1:
"""
print('Activity 1:')
try:
    num1 = int(input("enter a value: "))
    num2 = int(input("Enter a value: "))
    print(num1, "/", num2, " is", num1 / num2)
except ZeroDivisionError:
    print('Invalid division by 0 for input 2, please try again')
    pass
except ValueError as v:
    print('Only use integers as your input')
    pass

"""
Problem 2:
"""
print('Activity 2:')


def step_update(p, q):
    x = (p * (1 + 1.3 * (1 - p))) - (.5 * p * q)
    y = (.3 * q) + (1.6 * p * q)
    return x, y


def turtle_setup(a, b):
    turtle.setworldcoordinates(0, 0, 2, 2)
    turtle.speed(0)
    turtle.color('red')
    turtle.penup()
    turtle.goto(a, b)
    turtle.pd()


def get_population(pop_for):
    try:
        population = float(input("Enter the population for " + pop_for + ": "))
    except ValueError as v:
        print('Only use floats as your input')
        print('Exiting the program')
    except UnboundLocalError as u:
        print('You must enter a value')
        print('Exiting the program')
    return population


def get_plot_point_qty():
    try:
        plot_points = int(input("Enter the number of points to plot: "))
    except ValueError as v:
        print('Only use integers as your input')
        print('Exiting the program')
    except UnboundLocalError as u:
        print('You must enter a value')
        print('Exiting the program')
    return plot_points


def run_plots(plot_points, a, b):
    for n in range(plot_points):
        a, b = step_update(a, b)
        # print('going to ', a, b) # a debug comment
        turtle.goto(a, b)


def logistic():
    a = get_population('a')
    b = get_population('b')
    turtle_setup(a, b)
    plot_points = get_plot_point_qty()
    run_plots(plot_points, a, b)


if __name__ == "__main__":
    logistic()
