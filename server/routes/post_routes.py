from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/posts', methods = ['GET', 'POST'])
def posts():

    if request.method == 'GET':
        posts = Post.query.all()
        post_dict = [post.to_dict() for post in posts]

        response = make_response(
            post_dict,
            200
        )

    elif request.method == 'POST':
        form_data = request.get_json()

        try:
            new_post_obj = Post(
                user_id = form_data['user_id'],
                content = form_data['content'],
                posted_at = form_data['posted_at']
            )

            db.session.add(new_post_obj)
            db.session.commit()

            response = make_response(
                new_post_obj.to_dict(),
                201
            )
        except ValueError:
            response = make_response(
                {"errors": ["validation errors in POST to posts"]},
                400
            )
            return response
        
    return response

@app.route('/posts/<int:id>', methods = ['GET'])
def post_by_id(id):
    post = Post.query.filter(Post.id == id).first()
    
    response = make_response(
        post.to_dict(),
        200
    )
    return response