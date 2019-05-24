"""
  Created by Cao,Xin on 2019-05-23 10:01
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import app, socketio
from flask_socketio import SocketIO, join_room
from app.celery import celery_app
from flask import render_template, request, url_for, redirect, session, jsonify
import time
import random


@app.route('/')
def index():
    if 'id' in session:
        name = session['id']
        return render_template('index.html', name=name)
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('id')
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    """
    /run_task url view function
    """
    name = request.form.get('emit_name', None)
    if name:
        session['id'] = name

    #add.delay(session['id'])
    return render_template('index.html', name=name)


@celery_app.task
def add(room):
    print('room = {}'.format(room))
    for i in range(1, 5):
        print('random int :', i)
        time.sleep(1)

    import eventlet; eventlet.monkey_patch()
    socket = SocketIO(message_queue='redis://localhost:6379/1')
    val = random.randint(1, 100)
    socket.emit('test_message', {'data': val}, namespace='/test_conn', room=room)


@socketio.on('connect', namespace='/test_conn')
def test_connect():
    pass


@socketio.on('join_room', namespace='/test_conn')
def joinroom(msg):
    print('join_room', session['id'])
    join_room(session['id'])

    add.delay(session['id'])

