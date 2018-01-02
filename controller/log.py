#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;
from flask import jsonify

from controller import app
from extension import db
from garbage import create_log_id
from models import User
from models.log import Log

__Author__ = "Amir Mohammad"


# @app.route("/<string:username>/<string:action>")
def add_log(username, action):
    user_obj = User.query.filter_by(username=username).first_or_404()
    log_obj = Log(user=user_obj, action=action)
    db.session.add(log_obj)
    db.session.commit()
    return jsonify(log_obj.to_json()), 200


    # add_log("amir","login")
