# main.py
from turtle import Screen
from player import Player
from car_managing import CarManaging
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars_list = []

# Create 30 car objects
for _ in range(100):
    new_car = CarManaging()
    cars_list.append(new_car)

screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    for car in cars_list:
        car.forward(-5)
        # detect collision with end
        if player.ycor() > 280:
            scoreboard.win()
            is_game_on = False

        # detect collision with car
        if player.distance(car) < 41:
            scoreboard.game_over()
            is_game_on = False
    screen.update()

screen.exitonclick()
