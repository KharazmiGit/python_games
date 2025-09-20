import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def screen_func():
    screen = Screen()
    screen.title('snake game')
    screen.bgcolor('black')
    screen.setup(width=600, height=600, startx=0, starty=0)
    screen.tracer(0)

    return screen


screen = screen_func()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        screen.update()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()

    # Detect collision with tail
    for seg in snake.snake_body[1:-1]:

        if snake.head.distance(seg) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()

