#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   IMPORTING MODULES    -

https://docs.python.org/2.7/library/index.html

Description:

1.  get current OS Directory
2.  make new directory name "Nuova_Directory"
3.  rename "Nuova_Directory" to "NuovaBalubba"
4.  remove "NuovaBalubba"

"""


import os
import time

curDir = os.getcwd()
print curDir

os.mkdir('Nuova_Directory')

time.sleep(2)

os.rename('Nuova_Directory','CartellaRinominata')
time.sleep(2)
os.rmdir('CartellaRinominata')
