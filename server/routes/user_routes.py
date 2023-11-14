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