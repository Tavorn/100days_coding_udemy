import time
from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard
from pong import Pong

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

ball = Ball()
scoreboard = ScoreBoard()
pong = Pong()

screen.listen()
screen.onkey(pong.up, "Up")
screen.onkey(pong.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    ball.refresh()
    time.sleep(0.1)
    pong.move()


screen.exitonclick()

"""
# width = 20
# height = 100
# x_pos = 350
# y_pos = 0

move up
move down
"""
