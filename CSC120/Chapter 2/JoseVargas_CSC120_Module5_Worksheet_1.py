from turtle import Turtle, Screen


class ActivityOne(object):
    turtle_1 = None
    turtle_2 = None
    screen = Screen()

    def __init__(self, t1color, t1shape, t2color, t2shape):
        print('Starting Activity')
        if t1shape is None:
            self.turtle_1 = Turtle()
            self.turtle_1.hideturtle()
        else:
            self.turtle_1 = Turtle(t1shape)
        self.turtle_1.color(t1color)
        if t2shape is None:
            self.turtle_2 = Turtle()
            self.turtle_2.hideturtle()
        else:
            self.turtle_2 = Turtle(t2shape)
        self.turtle_2.color(t2color)

    def move_turtles_equally(self, distance):
        self.turtle_1.fd(distance)
        self.turtle_2.fd(distance)

    def setup_turtles(self):
        self.turtle_1.pu()
        self.turtle_1.goto(0, 100)
        self.turtle_1.pd()
        self.move_turtles_equally(150)

    def run_turtles(self):
        for i in range(2):
            self.turtle_1.right(120)
            self.turtle_2.left(120)
            self.move_turtles_equally(150)

    def finished(self):
        print('Finished with Activity One')
        input('Press [Enter] to continue to the next activity')
        self.screen.clearscreen()


class ActivityTwo(ActivityOne):
    screen = Screen()

    def __init__(self, t1color, t1shape, t2color, t2shape):
        super().__init__(t1color, t1shape, t2color, t2shape)
        self.turtle_1.fillcolor('green')
        self.turtle_1.begin_fill()
        self.turtle_2.fillcolor('yellow')
        self.turtle_2.begin_fill()

    def run_activity(self):
        self.setup_turtles()
        self.run_turtles()
        self.turtle_1.end_fill()
        self.turtle_2.end_fill()
        self.finished()


class ActivityThree(ActivityOne):
    Screen()
    t1color = None
    t1shape = None
    t2color = None
    t2shape = None

    def __init__(self, t1color, t1shape, t2color, t2shape):
        self.t1color = t1color
        self.t2color = t2color
        self.t1shape = t1shape
        self.t2shape = t2shape
        self.reset_screen()

    def reset_screen(self):
        self.screen.clearscreen()
        self.screen.bgcolor('lightblue')
        super().__init__(t1shape=None, t2shape=None, t1color=self.t1color, t2color=self.t2color)
        self.turtle_1.color(self.t1color)
        self.turtle_2.color(self.t2color)

    def run_activity(self):
        self.create_rhombus()
        input('Press Enter to draw the next object')
        self.reset_screen()
        self.create_triangles()
        input('Press Enter to draw the next object')
        self.reset_screen()
        self.create_3d_rectangle()
        input('Press Enter to draw the next object')
        self.reset_screen()
        self.olympic_rings()
        input('Press Enter to draw the next object')
        self.reset_screen()
        self.create_compass()
        input('Press Enter to draw the next object')
        self.reset_screen()
        self.create_with_x()
        self.finished()

    def create_rhombus(self):
        self.turtle_2.pu()
        self.turtle_2.goto(177, 0)
        self.turtle_1.pd()
        self.turtle_2.pd()
        self.turtle_1.color(self.t1color)
        self.turtle_1.fillcolor('white')
        self.turtle_2.fillcolor('white')
        self.turtle_1.begin_fill()
        self.turtle_2.begin_fill()
        self.turtle_1.right(45)
        self.turtle_2.right(45)
        for i in range(4):
            self.turtle_1.right(90)
            self.turtle_2.right(90)
            self.move_turtles_equally(125)
        self.turtle_1.end_fill()
        self.turtle_2.end_fill()
        self.turtle_2.begin_poly()

    def create_triangles(self):
        angle1 = 65
        angle2 = 65 * 2
        angle3 = 310 - angle2 - angle1
        angle4 = 42
        angle5 = angle4 * 2
        angle6 = -27 - angle2 - angle1
        self.turtle_1.left(angle1)
        self.turtle_1.fd(175)
        self.turtle_1.right(angle2)
        self.turtle_1.fd(175)
        self.turtle_1.right(angle3)
        self.turtle_1.fd(148)

        self.turtle_2.begin_fill()
        self.turtle_2.fillcolor('white')
        self.turtle_2.left(angle4)
        self.turtle_2.fd(100)
        self.turtle_2.right(angle5)
        self.turtle_2.fd(100)
        self.turtle_2.right(angle6)
        self.turtle_2.fd(100)
        self.turtle_2.end_fill()

    def create_3d_rectangle(self):
        self.create_square()
        self.turtle_1.right(45)
        self.turtle_1.fd(282)
        self.turtle_1.pu()
        self.turtle_1.right(45)
        self.turtle_1.back(100)
        self.turtle_1.pd()
        self.create_square()
        self.turtle_1.left(45)
        self.turtle_1.back(141)
        self.turtle_1.pu()
        self.turtle_1.left(90)
        self.turtle_1.back(142)
        self.turtle_1.pd()
        self.turtle_1.right(90)
        self.turtle_1.fd(141)

    def create_square(self):
        for i in range(4):
            self.turtle_1.fd(100)
            self.turtle_1.right(90)

    def olympic_rings(self):
        coordinates = [
            [-125, 0],
            [-75, -50],
            [-25, 0],
            [25, -50],
            [70, 0]
        ]
        for coord in coordinates:
            self.turtle_1.pu()
            self.turtle_1.goto(coord[0], coord[1])
            self.turtle_1.pd()
            self.turtle_1.circle(40)

    def create_compass(self):
        self.turtle_1.circle(50)
        self.turtle_1.pu()
        self.turtle_1.goto(-235, 45)
        self.turtle_1.write('West')
        self.turtle_1.goto(-200, 50)
        self.turtle_1.pd()
        self.turtle_1.fd(400)
        self.turtle_1.pu()
        self.turtle_1.goto(210, 45)
        self.turtle_1.write('East')
        self.turtle_1.goto(-12, 250)
        self.turtle_1.write('North')
        self.turtle_1.goto(0, 250)
        self.turtle_1.pd()
        self.turtle_1.right(90)
        self.turtle_1.fd(400)
        self.turtle_1.pu()
        self.turtle_1.goto(-12, -165)
        self.turtle_1.write('South')

    def create_with_x(self):
        for i in range(4):
            self.turtle_1.dot()
            if i % 2 == 0:
                for i in range(4):
                    if i == 0 or i == 3:
                        self.turtle_1.fd(25)
                    else:
                        self.turtle_1.fd(45)
                    self.turtle_1.pu()
                    if i < 3:
                        self.turtle_1.fd(20)
                    self.turtle_1.pd()
            else:
                self.turtle_1.fd(200)
            self.turtle_1.right(90)
        self.turtle_1.right(45)
        self.turtle_1.fd(142)
        self.turtle_1.dot()
        self.turtle_1.fd(138)
        self.turtle_1.pu()
        self.turtle_1.right(90+45)
        self.turtle_1.fd(196)
        self.turtle_1.pd()
        self.turtle_1.left(45)
        self.turtle_1.fd(-280)

    def __finished(self):
        print('Click on the image to complete activity three')
        self.screen.exitonclick()
        print('Finished with Activity Three')


if __name__ == '__main__':
    acOne = ActivityOne(t1color='green', t1shape='arrow', t2color='red', t2shape='square')
    acOne.setup_turtles()
    acOne.run_turtles()
    acOne.finished()
    acTwo = ActivityTwo(t1color='green', t1shape='arrow', t2color='red', t2shape='square')
    acTwo.run_activity()
    acThree = ActivityThree(t1color='black', t1shape=None, t2color='black', t2shape=None)
    acThree.run_activity()
    print('Done running all of the activities')

