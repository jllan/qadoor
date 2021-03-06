# encoding: utf-8

from flask import Blueprint, request, current_app, redirect, url_for, jsonify
from .models import User
from sqlalchemy import or_
from ..dbs import db
from flask_login import login_user, logout_user, login_required, current_user

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/signup', methods=['POST'])
def user_signup():
    try:
        user_instance = User.query.filter(or_(User.name==request.form['name'],
                                              User.email==request.form['email'])
                                          ).first()
        if user_instance:
            return jsonify(status='error', info='该用户已存在')
        else:
            user_instance = User()
            user_instance.name = request.form['name']
            user_instance.email = request.form['email']
            user_instance.set_password(request.form['password'])
            db.session.add(user_instance)
            db.session.commit()
            return jsonify(status='success', info='创建成功')
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))

@user.route('/login', methods=['POST'])
def user_login():
    try:
        user_instance = User.query.filter(User.name==request.form['name']).first()
        if user_instance:
            print(request.form['name'])
            print(request.form['password'])
            if user_instance.verify_password(request.form['password']):
                login_user(user_instance)
        return redirect(url_for('qa.index'))
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))

@user.route('/logout', methods=['GET'])
@login_required
def user_logout():
    logout_user()
    return redirect(url_for('qa.index'))
