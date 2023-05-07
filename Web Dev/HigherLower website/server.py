import random
from flask import Flask
app = Flask(__name__)

CORRECT_ANS = random.randint(0,9)

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/')
def choose_ans(CORRECT_ANS):
    CORRECT_ANS = random.randint(0,9)

@app.route('/<int:guess>')
def check_ans(guess):
    if guess > CORRECT_ANS:
        return '<h1>Too high! Try again!</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g">'

    elif guess < CORRECT_ANS:
        return '<h1>Too low! Try again!</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    else:
        return '<h1>Perfect! You win!</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)