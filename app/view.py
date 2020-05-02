from app import app, db
from flask import render_template
from flask import jsonify
from flask import request

from models import *


test = [
    {
        'name': 'test 1',
        'type': 'unit'
    },
    {
        'name': 'test 2',
        'type': 'unit'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def reg():
    return render_template('registration.html')

@app.route('/javascript-development')
def devjs():
    return render_template('devjs.html')


@app.route('/api/metatypes', methods = ['GET'])
def show_metatypes():
    metatypes = mtypes_schema.dump( Metatypes.query.all() )
    return jsonify(metatypes)

@app.route('/api/metatypes', methods = ['POST'])
def add_metatype():
    name = request.json['name']

    new_metatype = Metatypes(name = name)

    db.session.add(new_metatype)
    db.session.commit()
