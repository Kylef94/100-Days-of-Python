from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url = 'https://api.npoint.io/c790b4d5cab58020d391'

r = requests.get(url)
posts = r.json()


@app.route("/")
def home_page():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact_page():
    if request.method == 'GET':
        return render_template("contact.html", msg_sent=False)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_num = request.form['phone num']
        message = request.form['message']
        return render_template("contact.html", msg_sent = True)

@app.route("/post/<post_id>")
def get_post(post_id):
    for post in posts:
        if post['id'] == int(post_id):
            blog_post = post

    return render_template('post.html', blog_post=blog_post)




if __name__ == "__main__":
    app.run(debug=True)