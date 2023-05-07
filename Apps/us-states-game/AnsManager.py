import turtle
import pandas


class AnsManager():

    def __init__(self):
        self.state_list = pandas.read_csv('50_states.csv')
        self.correct_guesses = []
        self.mapper = turtle.Turtle()
        self.mapper.pu()
        self.mapper.hideturtle()

    def check_ans(ans):
        ans = ans.Title()
        if ans in state_list.state.values:
            df_row = state_list[state_list.state == answer_state]
            print(df_row)
            x = int(df_row.x)
            y = int(df_row.y)
            print(x)
            print(y)
            mapper.goto(x, y)
            mapper.write((answer_state))
            self.correct_guesses.append(ans)

        else:
            print('Game Over')

    def correct_ans(ans):
        correct_guesses.append(ans)
        state_row = state_list.state[ans]
        print(state_row)


