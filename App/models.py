#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/18 0018 16:01
# @author  : zza
# @Email   : 740713651@qq.com

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from App import db


class User(db.Model):
    """
    用户类
    """
    __tablename__ = 'user'
    u_email = db.Column(db.String(64), primary_key=True, unique=True, comment="邮箱就是id，不可更换")
    u_name = db.Column(db.String(32), comment="昵称，不可更改")
    u_qq = db.Column(db.String(32), comment="QQ")
    u_weixin = db.Column(db.String(32), comment="微信")
    u_create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    u_family_id = db.Column(db.Integer, default=None, comment="所属的族群号")
    u_key_word_list = db.Column(db.String(128), comment="特征词")

    def __init__(self, name, email):
        self.u_email = email
        self.u_name = name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Family(db.Model):
    """
    用户关联的族群实例
    """
    __tablename__ = 'familyr'

    f_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="族群号")
    f_member_num = db.Column(db.Integer, default=0, comment="族群人数")
    f_create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    f_creator = db.Column(db.String(64), db.ForeignKey('user.u_email'), comment="族群的创建者的邮箱(id)")
    u_name = db.Column(db.String(32), db.ForeignKey('user.u_email'), comment="创建者昵称")

    def __init__(self, creator):
        self.f_creator = creator

    def save(self):
        db.session.add(self)
        db.session.commit()
