#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python imports :
import os

# flask imports :
from flask import request, jsonify, abort, render_template
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

        macro_obj = Mac(username=User.logged_in_user(), title1=title1,title2=title2,title3=title3,
                        title4=title4, title5=title5, content=contetnt)

        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            filename = secure_filename(str(title1)+'__'+str(User.logged_in_user()))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if title1.strip() != '' and contetnt.strip() != '':
        db.session.add(macro_obj)
        db.session.commit()
        # user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
        add_log(User.logged_in_user(), "Adding data with form 1")
        # TODO . show accept page and add back to enter data.
        # return jsonify(user_obj.to_json()), 200
        return render_template('accept.html'),200
    else:
        return '''
        The data is not valid . please check it again ...
        '''


@app.route('/handbook', methods=['POST', 'GET'])
def submit2():
    book = request.form['book']
    handbook_obj = HandBook(username=User.logged_in_user(), handBook=book)
    db.session.add(handbook_obj)
    db.session.commit()
    user_obj = User.query.filter_by(username=User.logged_in_user()).first_or_404()
    add_log(User.logged_in_user(), "Adding data with form 4")
    return jsonify(user_obj.to_json()), 200






'''
fixme . if the name is same . not upload the second picture.
TODO . set in the title content data.
TODO set . only can send picture.
TODO api for downloading the picture .
fixme . repair the access level.
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
            # return '''
            # <h2>File uploaded Completely</h3>'''
    #
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method="post" enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''

