from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from life import Life
from brick import Brick
import time
ball = Ball()
score = Score()
life = Life()
r_paddle = Paddle((0,-250))
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.left, "Left")
screen.onkey(r_paddle.right, "Right")
bricks = []
for x in range(-320, 350, 70):
    for y in range(100, 250, 30):
        bricks.append(Brick((x, y)))
while True:
    time.sleep(ball.speedy)
    screen.update()
    ball.move()
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            bricks.remove(brick)
            score.score()
            ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()
    if ball.ycor() < -290:
        ball.reset_ball()
        life.life()
        if life.check_game_over():
            break
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
screen.exitonclick()