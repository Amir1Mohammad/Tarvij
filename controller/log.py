#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"


# project import :
from controller import app
from models.log import Log
from controller.extension import db
