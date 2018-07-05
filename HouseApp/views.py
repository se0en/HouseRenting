# -*- encoding=UTF-8 -*-

from HouseApp import app
from flask import render_template, request, flash, get_flashed_messages, redirect
from flask_login import login_user, logout_user, current_user, login_required
from models import User


@app.route('/', methods={'post', 'get'})
def index():
    if request.method == 'get':
        return render_template('index.html')


def redirect_with_msg(target, msg, category):
    if msg != None:
        flash(msg, category=category)
    return redirect(target)


@app.route('/reg/', methods={'post', 'get'})
def reg():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    repeat_password = request.values.get('repeat_password').strip()
    email = request.values.get('email').strip()

    if username == '' or password == '' or repeat_password == '' or email == '':
        return redirect_with_msg('regloginpage', u'不能为空', 'reglogin')
    
    user = User.query.filter_by(username=username).first()
    if user != None:
        redirect_with_msg('/regloginpage/', u'用户名已经存在', 'reglogin')
