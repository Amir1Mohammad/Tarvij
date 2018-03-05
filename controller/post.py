#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python imports :
import os

# flask imports :
from flask import request, abort, render_template
from werkzeug.utils import secure_filename

# project imports :
from controller import db, app
from models.user import User
from models.handbook import HandBook
from models.macros import Mac
from controller.log import add_log
from garbage import allowed_file


@app.route('/matlab', methods=['POST', 'GET'])
def submit1():
    if request.method == 'GET':
        if User.logged_in_user() is None:
            abort(403)
        else:
            return render_template("enter_data.html")

    elif request.method == 'POST':
        title1 = request.form['title1']
        title2 = request.form['title2']
        title3 = request.form['title3']
        title4 = request.form['title4']
        title5 = request.form['title5']
        contetnt = request.form['content']

        macro_obj = Mac(username=User.logged_in_user(), title1=title1, title2=title2, title3=title3,
                        title4=title4, title5=title5, content=contetnt)

        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            filename = secure_filename(str(title1) + '__' + str(User.logged_in_user()))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if title1.strip() != '' and contetnt.strip() != '':
        db.session.add(macro_obj)
        db.session.commit()
        # user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
        add_log(User.logged_in_user(), "Adding data with form 1")
        # TODO . show accept page and add back to enter data.
        # return jsonify(user_obj.to_json()), 200
        return render_template('accept.html'), 200
    else:
        return '''
        The data is not valid . please check it again ...
        '''


@app.route('/handbook', methods=['POST', 'GET'])
def submit2():
    book = request.form['book']
    handbook_obj = HandBook(username=User.logged_in_user(), handbook=book)
    db.session.add(handbook_obj)
    db.session.commit()
    # user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
    add_log(User.logged_in_user(), "Adding data with form 4")
    return render_template('accept.html'), 200
    # return jsonify(user_obj.to_json()), 200


@app.route('/editing', methods=['POST', 'GET'])
def editing():
    if request.method == "GET":
        if User.logged_in_user() is None:
            abort(403)
    elif request.method == "POST":
        ser = User.logged_in_user()
        title_obj = Mac.query.filter_by(username=ser).all()
        # for tit in title_obj:
        #     print tit.title1
        return render_template('editing.html', title_obj=title_obj)


@app.route('/dele', methods=['POST', 'GET'])
def del_title():
    numberis = request.form['delete']
    if numberis:
        Mac.query.filter_by(id=numberis).delete()
        return '''<h2>
        Deleted Title Done.
        </h2>'''
    else:
        return '''<h1>
                Deleted Title Failed !!!
                </h1>'''

