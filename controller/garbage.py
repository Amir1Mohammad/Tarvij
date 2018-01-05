#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# project import:
from controller import ALLOWED_EXTENSIONS

__Author__ = "Amir Mohammad"


def create_user_id():
    from random import randint
    ic = randint(1000, 9999)
    return ic


def create_log_id():
    from random import randint
    ic = randint(1000, 9999)
    return ic


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS