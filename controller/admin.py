#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports :
from flask import render_template, jsonify, request, abort, redirect
# python imports :
import unicodedata

# project imports :
from models.user import User
from models.log import Log
from controller import app
from controller.extension import db
from garbage import create_user_id

__Author__ = "Amir Mohammad"


@app.route('/add_admin',methods=['POST','GET'])
def add_admin():
    username = request.form['username']
    passwordhash = request.form['password']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    gender = request.form['gender']
    phones = request.form['phone']
    brand = request.form['brand']
    category = request.form['category']
    user_obj = User(id=create_user_id(), username=username, passwordhash=passwordhash, firstname=firstname,
                    lastname=lastname,
                    gender=gender, phones=phones, brand=brand, category=category)

    db.session.add(user_obj)
    db.session.commit()

    return jsonify(msg = "added successfully"), 200


def delete_admin(username):
    user_obj = User(username=username)
    db.session.delete(user_obj)
    db.session.commit()


@app.route('/log/<username>')
def show_log_name(username):
    user_obj = User.query.filter_by(username=username).first_or_404()
    print user_obj.to_json()

    return jsonify(user_obj.to_json())
    # return render_template('show_user_name.html', log_obj_q=user_obj.to_json())


# fixme : only show first log on DB .
@app.route('/log', methods=['GET'])
def show_log_all():
    if User.logged_in_user() == "tecvest@1010":
        log_obj_q = Log.query.all()
        # print jsonify(logs=[i.to_json(with_user=True) for i in log_obj_q]), 200
        # print "action is : ", log_obj_q.action
        # print "time is : ", log_obj_q.time
        return render_template('show_user_date.html', log_obj_q=log_obj_q)
    else:
        abort(403)


@app.route('/', methods= ['GET', 'Post'])
def to_add_admin():
    if request.form['Work'] == 'add_admin' :
        return render_template('add_admin.html')

    elif request.form['Work'] == 'view_logs':
        return redirect('log')
