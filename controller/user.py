#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


__author__ = "Amir Mohammad"




# flask imports :
from flask import render_template

# project imports :
from controller import app


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


def log_out():
    pass


@app.route('/accept', methods=['GET'])
def accept():
    return render_template('accept.html')
