#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# pictureget.py

# Copyright 2011 by Dominic Miglar

import os
from functions import logToFile
from glob import glob
from config import logFile, pictureTypes


# Funktion: getit(logfile, picturedir, picturetype) - returnt eine Liste mit Pfaden
# Argumente:
#     * picturedir: In diesem Ordner soll die Funktion nach Bildern suchen (Bsp. /meine/bilder/sind/hier)
#
def getit(picturedir):
    # Prüfen, ob der Pfad existiert, ob man auf den Pfad zugreifen kann, und ob man den Pfad lesen kann
    # BEGIN Prüfen
    logToFile(logFile, 'getit:\t\tgetit 0.1a started...')
    if not os.access(picturedir, os.F_OK):
        logToFile(logFile, 'getit:\t\tERROR: Pfad '+picturedir+' existiert nicht!.')
        return
    if not os.access(picturedir, os.X_OK):
        logToFile(logFile, 'getit:\t\tERROR: Zugriff auf Pfad '+picturedir+' verweigert!')
        return           
    if not os.access(picturedir, os.R_OK):
        logToFile(logFile, 'getit:\t\tERROR: Pfad '+picturedir+' kann nicht gelesen werden!')
        return
    # END Prüfen
    
    picturelist = []
    for pictureType in pictureTypes:
        typelist = glob('./'+picturedir+'/*.'+pictureType)
        if len(typelist) != 0:
            picturelist.extend(typelist)

    # returnlist: Liste, die anschliessend zurueckgegeben wird.
    returnlist = []

    for picture in picturelist:
        head, tail = os.path.split(picture)
        returnlist.append(tail)
    return returnlist
