from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/user_groups', methods = ['GET', 'POST'])
def user_groups():

    if request.method == 'GET':
        user_groups = User_Group.query.all()
        user_group_dict = [user_group.to_dict() for user_group in user_groups]

        response = make_response(
            user_group_dict,
            200
        )

    elif request.method == 'POST':
        form_data = request.get_json()

        try:
            new_user_group_obj = User_Group(
                user_id = form_data['user_id'],
                group_id = form_data['group_id']
            )

            db.session.add(new_user_group_obj)
            db.session.commit()

            response = make_response(
                new_user_group_obj.to_dict(),
                201
            )
        except ValueError:
            response = make_response(
                {"errors": ["validation errors in POST to user_groups"]},
                400
            )
            return response

    return response

@app.route('/user_groups/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def user_group_by_id(id):
    user_group = User_Group.query.filter(User_Group.join_table_id == id).first()

    if user_group:
        if request.method == 'GET':
    
            response = make_response(
                user_group.to_dict(),
                200
            )

        elif request.method == 'PATCH':
            form_data = request.get_json()

            try:
                for attr in form_data:
                    setattr(user_group, attr, form_data.get(attr))
                
                db.session.commit()

                response = make_response(
                    user_group.to_dict(),
                    202
                )

            except ValueError:
                response = make_response(
                    {"errors": ["validation errors in PATCH to user_groups id"]},
                    400
                )
                return response
            
        elif request.method == 'DELETE':
            db.session.delete(user_group)
            db.session.commit()

            response = make_response(
                {},
                204
            )
        
    else:
        response = make_response(
            {"error": "User_group not found"},
            404
        )

    return response