from app import app, db
from flask import render_template
from flask import jsonify
from flask import request

from models import *



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def reg():
    return render_template('registration.html')

@app.route('/javascript-development')
def devjs():
    return render_template('devjs.html')

                                                            # API
                                                                        #metatypes API
# get all metatypes
@app.route('/api/metatypes', methods = ['GET'])
def show_metatypes():
    metatypes = mtypes_schema.dump( Metatypes.query.all() )
    return jsonify(metatypes)

# get a metatype by id
@app.route('/api/metatypes/<id>', methods = ['GET'])
def get_metatype(id):
    mtype = Metatypes.query.get(id)
    return mtype_schema.jsonify(mtype)


# create a metatype
@app.route('/api/metatypes', methods = ['POST'])
def add_metatype():
    name = request.json['name']

    new_metatype = Metatypes(name = name)

    db.session.add(new_metatype)
    db.session.commit()
    return mtype_schema.jsonify(new_metatype)

# update a metatype
@app.route('/api/metatypes/<id>', methods = ['PUT'])
def update_metatype(id):
    metatype = Metatypes.query.get(id)
    # obtaining info from request
    name = request.json['name']
    # setting item's properties
    metatype.name = name
    # database 
    db.session.commit()
    return mtype_schema.jsonify(metatype)

# delete a metatype
@app.route('/api/metatypes/<id>', methods = ['DELETE'])
def delete_metatype(id):
    delete_metatype = Metatypes.query.get(id)
    # database 
    db.session.delete(delete_metatype)
    db.session.commit()
    return mtype_schema.jsonify(delete_metatype)

                                                                    #types API
# get all types
@app.route('/api/types', methods = ['GET'])
def show_types():
    types = types_schema.dump( Types.query.all() )
    return jsonify(types)

# get a type by id                                                          has been tested 9 may 2020
@app.route('/api/types/<id>', methods = ['GET'])
def get_type(id):
    a_type = Types.query.get(id)
    resp = type_schema.dump(a_type)
    return jsonify(resp)


# create a type                                                             to be tested
@app.route('/api/types', methods = ['POST'])
def add_type():
    name = request.json['name']
    number = request.json['number']

    new_type = Types(name = name, number = number)

    db.session.add(new_type)
    db.session.commit()
    resp = type_schema.dump(new_type)
    return jsonify(resp)

# update a type                                                             to be tested
@app.route('/api/types/<id>', methods = ['PUT'])
def update_type(id):
    a_type = Types.query.get(id)
    # obtaining info from request
    name = request.json['name']
    number = request.json['number']
    # setting item's properties
    a_type.name = name
    a_type.number = number
    # database 
    db.session.commit()
    return type_schema.jsonify(a_type)

# delete a type                                                         to be tested
@app.route('/api/types/<id>', methods = ['DELETE'])
def delete_type(id):
    delete_type = Types.query.get(id)
    # database 
    db.session.delete(delete_type)
    db.session.commit()
    return type_schema.jsonify(delete_type)