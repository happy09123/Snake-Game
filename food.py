from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randrange(-290, 290, 20), random.randrange(-290, 290, 20))