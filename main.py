from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
height = 400
width = 500
screen.setup(width, height)
print(screen.window_width())
print(screen.window_height())
screen.title("Welcome to the turtle race")



screen.exitonclick()
