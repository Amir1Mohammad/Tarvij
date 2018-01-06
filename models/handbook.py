
# imports
from datetime import datetime
from controller.extension import db

__author__ = 'Sepehr'


class HandBook(db.Model):
    __tablename__ = 'handbook'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    handbook = db.Column(db.Text, nullable=False)
