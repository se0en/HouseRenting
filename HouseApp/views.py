# -*- encoding=UTF-8 -*-

from HouseApp import app

@app.route('/')
def index():
    return 'Hello'