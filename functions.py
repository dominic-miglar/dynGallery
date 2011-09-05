#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright 2011 by Dominic Miglar

# Funktion logToFile(filename, logmessage): Dient zur Erstellung des Logfiles
# Argumente:
#     * filename - In dieses File wird geloggt
#     * logmessage - Dieser Text wird an das Logfile angehaengt
def logToFile(filename, logmessage):
    myLog = open(filename, 'a')
    myLog.write(logmessage+'\n')
    myLog.close()
