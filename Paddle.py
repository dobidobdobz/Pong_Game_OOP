from turtle import Turtle


class Paddle(Turtle):

    # creates size, shape, color, and positions paddles
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # upward movement method for paddle
    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    # downward movement method for paddle
    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
