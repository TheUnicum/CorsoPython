#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   IMPORTING MODULES    -

https://docs.python.org/2.7/library/index.html

"""

import math  # noqa
import random  # noqa
import string           # 7. String Services
import time  # noqa
import subprocess  # noqa
import threading  # noqa
import socket  # noqa
import Tkinter  # noqa
import sys  # noqa

'''
string.split(s[, sep[, maxsplit]])
string.strip(s[, chars])
string.zfill(s, width)
'''
testo = 'Testo di prova'
print string.split(testo)		# same testo.split()
print string.zfill(120, 5)      # write Nr:120 utilizzando almeno 5 cifre

print time.time()
