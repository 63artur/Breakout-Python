from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, position):

        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setpos(position)

    def left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())
