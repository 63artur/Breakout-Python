from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-290,250)
        self.write(f'Score: {self.score}', align="center", font=("Arial", 24, "bold" ))
    def score(self):
        self.score += 1
        self.update_score()
