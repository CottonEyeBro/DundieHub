from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/user_groups', methods = ['GET'])
def user_groups():
    user_groups = User_Group.query.all()
    user_group_dict = [user_group.to_dict() for user_group in user_groups]

    response = make_response(
        user_group_dict,
        200
    )
    return response