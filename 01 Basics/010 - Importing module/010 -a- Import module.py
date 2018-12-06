#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   IMPORTING MODULES    -

https://docs.python.org/2/tutorial/modules.html

Standard library
https://docs.python.org/2.7/library/index.html

importing       import 'namemodule'
from            from 'module' import 'namemodule'
as              import 'module' as 'Myname'
*               from math import *

"""


# Basic importing
import math
print 'math.pi           :', math.pi

# Import Simgle element
from math import pi  # noqa
print 'pi                :', pi

# Import Simgle element and rename
from math import pi as Pgreco  # noqa
print 'Pgreco            :', Pgreco

# Import all elements
from math import *  # noqa
print 'pi,e              :', pi, e
