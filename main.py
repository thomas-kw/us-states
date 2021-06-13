# Get coordinates from the map:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
# print(answer_state)

import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color('black')
df = pandas.read_csv("50_states.csv")

correct_guess = []
game_is_on = True
while game_is_on:
    guess = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    if guess in df['state'].unique():
        correct_guess.append(guess)
        idx = df[df["state"] == guess].index.values.astype(int)[0]
        row = df[df['state'] == guess]
        x = row.loc[idx]['x']
        y = row.loc[idx]['y']
        writer.goto((x, y))
        writer.write(guess)


turtle.mainloop()
