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

guessed_states = []
while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)} out of 50 guessed", prompt="What's another state's name?").title()
    if guess == "Exit":
        total_states = df["state"].to_list()
        for state in guessed_states:
            if state in total_states:
                total_states.remove(state)
        total_df = pandas.DataFrame(total_states)
        total_df.to_csv("remaining_states.csv")
        break
    if guess in df['state'].unique():
        guessed_states.append(guess)
        # idx = df[df["state"] == guess].index.values.astype(int)[0]
        # row = df[df['state'] == guess]
        # x = row.loc[idx]['x']
        # y = row.loc[idx]['y']
        # writer.goto((x, y))
        # writer.write(guess)
        state_data = df[df.state == guess]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(state_data.state.item())


# turtle.mainloop()
