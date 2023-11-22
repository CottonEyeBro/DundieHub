from flask import Flask, make_response, request, session
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/users', methods = ['GET', 'POST'])
def users():

    if request.method == 'GET':
        users = User.query.all()
        user_dict = [user.to_dict() for user in users]

        response = make_response(
            user_dict,
            200
        )

    elif request.method == 'POST':
        form_data = request.get_json()

        try:
            new_user_obj = User(
                name = form_data['name'],
                username = form_data['username'],
                password = form_data['password'],
                joined_on = form_data['joined_on']
            )

            db.session.add(new_user_obj)
            db.session.commit()

            response = make_response(
                new_user_obj.to_dict(),
                201
            )
        except ValueError:
            response = make_response(
                {"errors": ["validation errors in POST to users"]},
                400
            )
            return response

    return response

@app.route('/users/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if user:
        if request.method == 'GET':
    
            response = make_response(
                user.to_dict(),
                200
            )

        elif request.method == 'PATCH':
            form_data = request.get_json()

            try:
                for attr in form_data:
                    setattr(user, attr, form_data.get(attr))
                
                db.session.commit()

                response = make_response(
                    user.to_dict(),
                    202
                )

            except ValueError:
                response = make_response(
                    {"errors": ["validation errors in PATCH to users id"]},
                    400
                )
                return response
            
        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

            response = make_response(
                {},
                204
            )
        
    else:
        response = make_response(
            {"error": "User not found"},
            404
        )

    return response