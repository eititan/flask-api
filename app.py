from flask import Flask, render_template, abort, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#db table layout
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Pokemon %r>' % self.name

class PokemonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

# pokemon_schema = PokemonSchema(strict=True)
# pokemons_schema = PokemonSchema(many=True, strict=True)

@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route('/api/pokemon/<int:index>')
def api_pokemon_detail(index):
    try:
        #get info from db with id, then pass data to jinja template
        #return jsonified results
        return str(index)
    except IndexError:
        abort(404)

@app.route('/api/pokemon')
def api_pokemon():
    all_pokemon = Pokemon.query.all()
    # result = pokemons_schema.dump(all_pokemon)
    return str(len(all_pokemon))

@app.route('/api/type/<int:index>')
def api_type_detail(index):
    try:
        #get type from db with id, then pass data to jinja template
        #return jsonified results
        return str(index)
    except IndexError:
        abort(404)