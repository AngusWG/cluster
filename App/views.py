#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/18 0018 17:17
# @author  : zza
# @Email   : 740713651@qq.com
# from App import db
from flask import Blueprint, render_template

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def hello_world():
    return render_template('index.html')


@user_blueprint.route('/base')
def creat_db():
    return render_template('base.html')
