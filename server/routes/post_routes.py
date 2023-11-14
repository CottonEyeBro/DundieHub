from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/posts', methods = ['GET'])
def posts():
    posts = Post.query.all()
    post_dict = [post.to_dict() for post in posts]

    response = make_response(
        post_dict,
        200
    )
    return response