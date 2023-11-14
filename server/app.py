#!/usr/bin/env python3

from config import app
from routes.user_routes import users

# Main Server View:
@app.route('/')
def index():
    return '<h1>Cooper Lindsley Capstone Project Server</h1>'

# Run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)

