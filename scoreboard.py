from turtle import Turtle


class Scoreboard(Turtle):   # Scoreboard class that inherits from Turtle class and creates a scoreboard object
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    # Method to update the score on the screen
    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Method to increase the score of the left paddle by 1
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    # Method to increase the score of the right paddle by 1
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
