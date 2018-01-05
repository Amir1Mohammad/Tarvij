#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports :
from flask import jsonify, abort, send_file

# project imports:
from models.macros import Mac
from models.handbook import Handbook
from controller import app
from models.user import User


@app.route('/api/title/<string:username>', methods=['GET', 'POST'])
def see_mac(username):
    if User.logged_in_user() == "tecvest@1010":
        listme = []
        o = Mac.query.filter_by(username=username).all()
        for row in o:
            show = {
                'username': row.username,
                'title': row.title,
                'content': row.content,
            }

            listme.append(show)
        return jsonify(jsonify=listme), 200
    else:
        abort(403)


@app.route('/api/content/<string:username>', methods=['POST', 'GET'])
def show_two(username):
    if User.logged_in_user() == "tecvest@1010":
        listme = []
        o = Handbook.query.filter_by(username=username).all()
        for row in o:
            show = {
                'username': row.username,
                'handbook': row.handbook,
            }
            listme.append(show)
        return jsonify(jsonify=listme), 200
    else:
        abort(403)


# @app.route('/file')
# def file_downloads():
#     try:
#         return render_template('down.html')
#     except Exception as e:
#         return str(e)


# @app.route('/shows')
# def return_files_tut():
#     try:
#         return send_file('test.png')
#     except Exception as e:
#         return str(e)
