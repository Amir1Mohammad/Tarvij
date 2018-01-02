# -*- coding: utf-8 -*-


# imports
from datetime import datetime
from controller.extension import db

__author__ = 'Amir Mohammad'


class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.String(25), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_json(self, with_user=False):
        if with_user:
            _dict = self.to_json()
            _dict['user'] = self.user.to_json()
            return _dict
        return {
            'id': self.id,
            'action': self.action,
            'time': str(self.time)
        }
