from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)
turtle.pu()
turtle.goto(-100, 100)
turtle.pd()
screen.delay(0)

for i in range(4):
    turtle.dot()
    if i % 2 == 0:
        for i in range(4):
            if i == 0 or i == 3:
                turtle.fd(25)
            else:
                turtle.fd(45)
            turtle.pu()
            if i < 3:
                turtle.fd(20)
            turtle.pd()
    else:
        turtle.fd(200)
    turtle.right(90)
turtle.right(45)
turtle.fd(142)
turtle.dot()
turtle.fd(138)
turtle.pu()
turtle.right(90+45)
turtle.fd(196)
turtle.pd()
turtle.left(45)
turtle.fd(-280)

print('Click on the image to exit')
screen.exitonclick()
