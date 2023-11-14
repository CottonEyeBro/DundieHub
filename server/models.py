from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)





class User(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'users'

    # Serialize Rules


    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String, unique = True)
    joined_on = db.Column(db.String)
    # profile_photo = db.Column() -------------------------> Stretch goal


    # Relationships


    # Validations


    # __repr__
    def __repr__(self):
        return f'<User {self.id}: {self.name}. Username: {self.username}. Password: {self.password}. Joined: {self.joined_on}.\n>'




class User_Group(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'user_groups'

    # Serialize Rules


    # Build Table Columns
    join_table_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    # Relationships


    # Validations


    # __repr__
    def __repr__(self):
        return f'<User Group {self.join_table_id}: User ID: {self.user_id}. Group ID: {self.group_id}.\n>'




class Group(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'groups'

    # Serialize Rules


    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    group_name = db.Column(db.String, unique = True)
    group_desc = db.Column(db.String)
    group_started = db.Column(db.String)

    # Relationships


    # Validations


    # __repr__
    def __repr__(self):
        return f'<Group {self.id}: {self.group_name}. Group Description: {self.group_desc}. Group Started: {self.group_started}.\n>'




class Post(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'posts'

    # Serialize Rules


    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    posted_at = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # img_content = db.Column() -------------------------> Stretch goal

    # Relationships


    # Validations


    # __repr__
    def __repr__(self):
        return f'<Post {self.id}: Content {self.content}. Posted At: {self.posted_at}. User ID: {self.user_id}.\n>'




class Comment(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'comments'

    # Serialize Rules


    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    commented_at = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    # img_content = db.Column() -------------------------> Stretch goal 

    # Relationships


    # Validations


    # __repr__
    def __repr__(self):
        return f'<Comment {self.id}: Content {self.content}. Commented At: {self.commented_at}. User ID: {self.user_id}. Post ID: {self.post_id}.\n>'