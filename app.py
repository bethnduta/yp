from flask import Flask, render_template
from data import Blogs

app = Flask(__name__)

Blogs = Blogs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html',blogs=Blogs)


if __name__ == '__main__':
    app.run(debug=True)