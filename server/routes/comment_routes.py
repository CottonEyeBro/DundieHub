from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/comments', methods = ['GET', 'POST'])
def comments():

    if request.method == 'GET':
        comments = Comment.query.all()
        comment_dict = [comment.to_dict() for comment in comments]

        response = make_response(
            comment_dict,
            200
        )

    elif request.method == 'POST':
        form_data = request.get_json()

        try:
            new_comment_obj = Comment(
                user_id = form_data['user_id'],
                post_id = form_data['post_id'],
                content = form_data['content'],
                commented_at = form_data['commented_at']
            )

            db.session.add(new_comment_obj)
            db.session.commit()

            response = make_response(
                new_comment_obj.to_dict(),
                201
            )
        except ValueError:
            response = make_response(
                {"errors": ["validation errors in POST to comments"]},
                400
            )
            return response
        
    return response

@app.route('/comments/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def comment_by_id(id):
    comment = Comment.query.filter(Comment.id == id).first()

    if comment:
        if request.method == 'GET':
    
            response = make_response(
                comment.to_dict(),
                200
            )

        elif request.method == 'PATCH':
            form_data = request.get_json()

            try:
                for attr in form_data:
                    setattr(comment, attr, form_data.get(attr))
                
                db.session.commit()

                response = make_response(
                    comment.to_dict(),
                    202
                )

            except ValueError:
                response = make_response(
                    {"errors": ["validation errors in PATCH to comments id"]},
                    400
                )
                return response
            
        elif request.method == 'DELETE':
            db.session.delete(comment)
            db.session.commit()

            response = make_response(
                {},
                204
            )
        
    else:
        response = make_response(
            {"error": "Comment not found"},
            404
        )

    return response