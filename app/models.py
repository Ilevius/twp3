from app import * 
from datetime import datetime
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore, login_required, current_user


# for Flask-Security
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    secondname = db.Column(db.String(140))
    email = db.Column(db.String(140), unique=True)
    password = db.Column(db.String(140))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(140))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

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
    subs = db.relationship('Types', secondary=metatypes_types, backref = db.backref('metas', lazy='joined') )

    @property 
    def serialize(self):
        return {
            "kind": "metatypes",
            "id": self.id,
            "name": self.name,
            "number": self.id,
            "subs": self.serialize_subs
        }
    @property
    def serialize_subs(self):
        return[item.serialize for item in self.subs]    
    
#                                                               class of  T Y P E S
class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    number = db.Column(db.Integer)
    subs = db.relationship('Topics', secondary=topics_types, backref = db.backref('metas', lazy='dynamic') )

    @property 
    def serialize(self):
        return {
            "kind": "types",
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "order": 'by number',
            "subs": self.serialize_subs
        }
    @property
    def serialize_subs(self):
        return[item.serialize for item in self.subs]    

#                                                               The class of  T O P I C S
class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    shortname = db.Column(db.String(140), unique=True)

    @property
    def serialize(self):
        somelist = []
        return {
            "kind": "topics",
            "id": self.id,
            "name": self.name,
            "number": self.id,
            "subs": somelist
        }



#                                                           Marshmellow's schemas
#                                                                                 schema of  M E T A T Y P E S
ma = Marshmallow(app)

class MtypeSchema(SQLAlchemySchema):
    class Meta:
        model = Metatypes
        load_instance = True

    id = auto_field()
    name = auto_field()
    subs = auto_field()

    info = ma.Hyperlinks(
        {"kind": 'metatypes', "content": 'types'}
    )

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

    info = ma.Hyperlinks(
        {"kind": 'types', "content": 'topics'}
    )

type_schema =   TypeSchema()      
types_schema = TypeSchema(many=True) 

#                                                                                   The schema of  T O P I C S
class TopicSchema(SQLAlchemySchema):
    class Meta:
        model = Topics
        load_instance = True

    id = auto_field()
    name = auto_field()
    #asks = auto_field()                                this field will rise as ask object appears
    metas = auto_field()

    info = ma.Hyperlinks(
        {"kind": 'topics', "content": 'asks'}
    )

topic_schema =   TopicSchema()      
topics_schema = TopicSchema(many=True) 
