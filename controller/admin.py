#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports :


# project imports :
from models.user import User
from controller import app
from controller.extension import db
from garbage import create_user_id

__Author__ = "Amir Mohammad"


# fixme . maybe the table is not created .
@app.route('/admin', methods=['POST'])
def add_admin(username, passwordhash, firstname, lastname, gender, phones, brand, category):
    user_obj = User(id=create_user_id(), username=username, passwordhash=passwordhash, firstname=firstname,
                    lastname=lastname,
                    gender=gender, phones=phones, brand=brand, category=category)

    db.session.add(user_obj)
    db.session.commit()


def delete_admin(username):
    user_obj = User(username=username)
    db.session.delete(user_obj)
    db.session.commit()


def show_log_name():
    pass


def show_log_date():
    pass


def show_log_all():
    pass
