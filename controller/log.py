#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


from extension import db
from garbage import create_log_id
from models.log import Log

__Author__ = "Amir Mohammad"


def add_log(username, action):
    log_obj = Log(id=create_log_id(), username=username, action=action)
    db.session.add(log_obj)
    db.session.commit()