from turtle import Turtle
STARTING_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Pong:

    def __init__(self):
        self.create_pong()

    def create_pong(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(20)
        new_segment.penup()
        new_segment.goto(350, 0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(UP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

