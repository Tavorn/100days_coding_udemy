from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.random_position = random.randint(250, -250)
        self.y_move = STARTING_MOVE_DISTANCE
        self.y_speed = MOVE_INCREMENT

    def create_car(self):
        pass

    def add_car(self, position):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(0, self.random_position)
        new_car.speed("fast")
        new_car.forward(LEFT)
        self.cars.append(new_car)

    def increase_speed(self):
        self.goto(0, self.y_speed)
