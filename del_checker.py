#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# del_checker.py

# Copyright 2011 by Dominic Miglar

import os
from functions import logToFile
from pictureget import getit
from config import pictureDir, THUMBpictureDir, logFile

# Funktion: del_checker()
# Überprüft, ob es alle Thumbs auch als grosses Bild gibt, ist dies nicht der Fall 
# (grosses Bild wurde gelöscht), dann wird ebenfalls das entsprechende Thumbnail gelöscht.
#
def del_checker():
    logToFile(logFile, 'del_checker\tdel_checker 0.1a started..')
    thumb_list = getit(THUMBpictureDir)
    for thumb in thumb_list:
        if not os.access(pictureDir+'/'+thumb, os.F_OK):
            logToFile(logFile, 'del_checker:\tDEL FILE '+THUMBpictureDir+'/'+thumb+' !')
            os.remove(THUMBpictureDir+'/'+thumb)
