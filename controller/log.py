#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"


# project import :
from controller import app
from models.log import Log
from controller.extension import db
from controller.garbage import create_log_id


# fixme like admin
# @app.route('/logfile',methods=['GET'])
def add_log(username, action):
    log_obj = Log(id=create_log_id(), username=username, action=action)
    db.session.add(log_obj)
    db.session.commit()

add_log('amir','shal')