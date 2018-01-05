#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


__author__ = "Amir Mohammad"

# flask imports :
from flask import render_template, request, abort

# project imports :
from controller import app
from models.user import User
from log import add_log


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


