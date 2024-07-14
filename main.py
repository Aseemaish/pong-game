from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from screen import Setup

screen = Screen()
screen.tracer(0)  # Turn off the screen updates
screen.setup(800, 600)  # Set the screen size
screen.bgcolor("black")

separator = Setup()  # Create a separator object

ball = Ball()  # Create a ball object

r_paddle = Paddle((340, 0))  # Create a right paddle object
l_paddle = Paddle((-340, 0))  # Create a left paddle object
score = Scoreboard()  # Create a scoreboard object
screen.listen()  # Listen for key presses
game_is_on = True


#Function to turn off the game
def off():
    global game_is_on
    game_is_on = False

#Key bindings for the paddles
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(off, "q")
#Main game loop
while game_is_on:
    time.sleep(ball.move_speed) # Pause the program for some seconds
    screen.update() # Update the screen
    ball.move() # Move the ball
    if ball.ycor() > 280 or ball.ycor() < -280: # Check if the ball has hit the top or bottom wall
        ball.y_bounce()
    # Check if the ball has hit the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 310 or ball.distance(l_paddle) < 50 and ball.xcor() < -310:
        ball.x_bounce()
    # Check if the ball has hit the left or right wall
    if ball.xcor() > 330:
        ball.reset_pos()
        score.l_point()
    if ball.xcor() < -330:
        ball.reset_pos()
        score.r_point()
screen.clearscreen()    # Clear the screen
#Printing the final message
final_message = Turtle()
final_message.color("black")
final_message.penup()
final_message.hideturtle()
final_message.goto(0, 50)
final_message.write("Game Over", align="center", font=("Courier", 24, "normal"))
final_message.goto(0, 0)
final_message.write(f"Final Score: {score.l_score} : {score.r_score}", align="center", font=("Courier", 24, "normal"))
final_message.goto(0, -50)
if score.l_score > score.r_score:
    winner = "Left"
elif score.l_score < score.r_score:
    winner = "Right"
else:
    winner = "Scores are tied!!"
final_message.write(f"The winner is: {winner}", align="center", font=("Courier", 24, "normal"))
time.sleep(5)
screen.bye()
