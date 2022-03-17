from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.y_move = MOVE_DISTANCE

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(0, new_y)

    def reset_position(self):
        self.penup()
        self.goto(STARTING_POSITION)

