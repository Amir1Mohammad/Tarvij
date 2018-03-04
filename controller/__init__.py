from flask import Flask
import os
from controller.extension import db

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'topsecret'
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = '/home/cloner/Desktop/Tarvij/static/picture'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['JSON_AS_ASCII'] = False
db.init_app(app)

__Author__ = "Amir Mohammad"

from controller import log, user, admin, fof, api, post, admin2
