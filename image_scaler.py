#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright 2011 by Dominic Miglar

# Skaliert die Bilder im picDir (damit Sie auch auf kleineren Bildschirmen schoen in
# der LightBox angezeigt werden.

from pictureget import getit
from functions import logToFile
from config import logFile, pictureDir, PICsize

import os
import Image

def img_scaler():
    logToFile(logFile, 'image_scaler\timage_scaler 0.1a started')
    imgList = getit(pictureDir)
    for img in imgList:
        pic = Image.open(pictureDir+'/'+img)
        width, height = pic.size
        if width > PICsize[0] or height > PICsize[1]:
            logToFile(logFile, '\nimage_scaler\twidth, height: '+str(width)+' '+str(height))
            logToFile(logFile, 'image_scaler\tSCALING IMAGE: '+pictureDir+'/'+img)
            pic.thumbnail(PICsize, Image.ANTIALIAS)
            pic.save(pictureDir+'/'+img)
