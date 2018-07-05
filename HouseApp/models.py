# -*- encoding=UTF-8 -*-

from HouseApp import db


class User(db.Model):
    username = db.Column(db.String(50), primary_key=True, unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(30))
    Tel = db.Column(db.String(20))
    salt = db.Column(db.String(32))

    def __init__(self, username, password, email, tel=0, salt=''):
        self.username = username
        self.password = password
        self.email = email
        self.Tel = tel
        self.salt = salt

    def __repr__(self, username):
        return '<User %s>' % username


