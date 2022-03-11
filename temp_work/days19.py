from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
height = 400
width = 500
screen.setup(width, height)
screen.title("Welcome to the turtle race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

"""
# def bet_turtle(colors_list, num, y_position):
#     tim = Turtle(shape="turtle")
#     tim.color(colors_list[num])
#     tim.penup()
#     tim.goto(x=-230, y=y_position)
#
#
# turtle1 = bet_turtle(colors, 0, 150)
# turtle2 = bet_turtle(colors, 1, 100)
# turtle3 = bet_turtle(colors, 2, 50)
# turtle4 = bet_turtle(colors, 3, 0)
# turtle5 = bet_turtle(colors, 4, -50)
# turtle5 = bet_turtle(colors, 5, -100)
"""
