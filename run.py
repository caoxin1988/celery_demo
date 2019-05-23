"""
  Created by Cao,Xin on 2019-05-23 10:03
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import app


if __name__ == '__main__':
    app.run()



# gunicorn --worker-class eventlet -w 1 app:app
