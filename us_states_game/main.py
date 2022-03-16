import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
user_guesses = []
all_states = data.state.to_list()
missed_states = []
input_title_string = f"{len(user_guesses)}/{len(data)} States Correct"

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

game_is_on = True

while len(user_guesses) < len(data) and game_is_on:
    user_answer = screen.textinput(title=input_title_string, prompt="Enter a state name.").title()
    if user_answer not in user_guesses and data.state.str.match(user_answer).any():
        user_guesses.append(user_answer)
        state_info = data[data.state == user_answer]
        turtle.setposition(int(state_info.x), int(state_info.y))
        turtle.write(arg=state_info.state.item(), align="left")
    elif user_answer == "Exit":
        game_is_on = False
        for state in all_states:
            if state not in user_guesses:
                missed_states.append(state)
    input_title_string = f"{len(user_guesses)}/{len(data)} States Correct"
turtle.setposition(0, 0)
if len(user_guesses) == 50:
    turtle.write(arg="Congratulations, you did it!", align="center", font=("Arial", 30, "normal"))
else:
    turtle.write(arg="You didn't guess all the states!", align="center", font=("Arial", 30, "normal"))

missed_states_df = pandas.DataFrame(missed_states)
missed_states_df.to_csv("missed_states.csv")

screen.exitonclick()
