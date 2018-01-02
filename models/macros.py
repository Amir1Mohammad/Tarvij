# -*- coding: utf-8 -*-


# imports
from datetime import datetime
from controller.extension import db

__author__ = 'Sepehr'


class Mac(db.Model):
    __tablename__ = 'macros'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    title = db.Column(db.Unicode(254), nullable=False)
    content = db.Column(db.Text, nullable=False)
