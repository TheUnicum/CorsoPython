#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   COLORED ERRORS    -

"""

import sys

#colored errors
#only in python shell

sys.stderr.write("This is stderr text\n")
sys.stderr.flush()

sys.stdout.write("This is stdout text\n")
