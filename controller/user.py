#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__author__ = "Amir Mohammad"

# flask imports :
from flask import render_template, flash, request, redirect, url_for, abort

# project imports :
from controller import app


@app.route('/login', methods=['POST'])
def login():
    pass


def logout():
    pass

# @app.route('/accept', methods=['GET'])
# def accept():
#     return render_template('accept.html')
