from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/comments', methods = ['GET'])
def comments():
    comments = Comment.query.all()
    comment_dict = [comment.to_dict() for comment in comments]

    response = make_response(
        comment_dict,
        200
    )
    return response

@app.route('/comments/<int:id>', methods = ['GET'])
def comment_by_id(id):
    comment = Comment.query.filter(Comment.id == id).first()
    
    response = make_response(
        comment.to_dict(),
        200
    )
    return response