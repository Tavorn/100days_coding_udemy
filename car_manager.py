from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = random.randint(0, 20)
        self.random_car()
        self.y_move = STARTING_MOVE_DISTANCE
        self.y_speed = MOVE_INCREMENT

    def create_car(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.speed("fast")
        self.forward(LEFT)

    def move(self):
        new_y = random.randint(250, -250)
        self.goto(0, new_y)

    def random_car(self):
        self.create_car()

    def increase_speed(self):
        self.goto(0, self.y_speed)
