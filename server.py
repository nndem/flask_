from flask import Flask, render_template

from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nick'


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
def blog_post(blog_id):
    return 'This is blog post number' + blog_id


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('/signup.html', form=form)


if __name__ == "__main__":
    app.run()
