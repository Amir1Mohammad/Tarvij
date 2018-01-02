#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;
from controller.garbage import create_user_id

__author__ = "Amir Mohammad"

# flask imports :
from flask import render_template, flash, request, redirect, url_for, abort, jsonify

# project imports :
from controller import app
from models.user import User
from models.macros import Mac
from models.handbook import Handbook
from controller.extension import db

# TODO add log in the functions .
# TODO for login and logout and add_data and delete_data .


@app.route('/admin_home', methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_obj = User.query.filter_by(username=username).first_or_404()
    if user_obj.passwordhash != password:
        abort(403)
    user_obj.login()
    if username == "tecvest@1010":
        return render_template('admin_home.html')
    else:
        return render_template("enter_data.html")



@app.route('/')
def index():
    return render_template('login.html')

@app.route("/logout")
def logout():
    User.logout()
    return render_template('login.html')


@app.route('/test')
def begin():
    return render_template('enter_data.html')

@app.route('/matlab', methods=['POST', 'GET'])
def submit1():
    title = request.form['title']
    contetnt = request.form['content']

    macro_obj = Mac( username = User.logged_in_user(), title = title, content = contetnt)
    db.session.add(macro_obj)
    db.session.commit()
    user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
    return jsonify(user_obj.to_json()), 200

@app.route('/handbook', methods=['POST', 'GET'])
def submit2():
    book = request.form['book']
    handbook_obj = Handbook(username = User.logged_in_user(), handbook = book)
    db.session.add(handbook_obj)
    db.session.commit()
    user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
    return jsonify(user_obj.to_json()), 200
# @app.route('/accept', methods=['GET'])
# def accept():
#     return render_template('accept.html')
