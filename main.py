import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pandas.read_csv("50_states.csv")


# Get coordinates from the map:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
# print(answer_state)

print(df.head())


turtle.mainloop()