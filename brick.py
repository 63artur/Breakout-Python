from turtle import Turtle
import random

class Brick(Turtle):
    def __init__(self, position):
        R = random.random()
        B = random.random()
        G = random.random()
        super().__init__()
        self.shape("square")
        self.color(R,G,B)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.setpos(position)

