from app import * 
from datetime import datetime
from flask_marshmallow import Marshmallow

marsh = Marshmallow(app)

#                                                               class of metatypes
class Metatypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    #creationdate = db.Column(db.DateTime, default=datetime.now())
    
class MtypeSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'creationdate')

mtype_schema =   MtypeSchema()      
mtypes_schema = MtypeSchema(many=True)      

#                                                               class of types
class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    #creationdate = db.Column(db.DateTime, default=datetime.now())
    number = db.Column(db.Integer)

class TypeSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'number', 'creationdate')

type_schema =   TypeSchema()      
types_schema = TypeSchema(many=True) 
