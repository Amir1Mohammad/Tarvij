#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# flask import :
from flask import render_template

# project import :
from controller import app


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404