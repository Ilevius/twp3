from app import * 
from datetime import datetime
from flask_marshmallow import Marshmallow

marsh = Marshmallow(app)

class Metatypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    creationdate = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Metatypes, self).__init__(*args, **kwargs)
    
class MtypeSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'creationdate')

mtype_schema =   MtypeSchema()      
mtypes_schema = MtypeSchema(many=True)      

