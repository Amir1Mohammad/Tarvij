#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports :
from flask import render_template, jsonify, request, abort, redirect

# project imports :
from models.user import User
from models.log import Log
from controller import app
from controller.extension import db

__Author__ = "Amir Mohammad"


def set_limit_log(min=3, max=50):
    row_count = Log.query.count()
    for i in range(2):
        if not min < row_count <= max:
            print "the member of log : ", row_count
            limit_log_person = Log.query.limit(2).all()
            me = limit_log_person[1]
            db.session.delete(me)
            db.session.commit()
        else:
            row_count = Log.query.count()
            print "the member of log : ", row_count


@app.route('/add_admin', methods=['POST', 'GET'])
def add_admin():
    if request.method == "GET":
        if User.logged_in_user() is None:
            abort(403)

    elif request.method == "POST":
        username = request.form['username']
        passwordhash = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        phones = request.form['phone']
        brand = request.form['brand']
        category = request.form['category']

        user_obj = User(username=username, passwordhash=passwordhash,
                        firstname=firstname, lastname=lastname, gender=gender, phones=phones,
                        brand=brand, category=category)

        db.session.add(user_obj)
        db.session.commit()
        return '''
                <script>
        function goBack() {
            window.history.back();
        }
        </script>
                Admin Added Successfully.
                <button onclick="goBack()">Go Back</button>
        ''', 200


@app.route('/login/delete/<username>')
def delete_admin(username):
    if User.logged_in_user() == "tecvest@1010":
        q = User.query.filter_by(username=username).first()
        print q
        if q is not None:
            User.query.filter_by(username=username).delete()
            return '''
            <h1>The User is Deleted</1>''', 200
        else:
            return '''<h1>The User not exist !</h1>'''
    else:
        abort(403)


@app.route('/log/<username>')
def show_log_name(username):
    user_obj = User.query.order_by(username=username).first_or_404()
    print user_obj.to_json()
    return jsonify(user_obj.to_json())
    # return render_template('show_user_name.html', log_obj_q=user_obj.to_json())


@app.route('/log', methods=['GET'])
def show_log_all():
    if User.logged_in_user() == "tecvest@1010":
        log_obj_q = Log.query.all()
        try:
            # set_limit_log()
            return render_template('show_user_date.html', log_obj_q=log_obj_q)
        except:
            return render_template('show_user_date.html')
    else:
        abort(403)


@app.route('/', methods=['GET', 'Post'])
def to_add_admin():
    if request.form['Work'] == 'add_admin':
        return render_template('add_admin.html')

    elif request.form['Work'] == 'view_logs':
        return redirect('log')
