#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python imports :
import os

# flask imports :
from flask import request, jsonify, flash, redirect
from werkzeug.utils import secure_filename


# project imports :
from controller import db, app
from models.user import User
from models.handbook import Handbook
from models.macros import Mac
from controller.log import add_log
from garbage import allowed_file


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


# fixme . if the name is same . not upload the second picture.
# TODO . set in the title content data.
# TODO set . only can send picture.
# TODO api for downloading the picture .
# fixme . repair the access level.
@app.route('/picture', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print "The Upload file is empty"
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print "The Upload file is empty"
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file'))
            return '''
            <h2>File uploaded Completely</h3>'''

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method="post" enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
