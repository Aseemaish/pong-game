from turtle import Turtle


class Ball(Turtle): # Ball class that inherits from Turtle class and creates a ball object
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Method to move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Method to bounce the ball along the y-axis
    def y_bounce(self):
        self.y_move *= -1

    # Method to bounce the ball along the x-axis and increase the speed
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Method to reset the position of the ball
    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()

