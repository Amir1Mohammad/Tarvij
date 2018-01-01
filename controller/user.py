#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__author__ = "Amir Mohammad"

# flask imports :
from flask import render_template, flash, request, redirect, url_for, abort

# project imports :
from controller import app
from models.user import User

@app.route('/admin_home', methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_obj = User.query.filter_by(username=username).first_or_404()
    if user_obj.passwordhash != password:
        abort(403)
    user_obj.login()
    return render_template('admin_home.html')




@app.route('/')
def index():
    return render_template('login.html')

@app.route("/logout")
def logout():
    User.logout()



# @app.route('/accept', methods=['GET'])
# def accept():
#     return render_template('accept.html')
