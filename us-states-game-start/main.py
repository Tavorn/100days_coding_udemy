import turtle
import pandas
from player_score import PlayerScore

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

# player_score = PlayerScore()

states_data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Score: 0/50", prompt="What's another state's name?").title()
x = states_data["x"].to_list
y = states_data["y"].to_list
states = states_data["state"].to_list

df = pandas.DataFrame(states_data)
if df["state"].where(df["state"] == answer_state):
    print("Yes")
else:
    print("No")

# if states_data["state"] == answer_state:
#     print("Yes")
# else:
#     print("No")

turtle.mainloop()
