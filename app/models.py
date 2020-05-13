from app import * 
from datetime import datetime
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
#from flask_security import UserMixin, RoleMixin

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
    subs = db.relationship('Types', secondary=metatypes_types, backref = db.backref('metas', lazy='dynamic') )
    
#                                                               class of  T Y P E S
class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    number = db.Column(db.Integer)
    subs = db.relationship('Topics', secondary=topics_types, backref = db.backref('metas', lazy='dynamic') )

#                                                               The class of  T O P I C S
class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    shortname = db.Column(db.String(140), unique=True)


#                                                           Marshmellow's schemas
#                                                                                 schema of  M E T A T Y P E S
class MtypeSchema(SQLAlchemySchema):
    class Meta:
        model = Metatypes
        load_instance = True

    id = auto_field()
    name = auto_field()
    subs = auto_field()

mtype_schema =   MtypeSchema()      
mtypes_schema = MtypeSchema(many=True) 

#                                                                                   schema of  T Y P E S 
class TypeSchema(SQLAlchemySchema):
    class Meta:
        model = Types
        load_instance = True

    id = auto_field()
    name = auto_field()
    number = auto_field()
    subs = auto_field()
    metas = auto_field()

type_schema =   TypeSchema()      
types_schema = TypeSchema(many=True) 

#                                                                                   The schema of  T O P I C S
class TopicSchema(SQLAlchemySchema):
    class Meta:
        model = Topics
        load_instance = True

    id = auto_field()
    name = auto_field()
    #subs = auto_field()
    metas = auto_field()

topic_schema =   TopicSchema()      
topics_schema = TopicSchema(many=True) 
