from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

# creates objects classes imported
screen = Screen()
paddle = Turtle()

# UI setup, screen size, color, title, tracer for animation switched off
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# starting coordinates of paddles
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))

# creates objects from imported classes
ball = Ball()
score = Scoreboard()

# screen listens for keystrokes & binds commands/functions to keystrokes pressed
screen.listen()
# moves paddles
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# variable set to keep while loop running
game_is_on = True

# loops the ball's movement, delays screen by ball move speed, refreshes screen
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # DETECT COLLISION WITH TOP WALL AND BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH right paddle (detects distance between ball and paddle to determine if its made contact)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 and ball.x_move > 0 or ball.distance(l_paddle) < 50 and ball.xcor() < -340 and ball.x_move < 0:
        ball.bounce_x()

    # DETECT when Right paddle misses vice versa. Increases score of left player + resets ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_score_l_paddle_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_score_r_paddle_score()

screen.exitonclick()
