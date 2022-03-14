from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Pong:

    def __init__(self):
        self.pong =  self.create_pong()

    def create_pong(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(5, 1)
        new_segment.penup()
        new_segment.goto(330, 0)
        return new_segment

    def move(self):
        self.pong.setheading(MOVE_DISTANCE)

    def up(self):
        if self.pong.heading() != DOWN:
            self.pong.setheading(UP)

    def down(self):
        if self.pong.heading() != UP:
            self.pong.setheading(DOWN)

