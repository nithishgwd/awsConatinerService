@echo off
set FLASK_APP=subOverTime:app
gunicorn -w 4 -b 0.0.0.0:8000 -k gevent -t 120 subOverTime:app
