from flask import Flask


trial = Flask(__name__)

@trial.route('/')
def hello_world():
    return render_template('home.html')

@trial.route('/')
def hello_world():
    return 'This is my about page'