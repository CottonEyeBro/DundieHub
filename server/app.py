#!/usr/bin/env python3

from config import app
from routes.user_routes import users, user_by_id
from routes.user_group_routes import user_groups, user_group_by_id
from routes.group_routes import groups, group_by_id
from routes.post_routes import posts, post_by_id
from routes.comment_routes import comments, comment_by_id

# Main Server View:
@app.route('/')
def index():
    return '<h1>Cooper Lindsley Capstone Project Server</h1>'

# Run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)

