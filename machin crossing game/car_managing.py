from random import randint
from turtle import Turtle

COLOR_LIST = ["black", "red", "blue", "green", "orange", "purple", "yellow"]


# (340, -270), (340, -250), (340, -230), (340, -210), (340, -190), (340, -160),
#      (340, -140), (340, 160),(340, 160),(340, 160),(340, 160),(340, 160),(340, 160),(340, 160),
class CarManaging(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(COLOR_LIST[randint(0, len(COLOR_LIST) - 1)])
        self.penup()
        random_y = randint(-270, 270)
        random_x = randint(340, 10000)
        self.goto(random_x, random_y)
