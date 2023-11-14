#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
import datetime

# Local imports
from app import app
from models import db, User, User_Group, Group, Post, Comment

if __name__ == '__main__':
    with app.app_context():
        print("Clearing Database(db)...")
        User.query.delete()
        # Group.query.delete()
        # User_Group.query.delete()
        # Post.query.delete()
        # Comment.query.delete()

        print("Seeding users...")
        print("Seeding groups...")
        print("Seeding user_groups...")
        print("Seeding posts...")
        print("Seeding comments...")

        print("Done seeding!... That's what she said!")

