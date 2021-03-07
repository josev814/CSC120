"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 11
Assignment: Homework
Date: 2020-11-03
"""

"""
Write a program that uses turtle graphics to display a snowman, similar to the one shown in Figure 5-30. 
In addition to a main function, the program should also have the following functions:
• drawBase. This function should draw the base of the snowman, which is the large snowball at the bottom.
• drawMidSection. This function should draw the middle snowball.
• drawArms. This function should draw the snowman’s arms.
• drawHead. This function should draw the snowman’s head, with eyes, mouth, and other facial features you desire.
• drawHat. This function should draw the snowman’s hat.
"""
from turtle import Turtle


def draw_circle(x_cord, y_cord, radius, fill_color=None):
    trtle.pu()
    trtle.goto(x_cord, y_cord)
    trtle.pd()
    if fill_color is not None:
        old_color = trtle.fillcolor()
        start_fill(fill_color)
    trtle.circle(radius)
    if fill_color is not None:
        trtle.end_fill()
        trtle.fillcolor(old_color)


def start_fill(color):
    trtle.fillcolor(color)
    trtle.begin_fill()


def move_pen(x_cord, y_cord, draw=False):
    if not draw:
        trtle.pu()
    trtle.goto(x_cord, y_cord)
    if not draw:
        trtle.pd()


def draw_square(x_cord, y_cord, length, fill_color=None):
    move_pen(x_cord, y_cord)
    if fill_color is not None:
        old_color = trtle.fillcolor()
        start_fill(fill_color)
    for i in range(3):
        trtle.fd(length)
        trtle.right(90)
    if fill_color is not None:
        trtle.end_fill()
        trtle.fillcolor(old_color)


def draw_rectangle(x_cord, y_cord, x_len, y_len, fill_color=None):
    move_pen(x_cord, y_cord)
    if fill_color is not None:
        old_color = trtle.fillcolor()
        start_fill(fill_color)
    for i in range(3):
        if i % 2 == 0:
            trtle.fd(y_len)
        else:
            trtle.fd(x_len)
        trtle.right(90)
    if fill_color is not None:
        trtle.end_fill()
        trtle.fillcolor(old_color)


def draw_line(x_cord, y_cord, len):
    move_pen(x_cord, y_cord, False)
    trtle.fd(len)


def draw_snowman():
    draw_base()
    draw_mid_section()
    draw_head()
    draw_face()
    draw_hat()
    draw_arms()


def draw_base():
    draw_circle(0, -300, 125)


def draw_mid_section():
    draw_circle(0, -50, 75)


def draw_arms():
    trtle.right(180)
    draw_left_arm()
    draw_right_arm()


def draw_right_arm():
    draw_line(-70, 50, 75)
    trtle.right(45)
    trtle.fd(75)
    trtle.left(15)
    draw_line(-198, 102, 20)
    trtle.right(60)
    draw_line(-198, 102, 20)


def draw_left_arm():
    draw_line(70, 50, 75)
    trtle.left(90)
    trtle.fd(75)
    trtle.left(45)
    draw_line(145, 124, 20)
    trtle.right(90)
    draw_line(145, 124, 20)
    trtle.left(90+45)


def draw_head():
    draw_circle(0, 100, 50)


def draw_face():
    draw_circle(-20, 155, 8, 'blue')
    draw_circle(20, 155, 8, 'blue')
    draw_line(-25, 125, 50)


def draw_hat():
    draw_square(-40, 270, 80, 'black')
    draw_rectangle(-70, 175, 140, 30, 'black')


if __name__ == '__main__':
    trtle = Turtle()
    trtle.hideturtle()
    trtle.speed(0)
    trtle.pensize(2)
    draw_snowman()
