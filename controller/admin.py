#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;
from flask import render_template
from garbage import create_user_id

__Author__ = "Amir Mohammad"

# python imports:

# project import :
from controller import app
from models.user import User

from controller.extension import db


# fixme . maybe the table is not created .
def add_admin(username, passwordhash, firstname, lastname, gender, phones, brand, category):
    user_obj = User(id=create_user_id(), username=username, passwordhash=passwordhash, firstname=firstname,
                    lastname=lastname,
                    gender=gender, phones=phones, brand=brand, category=category)

    db.session.add(user_obj)
    db.session.commit()
    print "add admin Done !"


# add_admin('amir', 'mypass', 'amirmohammad', 'mohammadi', 'Male', 123456, 'giah', 'zorat')


def delete_admin(username):
    user_obj = User(username=username)
    db.session.delete(user_obj)
    db.session.commit()
