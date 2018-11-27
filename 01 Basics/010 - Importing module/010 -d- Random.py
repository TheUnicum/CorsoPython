#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   IMPORTING MODULES    -

    -        RANDOM          -
Docs
https://docs.python.org/2.7/library/random.html

#random.random()        Return the next random floating point number in the range [0.0, 1.0).
#random.randint(a, b)   Return a random integer N such that a <= N <= b.

"""


import random
print random.__all__
print

print random.random()
print random.randint(50,100)
