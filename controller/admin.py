#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports :
from flask import render_template


# project imports :
from models.user import User
from models.log import Log
from controller import app
from controller.extension import db
from garbage import create_user_id

__Author__ = "Amir Mohammad"


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


@app.route('/log/<username>')
def show_log_name(username):
    log_obj_q = Log.query.filter_by(username=username).first_or_404()
    return render_template('show_user_name.html', log_obj_q=log_obj_q)


# fixme : only show first log on DB .
@app.route('/log', methods=['GET'])
def show_log_all():
    log_obj_q = Log.query.order_by(Log.username).all()
    print "username is : ", log_obj_q.username
    # print "action is : ", log_obj_q.action
    # print "time is : ", log_obj_q.time
    return render_template('show_user_date.html', log_obj_q=log_obj_q)
