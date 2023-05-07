from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['username']
    pword = request.form['password']
    return '<h1> name: {0}  Password: {1}'.format(name,pword)


if __name__ == "__main__":
    app.run(debug=True)