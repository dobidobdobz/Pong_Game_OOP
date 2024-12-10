from turtle import Turtle


class Ball(Turtle):

    # creates & sets size, shape, color, movement & movement speed for ball
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # adds movement increment to ball's current x+y coordinates and sets to new position
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # pivots ball's y-coordinate to opposite direction
    def bounce_y(self):
        self.y_move *= -1

    # pivots ball's x-coordinate to opposite direction
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # resets ball speed, and position to center of screen
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
