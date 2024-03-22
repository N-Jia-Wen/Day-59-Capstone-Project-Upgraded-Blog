from flask import Flask, render_template
import requests


response = requests.get(url="https://api.npoint.io/6d9316b546b857979fcb")
blog_posts = response.json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<index>")
def get_blog(index):
    return render_template("post.html", posts=blog_posts, index=int(index))


if __name__ == "__main__":
    app.run(debug=True)
