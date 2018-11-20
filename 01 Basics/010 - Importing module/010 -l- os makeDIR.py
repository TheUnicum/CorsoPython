#-*- coding: utf-8 -*-

"""
Docs
https://docs.python.org/2.7/library/index.html


get current OS Directory

make new directory name "Nuova_Directory"
rename "Nuova_Directory" to "NuovaBalubba"
remove "NuovaBalubba"

"""


import os
import time

curDir = os.getcwd()
print curDir

os.mkdir('Nuova_Directory')

time.sleep(2)

os.rename('Nuova_Directory','NuovaBalubba')
time.sleep(2)
os.rmdir('NuovaBalubba')