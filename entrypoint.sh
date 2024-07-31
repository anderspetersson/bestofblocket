#!/bin/bash
gunicorn bestofblocket.conf.wsgi:application
nginx -g 'daemon off;'
