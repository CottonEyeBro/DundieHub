from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/users', methods = ['GET'])
def users():
    users = User.query.all()
    user_dict = [user.to_dict() for user in users]

    response = make_response(
        user_dict,
        200
    )
    return response

@app.route('/users/<int:id>', methods = ['GET'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()
    
    response = make_response(
        user.to_dict(),
        200
    )
    return response