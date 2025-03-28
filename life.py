from turtle import Turtle
class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(290,250)
        self.lifes = 3
        self.update_lifes()
        self.check_game_over()
    def update_lifes(self):
        self.clear()
        self.goto(290,250)
        self.write(f'Life: {self.lifes}', align="center", font=("Arial", 24, "bold" ))
    def life(self):
        self.lifes  -= 1
        self.update_lifes()

    def check_game_over(self):
        if self.lifes == 0:
            self.goto(0,0)
            self.write('Game Over', align="center", font=("Arial", 24, "bold"))
            return True



