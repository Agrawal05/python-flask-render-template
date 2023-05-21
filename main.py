from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Deeksha Agrawal',
        'title': 'Beginner',
        'content': 'First flask Project',
        'date_posted': 'May 21 2023'
    },
    {
        'author': 'Neha Agrawal',
        'title': 'Beginner 2',
        'content': 'Second flask Project',
        'date_posted': '21 May 2023'
    }
]


@app.route("/")
@app.route("/home")
def hello_home():
    return render_template('home.html', posts=posts)

@app.route("/hello-world")
def hello_world():
    return render_template('hello.html', title='Hello')

if __name__ == '__main__':
    app.run(debug=True)
