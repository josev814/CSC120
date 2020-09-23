"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 5
Assignment: Lab Assignment 2: Treadmill Display
Date: 2020-09-22
"""


"""
A treadmill has a screen that displays speed, distance, time in minutes and seconds, calories and a figure of bars. 
The complete figure of 16 bars is shown after so many minutes that form a cycle. 
The cycle time is dependent on the speed level. 
There are two speed levels on the treadmill, 2.5 miles per hour and 3.5 miles per hour. 
The user is expected to change from one speed level to the other. 
The distance is dependent on the speed and the total time for specific speed level. 
The user must first set the speed level at 2.5mph before 3.5mph.  

The acceleration (a) is calculated using the formula: 
a=(v−v0)/t
 
Where t is the elapsed time in minutes, v0 (0 or 2.5mph) is the start speed and v is speed (2.5mph or 3.5mph). 
Speed level 2.5mph has a start speed of 0mph and speed level 3.5mph has a start speed of 2.5mph. 

The distance is calculated using the formula: 
d = v0t + (at^2) / 2
for every speed level at speed level 2.5mph, v0 = 0 
at speed level 3.5mph, v0 = 2.5mph. 

The number calories (k) is calculated using the formula: 
k= (t(0.175v+0.9vg)w) / 440
Where w is the weight in pounds
g is the incline level in percent with 0 for no incline and 1 for the maximum incline. 

The total number of bars is calculated using: 
b = (4.5t1+5t2) / 16 
where t1 is the time duration at speed level 2.5mph and t2 is the time duration at speed level 3.5mph. 
Note the final number of bars is an integer or a whole number. 

You should write a program that will display the following given the time durations spent at the two speed levels, 
the weight of the user and the incline level: 
1. The total distance: td = d1 + d2, d1 is the distance at speed level 2.5mph and 
   d2 is the distance at speed level 3.5mph calculated using the formula above. 
2. The total calories: tc = c1 + c2, c1 is the calories at speed level 2.5mph and 
   c2 is the calories at speed level 3.5mph using the formula above. 
3. The total number of bars (b) using the formula above. 

In your program you should have the following and other statements that you feel are necessary. 
1. Define a variable for speed level 2.5mph and assign the value 2.5 to it. 
2. Define a variable for speed level 3.5mph and assign the value 3.5 to it. 
3. Prompt the user to enter the time duration for speed level 2.5mph and assign the value to a variable. 
4. Prompt the user to enter the time duration for speed level 3.5mph and assign the value to a variable. 
5. Prompt the user to enter weight in pounds and assign value to a variable. 
6. Prompt the user to enter the incline level that is between 0 and 1 inclusive and assign to a variable. 
7. Calculate the acceleration at speed level 2.5 mph and assign to a variable. Use the formula. 
8. Calculate the acceleration at speed level 3.5mph and assign to a variable. 
9. Calculate the value for d1 and assign to a variable. Use the formula. 
10. Calculate the value for d2 and assign to a variable. 
11. Calculate the total distance and assign to a variable. 
12. Calculate the value for c1 and assign to a variable. Use the formula. 
13. Calculate the value for c2 and assign to a variable. 
14. Calculate the total calories. 
15. Calculate the total number of bars. Us the formula. 
16. Display the total distance. 
17. Display the total calories. 
18. Display the total number of bars. 
"""

SPEEDSTART = 0
SPEEDONE = 2.5
SPEEDTWO = 3.5


def get_acceleration(run_time, start_speed, speed):
    """
    Where t is the elapsed time in minutes,
    v0 (0 or 2.5mph) is the start speed and
    v is speed (2.5mph or 3.5mph).
    Speed level 2.5mph has a start speed of 0mph
    Speed level 3.5mph has a start speed of 2.5mph.
    a = (v - v0) / t

    :param run_time: the time spend at the speed
    :param start_speed: the start speed
    :param speed: the new speed
    :return: returns a float
    """
    accel = speed - start_speed / run_time
    return accel


def get_distance(run_time, start_speed, acceleration):
    """
    The distance is calculated using the formula:
    d = v0t + (at^2) / 2
    for every speed level at speed level 2.5mph, v0 = 0
    at speed level 3.5mph, v0 = 2.5mph.

    :param run_time: time spent at the speed
    :param start_speed: the beginning speed
    :param acceleration: the acceleration speed
    :return: returns a float
    """
    dist = start_speed * run_time + ((acceleration * run_time ** 2) / 2)
    return dist


def get_calories(run_time, speed, incline, weight):
    """
    The number calories (k) is calculated using the formula:
    k= (t(0.175v+0.9vg)w) / 440
    Where w is the weight in pounds
    g is the incline level in percent with 0 for no incline and 1 for the maximum incline.

    :param run_time: minutes running
    :param speed: the speed being used
    :param incline: the incline percentage
    :param weight: the user's weight
    :return: float calories
    """
    calories = (run_time * (.175 * speed + .9 * speed * incline) * weight) / 440
    return calories


def get_bars(time_at_one, time_at_two):
    """
    The total number of bars is calculated using:
    b=(4.5 * t1 + 5 * t2) / 16
    t1 is the time duration at speed level 2.5mph
    t2 is the time duration at speed level 3.5mph.
    Note the final number of bars is an integer or a whole number.

    :param time_at_one: minutes spend at speed one
    :param time_at_two: minutes spend at speed two
    :return: rounded down integer of how may bars to display
    """
    bars = (4.5 * time_at_one + 5 * time_at_two) / 16
    return int(bars)


# 3. Prompt the user to enter the time duration for speed level 2.5mph and assign the value to a variable.
# 4. Prompt the user to enter the time duration for speed level 3.5mph and assign the value to a variable.
# 5. Prompt the user to enter weight in pounds and assign value to a variable.
timeAtOne = float(input('How many minutes do you want to walk at {} MPH? '.format(SPEEDONE)))
timeAtTwo = float(input('How many minutes do you want to walk at {} MPH? '.format(SPEEDTWO)))
userWeight = float(input('What is your weight in lbs? '))
# 6. Prompt the user to enter the incline level that is between 0 and 1 inclusive and assign to a variable.
while True:
    try:
        inclineLevel = float(input('What incline level do you want to use 0 minimum and 1 being the max [ex: .25]? '))
        if inclineLevel > 1 or inclineLevel < 0:
            raise ValueError
        break
    except ValueError:
        print('The value must be between 0 and 1', end='\n\n')

# 7. Calculate the acceleration at speed level 2.5 mph and assign to a variable. Use the formula.
# 8. Calculate the acceleration at speed level 3.5mph and assign to a variable.
speedOneAccel = get_acceleration(timeAtOne, SPEEDSTART, SPEEDONE)
speedTwoAccel = get_acceleration(timeAtOne, SPEEDONE, SPEEDTWO)

# 9. Calculate the value for d1 and assign to a variable. Use the formula.
# 10. Calculate the value for d2 and assign to a variable.
# 11. Calculate the total distance and assign to a variable.
distOne = get_distance(timeAtOne, SPEEDSTART, speedOneAccel)
distTwo = get_distance(timeAtTwo, SPEEDONE, speedTwoAccel)
totalDistance = distOne + distTwo

# 12. Calculate the value for c1 and assign to a variable. Use the formula.
# 13. Calculate the value for c2 and assign to a variable.
# 14. Calculate the total calories.
calsOne = get_calories(timeAtOne, SPEEDONE, inclineLevel, userWeight)
calsTwo = get_calories(timeAtTwo, SPEEDTWO, inclineLevel, userWeight)
totalCals = calsOne + calsTwo

# 15. Calculate the total number of bars. Us the formula.
totalBars = get_bars(timeAtOne, timeAtTwo)

# 16. Display the total distance.
# 17. Display the total calories.
# 18. Display the total number of bars.
print('Total Distance for this exercise is ', totalDistance)
print('Total Calories for this exercise is ', totalCals)
print('Total Bars for this exercise is ', totalBars)
