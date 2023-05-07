from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/e216522712301d7ca458'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<post_id>')
def get_post(post_id):
    post_id = int(post_id)
    blog_url = 'https://api.npoint.io/e216522712301d7ca458'
    response = requests.get(blog_url)
    all_posts = response.json()
    blog_post = all_posts[post_id -  1]
    return render_template("post.html", blog_post=blog_post)



if __name__ == "__main__":
    app.run(debug=True)
