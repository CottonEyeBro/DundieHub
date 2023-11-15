from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/groups', methods = ['GET'])
def groups():
    groups = Group.query.all()
    group_dict = [group.to_dict() for group in groups]

    response = make_response(
        group_dict,
        200
    )
    return response

@app.route('/groups/<int:id>', methods = ['GET'])
def group_by_id(id):
    group = Group.query.filter(Group.id == id).first()
    
    response = make_response(
        group.to_dict(),
        200
    )
    return response