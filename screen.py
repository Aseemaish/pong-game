from turtle import Turtle


class Setup(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, -450)
        self.pendown()
        self.setheading(90)
        self.pensize(5)
        self.draw()

    def draw(self):
        for i in range(30):
            self.forward(15)
            self.penup()
            self.forward(20)
            self.pendown()
