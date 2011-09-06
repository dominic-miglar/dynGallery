#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# main.py

# Copyright 2011 by Dominic Miglar

from bottle import route, run, debug, static_file, redirect, request
from bottle import jinja2_template as template

import os

from pictureget import getit
from thumber import thumber
from functions import logToFile
from del_checker import del_checker
from image_scaler import img_scaler

from config import web_header, web_footer, web_title
from config import THUMBpictureDir, pictureDir, logFile


# Der Mainpath der Webseite 
# Wenn man den Inhalt '/' aufruft, wird man autom. auf diese Route verwiesen
mainpath = '/main'

@route('/')
def start():
    redirect(mainpath)

@route('/main')
def mainpage():
    logToFile(logFile, 'bottle:\t\tClient connecting from '+str(request['REMOTE_ADDR']))

    content = 'lorem ipsum blablablablabla'

    thumber()
    del_checker()
    img_scaler()

    thumbs = getit(THUMBpictureDir)    
    return template('child', mytitle=web_title, myheader=web_header, mycontent=content, myfooter=web_footer, thumbDir=THUMBpictureDir, picDir=pictureDir, thumbs=thumbs)

# STATIC ROUTES - BEGIN

@route('/styles/:style')
def static_style(style):
    return static_file(style, root='styles')

@route('/pictures/:picture')
def static_picture(picture):
    return static_file(picture, root='pictures')

@route('/pictures/thumbs/:thumb')
def static_thumb(thumb):
    return static_file(thumb, root='pictures/thumbs')

@route('/favicon.ico')
def favicon_static():
    return static_file('favicon.ico', root='static_stuff')

@route('/js/:path#.+#')
def js_static(path):
    return static_file(path, root='js')

# STATIC ROUTES - END

# Debug Mode 
debug(True)

# Servermuhbla
run(host="0.0.0.0", port=8080)
