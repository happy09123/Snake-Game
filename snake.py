from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.stop = False
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        position = [0, 0]
        for _ in range(0, 3):
            self.add_segment(position)
            position[0] += -20


    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.goto(position)

        self.segments.append(turtle)

        if (len(self.segments)-1) % 2 == 0:
            turtle.color("light gray")
        else:
            turtle.color("white")

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        if not self.stop:
            for s in range(len(self.segments) - 1, 0, -1):
                self.segments[s].goto(
                    self.segments[s - 1].pos()
                )

            self.segments[0].forward(20)

    def up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)

    def left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def restart(self):
        for segment in self.segments:
            segment.reset()

        self.__init__()
