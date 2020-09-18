from turtle import Turtle, Screen

BORDER = 5
FONT = ("Arial", 12, "normal")
FLOAT_FORMAT = "0.2f"
PENSIZE = 3


def letterFrequency(string):
    counter = dict()

    length = ord('z') - ord('a') + 1

    for ordinal in range(length):
        counter[chr(ordinal + ord('a'))] = 0

    count = 0

    for character in string:
        if character.isalpha():
            counter[character] += 1
            count += 1

    return [counter[key] / count for key in sorted(counter)]


def letterFreqPlot(turtle, canvas, string):

    turtle.pensize(PENSIZE)

    frequencyList = letterFrequency(string)

    maxheight = max(frequencyList)
    numbers = len(frequencyList)

    canvas.setworldcoordinates(-BORDER, -.05, numbers + 1, maxheight + 0.1)

    turtle.hideturtle()

    for frequency in sorted(set(frequencyList)):
        turtle.penup()
        turtle.home()
        turtle.lt(90)
        turtle.pendown()
        turtle.forward(frequency)
        turtle.left(90)
        turtle.forward(3)
        turtle.write(format(frequency, FLOAT_FORMAT), font=FONT)

    turtle.penup()
    turtle.home()
    turtle.sety(-0.0125)

    for i, frequency in enumerate(frequencyList):
        turtle.forward(0.5)
        turtle.write(chr(ord('a') + i), font=FONT)
        turtle.forward(0.5)

    turtle.home()
    turtle.goto(len(frequencyList) / 2, -0.025)
    turtle.write(string, align="center", font=FONT)

    turtle.home()
    turtle.fillcolor("blue")
    turtle.pendown()

    for frequency in frequencyList:
        if frequency > 0.0:
            turtle.begin_fill()
            for distance in [1, frequency] * 2:
                turtle.forward(distance)
                turtle.left(90)
            turtle.end_fill()
        turtle.forward(1)


yertle = Turtle()
yertle.speed('fastest')

screen = Screen()
screen.delay(0)
screen.tracer(0)

letterFreqPlot(yertle, screen, "an opportunity to teach is an opportunity to learn")

screen.exitonclick()
