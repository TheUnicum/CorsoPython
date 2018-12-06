#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   IMPORTING MODULES    -

https://docs.python.org/2/library/functions.html#dir

dir([object])
Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

__name__
__doc__
__all__         all user function

"""  # noqa


import math
print dir(math)
print
print math.__name__
print
print math.__doc__

print
import random  # noqa
print random.__all__
