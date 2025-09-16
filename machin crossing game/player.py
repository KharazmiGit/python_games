from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)


    def go_up(self):
        self.setheading(90)
        self.forward(5)

    def go_down(self):
        self.setheading(270)
        self.forward(5)
