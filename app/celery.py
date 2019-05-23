"""
  Created by Cao,Xin on 2019-05-23 10:51
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from celery import Celery
import time

celery_app = Celery('demo')

celery_app.config_from_object('app.celery_config')


