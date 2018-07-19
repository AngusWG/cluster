#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/18 0018 17:17
# @author  : zza
# @Email   : 740713651@qq.com
import os

from flask import Flask

# from App.models import db
from flask_sqlalchemy import SQLAlchemy

from App.views import user_blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
static_dir = os.path.join(BASE_DIR, 'static')
templates_dir = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__,
            static_folder=static_dir,
            template_folder=templates_dir)


def creat_app():
    app.register_blueprint(blueprint=user_blueprint, url_prefix='')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + '../data.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_ECHO'] = True

    # db.create_all()
    app.config['SECRET_KEY'] = 'secret_key'
    return app


#
creat_app()
db = SQLAlchemy(app)
from App.models import *

print("*" * 50)
db.create_all()
