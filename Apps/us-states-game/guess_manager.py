import pandas
import turtle

class Guess_Manager:

    def __init__(self):

        state_list = pandas.read_csv('50_states.csv')
