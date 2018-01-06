# -*- coding: utf-8 -*-


# imports
from datetime import datetime
from controller.extension import db

__author__ = 'Sepehr'


class Mac(db.Model):
    __tablename__ = 'macros'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    title1 = db.Column(db.Unicode(254), nullable=False)
    title2 = db.Column(db.Unicode(254), nullable=True)
    title3 = db.Column(db.Unicode(254), nullable=True)
    title4 = db.Column(db.Unicode(254), nullable=True)
    title5 = db.Column(db.Unicode(254), nullable=True)
    content = db.Column(db.Text, nullable=False)
    pic1 = db.Column(db.String(36), nullable=True)
    pic2 = db.Column(db.String(36), nullable=True)
