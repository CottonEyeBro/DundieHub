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

def create_groups():
    g1 = Group(
        group_name = "World's Best Boss",
        group_desc = 'Reserved for Dunder Mifflin Regional Managers with over 17 Dundies ONLY',
        group_started = datetime.datetime(month = 5, day = 12, year = 2023, hour = 6, minute = 21, second = 0, microsecond = 0, fold = 0)
    )
    g2 = Group(
        group_name = 'Bears, Beets, Battlestar Galactica Fanclub',
        group_desc = 'The only things that matter, objectively',
        group_started = datetime.datetime(month = 7, day = 11, year = 2023, hour = 11, minute = 4, second = 0, microsecond = 0, fold = 0)
    )
    groups = [g1, g2]
    return groups

def create_join_table():
    ug1 = User_Group(
        user_id = '1',
        group_id = '1'
    )
    ug2 = User_Group(
        user_id = '2',
        group_id = '2'
    )
    user_groups = [ug1, ug2]
    return user_groups

def create_posts():
    p1 = Post(
        content = "I love inside jokes. I'd love to be a part of one someday.",
        posted_at = datetime.datetime(month = 5, day = 12, year = 2023, hour = 6, minute = 21, second = 0, microsecond = 0, fold = 0),
        user_id = 1
    )
    p2 = Post(
        content = "I am fast. To give you a reference point, I'm somewhere between a snake and a mongoose… and a panther.",
        posted_at = datetime.datetime(month = 6, day = 19, year = 2023, hour = 3, minute = 15, second = 0, microsecond = 0, fold = 0),
        user_id = 2
    )
    posts = [p1, p2]
    return posts

def create_comments():
    c1 = Comment(
        content = "Dwight, you ignorant slut!",
        commented_at = datetime.datetime(month = 5, day = 12, year = 2023, hour = 6, minute = 21, second = 0, microsecond = 0, fold = 0),
        post_id = 2,
        user_id = 1
    )
    c2 = Comment(
        content = "Michael is like Mozart, and I'm like Butch Cassidy. You mess with Mozart and you're gonna get a bullet in your head, courtesy of Butch Cassidy.",
        commented_at = datetime.datetime(month = 6, day = 19, year = 2023, hour = 3, minute = 15, second = 0, microsecond = 0, fold = 0),
        post_id = 1,
        user_id = 2
    )
    comments = [c1, c2]
    return comments
    

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
        groups = create_groups()
        db.session.add_all(groups)
        db.session.commit()

        print("Seeding user_groups...")
        user_groups = create_join_table()
        db.session.add_all(user_groups)
        db.session.commit()

        print("Seeding posts...")
        posts = create_posts()
        db.session.add_all(posts)
        db.session.commit()

        print("Seeding comments...")
        comments = create_comments()
        db.session.add_all(comments)
        db.session.commit()

        print("Done seeding!... That's what she said!")

