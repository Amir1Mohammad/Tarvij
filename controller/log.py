#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;
from controller import app
from extension import db
from garbage import create_log_id
from models.log import Log

__Author__ = "Amir Mohammad"


@app.route("/<string:username>/<string:action>")
def add_log(username, action):
    log_obj = Log(username=username, action=action)
    db.session.add(log_obj)
    db.session.commit()
    return "", 200


    # add_log("amir","login")
