from flask import Flask, render_template, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#db table layout
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Pokemon %r>' % self.name

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), unique=True, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def __init__(self, typename):
        self.type = typename

    def __repr__(self):
        return '<Type %r>' % self.type


@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route('/api/pokemon/<int:index>')
def api_pokemon_detail(index):
    try:
        pokemon = Pokemon.query.filter(Pokemon.id == index)
        return jsonify([i.serialize for i in pokemon])
    except IndexError:
        abort(404)

@app.route('/api/pokemon')
def api_pokemon_all():
    all_pokemon = Pokemon.query.all()
    return jsonify([i.serialize for i in all_pokemon])

@app.route('/api/type/<int:index>')
def api_type_detail(index):
    try:
        type = Type.query.filter(Type.id == index)
        return jsonify([i.serialize for i in type])
    except IndexError:
        abort(404)

@app.route('/api/type')
def api_type_all():
    try:
        all_types = Type.query.all()
        return jsonify([i.serialize for i in all_types])
    except IndexError:
        abort(404)