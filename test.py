from flask import Flask, render_template

app = Flask(__name__)

timesViewed = 0



@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route('/about')
def welcome():
    global timesViewed
    return "This page has been viewed " + str(timesViewed) + " times."

def viewed(views):
    global timesViewed
    timesViewed = views + 1