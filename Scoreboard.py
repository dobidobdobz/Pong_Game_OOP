from turtle import Turtle


class Scoreboard(Turtle):

    # creates, colors, positions & displays scoreboard
    def __init__(self):
        super().__init__()
        self.l_paddle_score = 0
        self.r_paddle_score = 0
        self.hideturtle()
        self.color("white")
        self.teleport(0, 250)
        self.write(f"{self.l_paddle_score} | {self.r_paddle_score}", move=False, align="center", font=("Arial", 30, "normal"))

    # increases, score of left player, clears previous data, displays new score
    def increase_score_l_paddle_score(self):
        self.l_paddle_score += 1
        self.clear()
        self.write(f"{self.l_paddle_score} | {self.r_paddle_score}", move=False, align="center",
                   font=("Arial", 30, "normal"))

    # increases, score of left player, clears previous data, displays new score
    def increase_score_r_paddle_score(self):
        self.r_paddle_score += 1
        self.clear()
        self.write(f"{self.l_paddle_score} | {self.r_paddle_score}", move=False, align="center",
                   font=("Arial", 30, "normal"))
