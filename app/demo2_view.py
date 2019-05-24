"""
  Created by Cao,Xin on 2019-05-24 14:50
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import app, socketio
from flask import (
    render_template,
    session,
    jsonify
)


@app.route('/demo2_view')
def demo2_view():
    name = session.get('id', None)

    return render_template('demo2.html', name=name)


@socketio.on('connect', namespace='/test_conn')
def connect():
    print('demo2 view connect')


@app.route('/longtask')
def longtask():
    print('get a long task')
    return jsonify({'data': '123'})

