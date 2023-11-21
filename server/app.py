#!/usr/bin/env python3

from config import app
from models import db, User
from flask import Flask, make_response, request, session
from datetime import datetime

from routes.user_routes import users, user_by_id
from routes.user_group_routes import user_groups, user_group_by_id
from routes.group_routes import groups, group_by_id
from routes.post_routes import posts, post_by_id
from routes.comment_routes import comments, comment_by_id

# Main Server View:
@app.route('/')
def index():
    return '<h1>Welcome to the DundieHub Server!</h1>'

# Non-RESTful Routing:
@app.route('/signup', methods = ['POST'])
def signup():
    # allow for user to signup new account
    form_data = request.get_json()

    name = form_data['name']
    username = form_data['username']
    password = form_data['password']

    try:

        # Get the current date and time
        current_datetime = datetime.utcnow()

        new_user = User(
            name = name,
            username = username,
            joined_on = current_datetime # Add the current date and time to the User object
        )
        # generates hashed password
        new_user.password_hash = password

        db.session.add(new_user)
        db.session.commit()

        # gives new user an id and sets signed in user to session
        session['user_id'] = new_user.id

        response = make_response(
            new_user.to_dict(),
            201
        )

    except:
        response = make_response(
            {"ERROR": "Could not create user!"},
            400
        )

    return response

@app.route('/check_user_session', methods = ['GET'])
def check_session():
    # check current session
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    if user:
        response = make_response(
            user.to_dict(), 
            200
        )
    else:
        response = make_response(
            {}, 
            404
        )
    return response

@app.route('/user_login', methods = ['POST'])
def user_login():
    # check if user can signin to account
    form_data = request.get_json()
    
    username = form_data['username']
    password = form_data['password']
    
    user = User.query.filter_by(username = username).first()
    if user:
        # authenticate user
        is_authenticated = user.authenticate(password)
        if is_authenticated:
            session['user_id'] = user.id
            resp = make_response(user.to_dict(), 201)
        else:
            resp = make_response({"ERROR" : "USER CANNOT LOG IN"}, 400)
    else:
        resp = make_response({"ERROR" : "USER NOT FOUND"}, 404)
    return resp

@app.route('/logout', methods = ['DELETE'])
def logout():
    # remove session
    session['user_id'] = None

    response = make_response(
        {},
        204
    )

    return response

# Run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)

