from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World MTF'


@app.route('/about')
def about():
    return "The About Page"


@app.route('/blog')
def blog():
    posts = [{'title': 'Technology in 2020', 'author': 'don Nick'},
             {'title': 'Expansion of MTH in Taganrog', 'author': 'don Nick'}
             ]
    return render_template('blog.html', author='Nick', sunny=False, posts=posts)


@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number' + blog_id


if __name__ == "__main__":
    app.run()
