from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'




class User_Group(db.Model, SerializerMixin):
    __tablename__ = 'user_groups'




class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'




class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'




class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'