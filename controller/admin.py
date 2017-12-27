#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python imports:

# project import :
from controller import app
from models.user import User

from controller.extension import db


@app.route('/register', methods=['POST'])
def add_admin(username, password, firstname, lastname, gender, phones, brand, category):
    pass


@app.route('/delete', methods=['POST'])
def delete_admin(username):
    pass
