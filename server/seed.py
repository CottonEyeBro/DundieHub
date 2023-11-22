#!/usr/bin/env python3

# Remote library imports
import datetime
from config import db, bcrypt

# Local imports
from app import app
from models import db, User, User_Group, Group, Post, Comment

# Seed Functions:
def create_users():
    u1 = User(
        name = 'Michael Scott',
        username = 'agentmichaelscarn',
        profile_image_url = './images/Michael.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 0, second = 0, microsecond = 0, fold = 0)
    )
    u1.password_hash = 'iluvpaper1234'
    u2 = User(
        name = 'Dwight Schrute',
        username = 'schrutefarmsbnb',
        profile_image_url = './images/Dwight.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 1, second = 0, microsecond = 0, fold = 0)
    )
    u2.password_hash = 'iluvmichael1234'
    u3 = User(
        name = 'Jim Halpert',
        username = 'bigtuna',
        profile_image_url = './images/Jim.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 2, second = 0, microsecond = 0, fold = 0)
    )
    u3.password_hash = 'iluvpam1234'
    u4 = User(
        name = 'Pam Beesly',
        username = 'whitestsneakers',
        profile_image_url = './images/Pam.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 3, second = 0, microsecond = 0, fold = 0)
    )
    u4.password_hash = 'iluvjim1234'
    u5 = User(
        name = 'Creed Bratton',
        username = 'irontothefire',
        profile_image_url = './images/Creed.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 4, second = 0, microsecond = 0, fold = 0)
    )
    u5.password_hash = 'iamthescrantonstrangler'
    u6 = User(
        name = 'Stanley Hudson',
        username = 'iamtoooldforthis',
        profile_image_url = './images/Stanley.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 5, second = 0, microsecond = 0, fold = 0)
    )
    u6.password_hash = 'iluvpretzelday1234'
    u7 = User(
        name = 'Andy Bernard',
        username = 'herecomestreble',
        profile_image_url = './images/Andy.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 6, second = 0, microsecond = 0, fold = 0)
    )
    u7.password_hash = 'iluvcornell1234'
    u8 = User(
        name = 'Angela Martin',
        username = 'kittymom452',
        profile_image_url = './images/Angela.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 7, second = 0, microsecond = 0, fold = 0)
    )
    u8.password_hash = 'iluvmycats1234'
    u9 = User(
        name = 'Kevin Malone',
        username = 'scrantonicity2',
        profile_image_url = './images/Kevin.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 8, second = 0, microsecond = 0, fold = 0)
    )
    u9.password_hash = 'iluvchili1234'
    u10 = User(
        name = 'Ryan Howard',
        username = 'iamthetemp',
        profile_image_url = './images/Ryan.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 9, second = 0, microsecond = 0, fold = 0)
    )
    u10.password_hash = 'iluvmoney1234'
    u11 = User(
        name = 'Oscar Martinez',
        username = 'bacchusgodofwine',
        profile_image_url = './images/Oscar.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 10, second = 0, microsecond = 0, fold = 0)
    )
    u11.password_hash = 'iluvaccounting1234'
    u12 = User(
        name = 'Kelly Kapoor',
        username = 'ryanloverxoxo',
        profile_image_url = './images/Kelly.png',
        joined_on = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 11, second = 0, microsecond = 0, fold = 0)
    )
    u12.password_hash = 'iluvryan1234'
    
    users = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12]
    return users

def create_groups():
    g1 = Group(
        group_name = "World's Best Boss",
        group_desc = 'Reserved for Dunder Mifflin Regional Managers with over 17 Dundies ONLY',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 12, second = 0, microsecond = 0, fold = 0)
    )
    g2 = Group(
        group_name = 'Bears, Beets, Battlestar Galactica Fanclub',
        group_desc = 'The only things that matter, objectively',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 13, second = 0, microsecond = 0, fold = 0)
    )
    g3 = Group(
        group_name = 'Office Romantics',
        group_desc = 'Reserved for all those who have caught the lovebug in the office',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 14, second = 0, microsecond = 0, fold = 0)
    )
    g4 = Group(
        group_name = 'Accounting 4 Life',
        group_desc = 'The Accounting Department',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 15, second = 0, microsecond = 0, fold = 0)
    )
    g5 = Group(
        group_name = 'Assistant(s) to the Regional Manager',
        group_desc = 'We are in charge (unless Michael says differently)',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 16, second = 0, microsecond = 0, fold = 0)
    )
    g6 = Group(
        group_name = 'Harcore Parkour Club',
        group_desc = 'PARKOUR!',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 17, second = 0, microsecond = 0, fold = 0)
    )
    g7 = Group(
        group_name = '(former) Michael Scott Paper Company Employees',
        group_desc = 'I will not beat. I will never give up. I am on a mission. That is the Michael Scott [Paper Company] guarantee.',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 18, second = 0, microsecond = 0, fold = 0)
    )
    g8 = Group(
        group_name = 'Creed Thoughts Subscribers',
        group_desc = 'www.creedthoughts.gov.www\creedthoughts',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 19, second = 0, microsecond = 0, fold = 0)
    )
    g9 = Group(
        group_name = 'Pretzel Day Enthusiasts',
        group_desc = 'It is all about the pretzels',
        group_started = datetime.datetime(month = 11, day = 20, year = 2023, hour = 1, minute = 20, second = 0, microsecond = 0, fold = 0)
    )
    groups = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
    return groups

def create_join_table():
    ug1 = User_Group(
        user_id = '1',
        group_id = '1'
    )
    ug2 = User_Group(
        user_id = '1',
        group_id = '6'
    )
    ug3 = User_Group(
        user_id = '1',
        group_id = '7'
    )
    ug4 = User_Group(
        user_id = '1',
        group_id = '9'
    )
    ug5 = User_Group(
        user_id = '2',
        group_id = '2'
    )
    ug6 = User_Group(
        user_id = '2',
        group_id = '3'
    )
    ug7 = User_Group(
        user_id = '2',
        group_id = '5'
    )
    ug8 = User_Group(
        user_id = '2',
        group_id = '6'
    )
    ug9 = User_Group(
        user_id = '3',
        group_id = '3'
    )
    ug10 = User_Group(
        user_id = '4',
        group_id = '3'
    )
    ug11 = User_Group(
        user_id = '4',
        group_id = '7'
    )
    ug12 = User_Group(
        user_id = '5',
        group_id = '8'
    )
    ug13 = User_Group(
        user_id = '6',
        group_id = '9'
    )
    ug14 = User_Group(
        user_id = '7',
        group_id = '3'
    )
    ug15 = User_Group(
        user_id = '7',
        group_id = '5'
    )
    ug16 = User_Group(
        user_id = '7',
        group_id = '6'
    )
    ug17 = User_Group(
        user_id = '8',
        group_id = '3'
    )
    ug18 = User_Group(
        user_id = '8',
        group_id = '4'
    )
    ug19 = User_Group(
        user_id = '9',
        group_id = '4'
    )
    ug20 = User_Group(
        user_id = '10',
        group_id = '3'
    )
    ug21 = User_Group(
        user_id = '10',
        group_id = '7'
    )
    ug22 = User_Group(
        user_id = '11',
        group_id = '4'
    )
    ug23 = User_Group(
        user_id = '12',
        group_id = '3'
    )
    user_groups = [ug1, ug2, ug3, ug4, ug5, ug6, ug7, ug8, ug9, ug10, ug11, ug12, ug13, ug14, ug15, ug16, ug17, ug18, ug19, ug20, ug21, ug22, ug23]
    return user_groups

def create_posts():
    p1 = Post(
        content = "I love inside jokes. I'd love to be a part of one someday.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 7, minute = 30, second = 0, microsecond = 0, fold = 0),
        user_id = 1
    )
    p2 = Post(
        content = "I am fast. To give you a reference point, I'm somewhere between a snake and a mongoose… and a panther.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 7, minute = 35, second = 0, microsecond = 0, fold = 0),
        user_id = 2
    )
    p3 = Post(
        content = "Dwight, at 8:00 AM today, someone poisons the coffee. DO NOT DRINK THE COFFEE! More instructions will follow. Cordially, Future Dwight.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 7, minute = 55, second = 0, microsecond = 0, fold = 0),
        user_id = 3
    )
    p4 = Post(
        content = "Last year, my performance review started with Michael asking me what my hopes and dreams were and it ended with him telling me he could bench press 190 pounds.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 8, minute = 15, second = 0, microsecond = 0, fold = 0),
        user_id = 4
    )
    p5 = Post(
        content = "I've been involved in a number of cults both as a leader and a follower. You have more fun as a follower but you make more money as a leader.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 8, minute = 45, second = 0, microsecond = 0, fold = 0),
        user_id = 5
    )
    p6 = Post(
        content = "I wake up every morning in a bed that's too small, drive my daughter to a school that's too expensive, and then I go to work to a job for which I get paid too little, but on pretzel day? Well, I like pretzel day...",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 9, minute = 20, second = 0, microsecond = 0, fold = 0),
        user_id = 6
    )
    p7 = Post(
        content = "I graduated from anger management the same way I graduated from Cornell; on time. Now I'm back, got a second chance, and I'm not gonna blow it. So LOOK OUT, DUNDER MIFFLIN... I mean look out in a fun way and not like I'm gonna hurt you...",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 9, minute = 30, second = 0, microsecond = 0, fold = 0),
        user_id = 7
    )
    p8 = Post(
        content = "Sometimes the clothes at Gap Kids are just too flashy so I'm forced to go to the American Girl store and order clothes for large, colonial dolls.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 9, minute = 35, second = 0, microsecond = 0, fold = 0),
        user_id = 8
    )
    p9 = Post(
        content = "I just wanna lie on the beach and eat hot dogs. That's all I've ever wanted.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 9, minute = 45, second = 0, microsecond = 0, fold = 0),
        user_id = 9
    )
    p10 = Post(
        content = "You got your sheep, and you got your black sheep, and I'm not even a sheep. I'm on the freakin' moon.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 9, minute = 50, second = 0, microsecond = 0, fold = 0),
        user_id = 10
    )
    p11 = Post(
        content = "I am super cool. I am an accountant at a failing paper supply company in Scranton. Much like Sir Ian McKellen.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 10, minute = 10, second = 0, microsecond = 0, fold = 0),
        user_id = 11
    )
    p12 = Post(
        content = "I never really thought about death till Princess Diana died. That was the saddest funeral ever. That and my sister's.",
        posted_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 10, minute = 15, second = 0, microsecond = 0, fold = 0),
        user_id = 12
    )
    posts = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    return posts

def create_comments():
    c1 = Comment(
        content = "Dwight, you ignorant slut!",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 7, minute = 36, second = 0, microsecond = 0, fold = 0),
        post_id = 2,
        user_id = 1
    )
    c2 = Comment(
        content = "Identity theft is not a joke, Jim! Millions of families suffer every year!",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 7, minute = 56, second = 0, microsecond = 0, fold = 0),
        post_id = 3,
        user_id = 2
    )
    c3 = Comment(
        content = "Now, exactly, how much pot did you smoke?",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 7, minute = 37, second = 0, microsecond = 0, fold = 0),
        post_id = 2,
        user_id = 3
    )
    c4 = Comment(
        content = "Cool beans man. I live by the quarry. We should hang out by the quarry and throw things down there!",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 10, minute = 11, second = 0, microsecond = 0, fold = 0),
        post_id = 11,
        user_id = 5
    )
    c5 = Comment(
        content = "Boy, have you lost your mind? 'cause I'll help ya find it!",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 9, minute = 51, second = 0, microsecond = 0, fold = 0),
        post_id = 10,
        user_id = 6
    )
    c6 = Comment(
        content = "I thought Rajnigandha was a boy's name...",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 8, minute = 17, second = 0, microsecond = 0, fold = 0),
        post_id = 4,
        user_id = 9
    )
    c7 = Comment(
        content = "Actually...",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 8, minute = 46, second = 0, microsecond = 0, fold = 0),
        post_id = 5,
        user_id = 11
    )
    c8 = Comment(
        content = "WELL, MY MIDDLE NAME IS RAJNIGANDHA AND I HATE IT!!!!!",
        commented_at = datetime.datetime(month = 11, day = 20, year = 2023, hour = 8, minute = 16, second = 0, microsecond = 0, fold = 0),
        post_id = 4,
        user_id = 12
    )
    comments = [c1, c2, c3, c4, c5, c6, c7, c8]
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

