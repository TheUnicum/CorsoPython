#-*- coding: utf-8 -*-

"""
Docs
https://docs.python.org/2.7/library/index.html

"""


import math
import random
import string		#7. String Services
import time
import subprocess
import threading
import socket
import Tkinter
import sys

'''
string.split(s[, sep[, maxsplit]])
string.strip(s[, chars])
string.zfill(s, width)
'''
testo = 'Testo di prova'
print string.split(testo)		# same testo.split()
print string.zfill(120, 5)      # write Nr:120 utilizzando almeno 5 cifre


print time.time()
