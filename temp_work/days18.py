import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
my_colors = [
    (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
    (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141),
    (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63),
    (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)
]

turtle_module.colormode(255)
turtle_module.speed("fastest")

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(my_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    turtle_module.resetscreen()


turtle_module.listen()
turtle_module.onkey(key="w", fun=move_forwards)
turtle_module.onkey(key="s", fun=move_backwards)
turtle_module.onkey(key="a", fun=turn_left)
turtle_module.onkey(key="d", fun=turn_right)
turtle_module.onkey(key="c", fun=clear)
turtle_module.exitonclick()


"""
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# 
# print(rgb_colors)

# 
# 
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
# 
# 
# def draw_circle(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         t.color(random_color())
#         t.circle(180)
#         t.setheading(t.heading() + size_of_gap)
# 
# 
# draw_circle(4)
# tim.pensize(20)
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
# 
# 
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
# 
"""
