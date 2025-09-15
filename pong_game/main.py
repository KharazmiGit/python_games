import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard


def screen_func():
    screen = Screen()
    screen.bgcolor('black')
    screen.tracer(0)
    screen.setup(width=800, height=600)
    screen.title('pong game')

    return screen


screen_obj = screen_func()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen_obj.listen()
screen_obj.onkey(r_paddle.go_up, 'Up')
screen_obj.onkey(r_paddle.go_down, 'Down')
screen_obj.onkey(l_paddle.go_up, 'w')
screen_obj.onkey(l_paddle.go_down, 's')

ball = Ball()
scoreboard = ScoreBoard()
scoreboard.update_scoreboard()  # ✅ Draw initial scores

cold_water = 'to be hide cannot be on challenge'
speed_rate = 0

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen_obj.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball goes out of screen
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()

screen_obj.exitonclick()
