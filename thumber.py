#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright 2011 by Dominic Miglar

import os
from functions import logToFile
from PIL import Image
from pictureget import getit
from config import logFile, pictureDir, THUMBpictureDir, THUMBsize

# Funktion: thumber - erstellt Thumbnails
#	Die Thumbnails heissen genau so, wie die originalen Dateien, befinden sich aber in einem eigenen Thumbnailordner.
# 
def thumber():
    if not os.access(THUMBpictureDir, os.F_OK):
        logToFile(logFile, 'thumber:\t\tERROR (thumber): Der Pfad '+THUMBpictureDir+' existiert nicht!')
        return
    if not os.access(THUMBpictureDir, os.X_OK):
        logToFile(logFile, 'thumber:\t\tERROR (thumber): Auf den Pfad '+THUMBpictureDir+' kann nich zugegriffen werden!')
        return
    if not os.access(THUMBpictureDir, os.R_OK):
        logToFile(logFile, 'thumber:\t\tERROR (thumber): Vom Pfad '+THUMBpictureDir+' kann nicht gelesen werden!')
        return
	
	logToFile(logFile, 'thumber:\t\tthumber 0.1a started...')
    ori_piclist = getit(pictureDir)
    for pic in ori_piclist:
        if not os.access(THUMBpictureDir+'/'+pic, os.F_OK):
            logToFile(logFile, 'thumber:\t\tCREATING THUMB for '+pic)
            im = Image.open(pictureDir+'/'+pic)
            im.thumbnail(THUMBsize, Image.ANTIALIAS)
            im.save(THUMBpictureDir+'/'+pic)
