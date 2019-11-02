#!/usr/bin/env python
"""mysql"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 21:04
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Fianna'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(64), unique=True, nullable=True)
    age = db.Column(db.Integer, nullable=True, server_default='0')
    height = db.Column(db.Integer, nullable=True, server_default='0')
    weight = db.Column(db.Integer, nullable=True, server_default='0')

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f'<User {self.name}{self.age}>'
