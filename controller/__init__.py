from flask import Flask
import os
from controller.extension import db
from extension import login_manager

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'topsecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db.init_app(app)
# login_manager.init_app(app)
# login_manager.login_view = "login"


__Author__ = "Amir Mohammad"

from controller import log, user, admin, fof
