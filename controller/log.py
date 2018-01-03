#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# project imports :
from flask import jsonify
from extension import db
from models import User
from models.log import Log

__Author__ = "Amir Mohammad"



def add_log(username, action):
    user_obj = User.query.filter_by(username=username).first_or_404()
    log_obj = Log(user=user_obj, action=action)
    db.session.add(log_obj)
    db.session.commit()
    return jsonify(log_obj.to_json()), 200
