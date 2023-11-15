from flask import Flask, make_response, request
from models import db, User, User_Group, Group, Post, Comment
from config import app

@app.route('/groups', methods = ['GET', 'POST'])
def groups():

    if request.method == 'GET':
        groups = Group.query.all()
        group_dict = [group.to_dict() for group in groups]

        response = make_response(
            group_dict,
            200
        )

    elif request.method == 'POST':
        form_data = request.get_json()

        try:
            new_group_obj = Group(
                group_name = form_data['group_name'],
                group_desc = form_data['group_desc'],
                group_started = form_data['group_started']
            )

            db.session.add(new_group_obj)
            db.session.commit()

            response = make_response(
                new_group_obj.to_dict(),
                201
            )
        except ValueError:
            response = make_response(
                {"errors": ["validation errors in POST to groups"]},
                400
            )
            return response

    return response

@app.route('/groups/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def group_by_id(id):
    group = Group.query.filter(Group.id == id).first()

    if group:
        if request.method == 'GET':
    
            response = make_response(
                group.to_dict(),
                200
            )

        elif request.method == 'PATCH':
            form_data = request.get_json()

            try:
                for attr in form_data:
                    setattr(group, attr, form_data.get(attr))
                
                db.session.commit()

                response = make_response(
                    group.to_dict(),
                    202
                )

            except ValueError:
                response = make_response(
                    {"errors": ["validation errors in PATCH to groups id"]},
                    400
                )
                return response
            
        elif request.method == 'DELETE':
            db.session.delete(group)
            db.session.commit()

            response = make_response(
                {},
                204
            )
        
    else:
        response = make_response(
            {"error": "Group not found"},
            404
        )

    return response