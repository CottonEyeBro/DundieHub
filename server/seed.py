#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
import datetime

# Local imports
from app import app
from models import db, User, User_Group, Group, Post, Comment

# Seed Functions:
def create_users():
    u1 = User(
        name = 'Michael Scott',
        username = 'agentmichaelscarn',
        password = 'iluvpaper1234',
        joined_on = datetime.datetime(month = 3, day = 24, year = 2005, hour = 12, minute = 0, second = 0, microsecond = 0, fold = 0)
    )
    u2 = User(
        name = 'Dwight Schrute',
        username = 'schrutefarmsbnb',
        password = 'iluvmichael1234',
        joined_on = datetime.datetime(month = 3, day = 24, year = 2005, hour = 12, minute = 1, second = 0, microsecond = 0, fold = 0)
    )
    users = [u1, u2]
    return users
    

if __name__ == '__main__':
    with app.app_context():
        print("Clearing Database(db)...")
        User.query.delete()
        Group.query.delete()
        User_Group.query.delete()
        Post.query.delete()
        Comment.query.delete()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding groups...")
        print("Seeding user_groups...")
        print("Seeding posts...")
        print("Seeding comments...")

        print("Done seeding!... That's what she said!")

