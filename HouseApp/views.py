# -*- encoding=UTF-8 -*-

from HouseApp import app, db
from HouseApp.models import User
from flask import render_template, request, flash, get_flashed_messages, redirect
from flask_login import login_user, logout_user, current_user, login_required
import random, hashlib


@app.route('/', methods={'post', 'get'})
def index():
    msg = ''
    for m in get_flashed_messages(with_categories=False, category_filter=['reglogin']):
        msg  = msg + m
    return render_template('index.html', msg=msg)


def redirect_with_msg(target, msg, category):
    if msg is not None:
        flash(msg, category=category)
    return redirect(target)


@app.route('/reg/', methods={'post', 'get'})
def reg():
    # request.args
    # request.form
    username = request.values.get('user_sign').strip()
    password = request.values.get('pass_sign').strip()
    # repeat_password = request.values.get('pass_repeat').strip()
    email = request.values.get('email').strip()
    tel = 0

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return redirect_with_msg('/', u'用户名已经存在', 'reglogin')

    salt = '.'.join(random.sample('0123456789ABCdef', 10))
    m = hashlib.md5()
    m.update((password + salt).encode('utf8'))
    password = m.hexdigest()
    user = User(username, password, email, tel, salt)
    db.session.add(user)
    db.session.commit()

    return redirect('/')

