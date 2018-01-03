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
from log import add_log


# TODO add log in the functions .
# TODO for login and logout and add_data and delete_data .


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if User.logged_in_user() is None:
            abort(403)
        elif User.logged_in_user() == "tecvest@1010":
            return render_template('admin_home.html')
        else:
            return render_template("enter_data.html")

    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user_obj = User.query.filter_by(username=username).first_or_404()
        if user_obj.passwordhash != password:
            abort(403)
        user_obj.login()
        add_log(username, "Login")
        if username == "tecvest@1010":
            return render_template('admin_home.html')
        else:
            return render_template("enter_data.html")
    else:
        abort(405)


@app.route('/')
def index():
    return render_template('login.html')


@app.route("/logout", methods=["POST", 'GET'])
def logout():
    username = User.logged_in_user()
    add_log(username, "Logout")
    User.logout()
    return render_template('login.html')


@app.route('/matlab', methods=['POST', 'GET'])
def submit1():

    title = request.form['title']
    contetnt = request.form['content']
    macro_obj = Mac(username=User.logged_in_user(), title=title, content=contetnt)
    db.session.add(macro_obj)
    db.session.commit()
    user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
    add_log(User.logged_in_user(), "Adding data with form 1")
    return jsonify(user_obj.to_json()), 200


@app.route('/handbook', methods=['POST', 'GET'])
def submit2():
    book = request.form['book']
    handbook_obj = Handbook(username=User.logged_in_user(), handbook=book)
    db.session.add(handbook_obj)
    db.session.commit()
    user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
    add_log(User.logged_in_user(), "Adding data with form 4")
    return jsonify(user_obj.to_json()), 200
