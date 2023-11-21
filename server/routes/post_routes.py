from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app
from datetime import datetime

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

        user_id = form_data['user_id']
        content = form_data['content']

        try:

            # Get the current date and time as of posting
            current_datetime = datetime.utcnow()

            new_post_obj = Post(
                user_id = user_id,
                content = content,
                posted_at = current_datetime # Add the current date and time to the new_post_obj
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

@app.route('/posts/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def post_by_id(id):
    post = Post.query.filter(Post.id == id).first()

    if post:
        if request.method == 'GET':
    
            response = make_response(
                post.to_dict(),
                200
            )

        elif request.method == 'PATCH':
            form_data = request.get_json()

            try:
                for attr in form_data:
                    setattr(post, attr, form_data.get(attr))
                
                db.session.commit()

                response = make_response(
                    post.to_dict(),
                    202
                )

            except ValueError:
                response = make_response(
                    {"errors": ["validation errors in PATCH to posts id"]},
                    400
                )
                return response
            
        elif request.method == 'DELETE':
            db.session.delete(post)
            db.session.commit()

            response = make_response(
                {},
                204
            )
        
    else:
        response = make_response(
            {"error": "Post not found"},
            404
        )

    return response