#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports :
from controller import app


# project imports:
from models.macros import Mac
from models.handbook import Handbook


@app.route('/api/butt1')
# TODO first login then can get data
def show_one():
    pass


@app.route('/api/butt2')
# TODO first login then can get data
def show_two():
    pass
