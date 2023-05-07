from flask import Flask, render_template
from datetime import date
import requests
app = Flask(__name__)

@app.route('/')
def home():
    year = date.today().year
    return render_template("index.html", year=year)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/e216522712301d7ca458'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

@app.route('/guess/<string:name>')
def guess(name):
    name = name.capitalize()
    age = agify(name)
    gender = genderize(name)
    return render_template("guess.html", name=name, age=age, gender=gender)

def agify(name):
    url = 'https://api.agify.io'
    params = {'name': name}

    r = requests.get(url, params)
    data = r.json()
    age = data["age"]
    return age

def genderize(name):
    url = 'https://api.genderize.io'
    params = {'name': name}

    r = requests.get(url, params)
    data = r.json()
    gender = data["gender"]
    return gender

if __name__ == "__main__":
    app.run(debug=True)
