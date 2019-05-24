# Demo with flask, flask-socketio and celery
============================================

This repo contains the following examples:

* login with user name and get result with asynchronous task


## Startup
----------

* clone this repo
* create a virtualenv with 'pipenv' and install packages with:

```plain
> $ pipenv update
```
* Open a new terminal and start redis server in it
* Open another terminal and start celery worker in it with:

```plain
> $ celery worker -A celery:celery_app --loglevel=info
```
* Start the Flask application:

```plain
> $ python run.py
```
or
 
 ```plain
> $ gunicorn --worker-class eventlet -w 1 app:app
 ```
the second way is recommended

* Go to `http://localhost:5000`(the first way) or `http://localhost:8000`(the later way) and try
the application



