import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game')
bg_image = 'blank_states_img.gif'
screen.addshape(bg_image)
turtle.shape(bg_image)
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt='Guess another state!').title()

    if answer_state == 'Exit':
        remaining_states = set(all_states).intersection(guessed_states)
        missed_states_df = pandas.DataFrame(remaining_states)
        missed_states_df.to_csv('States to remember.csv', index=False)
        break

# missing_states = [state for state in all_states if state not in guessed_states]

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


turtle.mainloop()