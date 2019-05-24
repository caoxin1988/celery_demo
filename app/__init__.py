"""
  Created by Cao,Xin on 2019-05-23 09:48
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-


from flask import Flask
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()


socketio = SocketIO()
# socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    socketio.init_app(app, message_queue='redis://localhost:6379/1')

    return app


app = create_app()


from . import views
from . import demo2_view
