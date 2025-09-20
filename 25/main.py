import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. num Game")
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(750, 500)
turtle.shape(image)


def write_on_map(state_name, position):
    obj = turtle.Turtle()
    obj.hideturtle()
    obj.penup()
    obj.goto(position)

    obj.write(f"{state_name}", align="center", font=("Arial", 7, "bold"))

    return obj


with open('50_states.csv', mode='r') as file:
    fifty_states = pd.read_csv(file)

    state_names = fifty_states['state']
missing_list = []
correct_guesses = []
missing_states = {
    'missing states': missing_list
}
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        for state in fifty_states['state']:
            if not state in correct_guesses:
                missing_list.append(state)

        df = pd.DataFrame(missing_states)
        df.to_csv('state_to_learn.csv')
        break

    if answer_state in state_names.values:

        try:
            go_to = fifty_states[fifty_states['state'] == answer_state]
            write_on_map(answer_state, position=(go_to['x'].values[0], go_to['y'].values[0]))
            if not answer_state in correct_guesses:
                correct_guesses.append(answer_state)
            print(len(correct_guesses))

        except Exception as e:
            print('an error has occurred', e)

    else:
        print('wrong one', answer_state)
        print(state_names)

screen.mainloop()
