from flask import Flask, render_template, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
#
# class Pokemon:
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Coulumn(db.string, unique=True, nullable=False)
#
#     def __repr__(self):
#         return "<Pokemon %r>" % self.name

timesViewed = 0

@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route('/about')
def welcome():
    global timesViewed
    timesViewed = viewed(timesViewed)
    return "This page has been viewed " + str(timesViewed) + " times."

def viewed(views):
    return views + 1


@app.route('/api/pokemon/<int:index>')
def api_pokemon_detail(index):
    try:
        #get info from db with id, then pass data to jinja template
        #return jsonified results
        return str(index)
    except IndexError:
        abort(404)

@app.route('/api/type/<int:index>')
def api_type_detail(index):
    try:
        #get type from db with id, then pass data to jinja template
        #return jsonified results
        return str(index)
    except IndexError:
        abort(404)