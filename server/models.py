from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db

class User(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'users'

    # Serialize Rules
    serialize_rules = ('-user_groups.user', '-user_groups.group', '-posts.user', '-comments.user', '-comments.post', '-posts.comments')

    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    joined_on = db.Column(db.String)
    # profile_photo = db.Column() -------------------------> Stretch goal


    # Relationships
    user_groups = db.relationship('User_Group', back_populates = 'user')
    posts = db.relationship('Post', back_populates = 'user')
    comments = db.relationship('Comment', back_populates = 'user')

    # Association Proxy
    # groups = association_proxy('user_groups', 'groups')

    # Validations
    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError('User must be given a name')
        
    @validates('username')
    def validates_username(self, key, username):
        if username:
            return username
        else:
            raise ValueError('User must be given a unique username')
        
    @validates('password')
    def validates_password(self, key, password):
        if password:
            return password
        else:
            raise ValueError('User must be given a password')

    # __repr__
    def __repr__(self):
        return f'<User {self.id}: {self.name}. Username: {self.username}. Password: {self.password}. Joined: {self.joined_on}.\n>'




class User_Group(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'user_groups'

    # Serialize Rules
    serialize_rules = ('-user.user_groups', '-group.user_groups', '-user.comments', '-user.posts')

    # Build Table Columns
    join_table_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    # Relationships
    user = db.relationship('User', back_populates = 'user_groups')
    group = db.relationship('Group', back_populates = 'user_groups')

    # __repr__
    def __repr__(self):
        return f'<User Group {self.join_table_id}: User ID: {self.user_id}. Group ID: {self.group_id}.\n>'




class Group(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'groups'

    # Serialize Rules
    serialize_rules = ('-user_groups.group', '-user_groups.user')

    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    group_name = db.Column(db.String, unique = True)
    group_desc = db.Column(db.String)
    group_started = db.Column(db.String)

    # Relationships
    user_groups = db.relationship('User_Group', back_populates = 'group')

    # Association Proxy
    # users = association_proxy('user_groups', 'users')

    # Validations
    @validates('group_name')
    def validates_group_name(self, key, group_name):
        if group_name:
            return group_name
        else:
            raise ValueError('Group must be given a unique name')
        
    @validates('group_desc')
    def validates_group_desc(self, key, group_desc):
        if group_desc:
            return group_desc
        else:
            raise ValueError('Group must be given a description')

    # __repr__
    def __repr__(self):
        return f'<Group {self.id}: {self.group_name}. Group Description: {self.group_desc}. Group Started: {self.group_started}.\n>'




class Post(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'posts'

    # Serialize Rules
    serialize_rules = ('-user.posts', '-comments.post', '-user.user_groups', '-comments.user', '-user.comments')

    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    posted_at = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # img_content = db.Column() -------------------------> Stretch goal

    # Relationships
    user = db.relationship('User', back_populates = 'posts')
    comments = db.relationship('Comment', back_populates = 'post')

    # Validations
    @validates('content')
    def validates_content(self, key, content):
        if content:
            return content
        else:
            raise ValueError('Post must contain content')

    # __repr__
    def __repr__(self):
        return f'<Post {self.id}: Content {self.content}. Posted At: {self.posted_at}. User ID: {self.user_id}.\n>'




class Comment(db.Model, SerializerMixin): # ====================================================================================================================
    __tablename__ = 'comments'

    # Serialize Rules
    serialize_rules = ('-user.comments', '-post.comments', '-user.user_groups', '-post.user', '-user.posts')

    # Build Table Columns
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    commented_at = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    # img_content = db.Column() -------------------------> Stretch goal 

    # Relationships
    user = db.relationship('User', back_populates = 'comments')
    post = db.relationship('Post', back_populates = 'comments')

    # Validations
    @validates('content')
    def validates_content(self, key, content):
        if content:
            return content
        else:
            raise ValueError('Comment must contain content')

    # __repr__
    def __repr__(self):
        return f'<Comment {self.id}: Content {self.content}. Commented At: {self.commented_at}. User ID: {self.user_id}. Post ID: {self.post_id}.\n>'