#!/bin/bash
cd src
gunicorn -w 4 -k gevent --bind 0.0.0.0:5000 wsgi:app