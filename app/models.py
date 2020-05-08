from app import * 
from datetime import datetime
from flask_marshmallow import Marshmallow

#                                                               assosiation table for  M E T A T Y P E S  &  T Y P E S
metatypes_types = db.Table('metatypes_types',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('metatypes_id', db.Integer, db.ForeignKey('metatypes.id')),
    db.Column('types_id', db.Integer, db.ForeignKey('types.id'))
)

#                                                               assosiation table for TYPES & TOPICS
topics_types = db.Table('topics_types',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('types_id', db.Integer, db.ForeignKey('types.id')),
    db.Column('topics_id', db.Integer, db.ForeignKey('topics.id'))
)

#                                                               class of  M E T A T Y P E S
class Metatypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    subs = db.relationship('Types', secondary=metatypes_types, backref = db.backref('metatypes', lazy='dynamic') )
    
#                                                               class of  T Y P E S
class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    number = db.Column(db.Integer)
    subs = db.relationship('Topics', secondary=topics_types, backref = db.backref('types', lazy='dynamic') )

#                                                               The class of  T O P I C S
class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    shortname = db.Column(db.String(140), unique=True)
#                                                           Marshmellow's schemas

marsh = Marshmallow(app)

class MtypeSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'subs_')

mtype_schema =   MtypeSchema()      
mtypes_schema = MtypeSchema(many=True)      

class TypeSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'number', 'subs_')

type_schema =   TypeSchema()      
types_schema = TypeSchema(many=True) 
