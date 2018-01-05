#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


__author__ = "Amir Mohammad"

# flask imports :
from flask import render_template, request, redirect, url_for, abort, jsonify, flash
from werkzeug.utils import secure_filename
import os

# project imports :
from controller import app
from garbage import allowed_file
from models.user import User
from models.macros import Mac
from models.handbook import Handbook
from controller.extension import db
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


@app.route('/picture', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method="post" action="/picture">
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
