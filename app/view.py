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
@login_required
def devjs():
    return render_template('devjs.html')

                                                            # API
                                                                        #get tree 
# get all metatypes                                                               has been tested 13 may 2020
@app.route('/api/tree', methods = ['GET'])
def tree():

    mtypes_list = []
    
    for mtype in Metatypes.query.all():
        mtypes_list.append( mtype.serialize )
    
    result = {
        "id": 0,
        "name": 'Все метатэги',
        "subs": mtypes_list
    }

    return result


                                                                        #metatypes API
# get all metatypes                                                               has been tested 13 may 2020
@app.route('/api/metatypes', methods = ['GET'])
@login_required
def show_metatypes():
    if current_user.has_role('Администратор'):
        metatypes = mtypes_schema.dump( Metatypes.query.all() )
        return jsonify(metatypes)
    else:
        return 'no access'

# get a metatype by id                                                              has been tested 14 may 2020
@app.route('/api/metatypes/<id>', methods = ['GET'])
@login_required
def get_metatype(id):
    mtype = Metatypes.query.get(id)
    resp = mtype_schema.dump(mtype)
    return jsonify(resp)

# create a metatype                                                                 to be tested
@app.route('/api/metatypes', methods = ['POST'])
def add_metatype():
    name = request.json['name']

    new_metatype = Metatypes(name = name)

    db.session.add(new_metatype)
    db.session.commit()
    resp = type_schema.dump(new_metatype)
    return jsonify(resp)

# update a metatype                                                         to be tested
@app.route('/api/metatypes/<id>', methods = ['PUT'])
def update_metatype(id):
    metatype = Metatypes.query.get(id)
    # obtaining info from request
    name = request.json['name']
    # setting item's properties
    metatype.name = name
    # database 
    db.session.commit()
    resp = type_schema.dump(metatype)
    return jsonify(resp)

# delete a metatype                                                         to be tested
@app.route('/api/metatypes/<id>', methods = ['DELETE'])
def delete_metatype(id):
    delete_metatype = Metatypes.query.get(id)
    # database 
    db.session.delete(delete_metatype)
    db.session.commit()
    resp = type_schema.dump(delete_metatype)
    return jsonify(resp)

                                                                    #  T Y P E S   A P I
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


# create a type                                                             has been tested 9 may 2020
@app.route('/api/types', methods = ['POST'])
def add_type():
    name = request.json['name']
    number = request.json['number']

    new_type = Types(name = name, number = number)

    db.session.add(new_type)
    db.session.commit()
    resp = type_schema.dump(new_type)
    return jsonify(resp)

# update a type                                                             has been tested 9 may 2020
@app.route('/api/types/<id>', methods = ['PUT'])
def update_type(id):
    a_type = Types.query.get(id)
    # obtaining info from request
    if request.json['name']:
        a_type.name = request.json['name']
    if 'request.json["number"]' in locals() :
        a_type.name = request.json['number']
    # database 
    db.session.commit()
    resp = type_schema.dump(a_type)
    return jsonify(resp)

# delete a type                                                         has been tested 9 may 2020
@app.route('/api/types/<id>', methods = ['DELETE'])
def delete_type(id):
    delete_type = Types.query.get(id)
    # database 
    db.session.delete(delete_type)
    db.session.commit()
    resp = type_schema.dump(delete_type)
    return jsonify(resp)

                                                                        #  T O P I C S   A P I
# get all types                                                                                     has been tested 10 may 2020
@app.route('/api/topics', methods = ['GET'])
def show_topics():
    topics = topics_schema.dump( Topics.query.all() )
    return jsonify(topics)

# get a type by id                                                          has been tested 10 may 2020
@app.route('/api/topics/<id>', methods = ['GET'])
def get_topic(id):
    a_topic = Topics.query.get(id)
    resp = topic_schema.dump(a_topic)
    return jsonify(resp)


# create a type                                                             has been tested 10 may 2020
@app.route('/api/topics', methods = ['POST'])
def add_topic():
    name = request.json['name']

    new_topic = Topics(name = name)

    db.session.add(new_topic)
    db.session.commit()
    resp = topic_schema.dump(new_topic)
    return jsonify(resp)

# update a type                                                             has been tested 10 may 2020
@app.route('/api/topics/<id>', methods = ['PUT'])
def update_topic(id):
    a_topic = Topics.query.get(id)
    # obtaining info from request
    name = request.json['name']
    # setting item's properties
    a_topic.name = name
    # database 
    db.session.commit()
    resp = topic_schema.dump(a_topic)
    return jsonify(resp)

# delete a type                                                         has been tested 10 may 2020
@app.route('/api/topics/<id>', methods = ['DELETE'])
def delete_topic(id):
    delete_topic = Topics.query.get(id)
    # database 
    db.session.delete(delete_topic)
    db.session.commit()
    resp = topic_schema.dump(delete_topic)
    return jsonify(resp)