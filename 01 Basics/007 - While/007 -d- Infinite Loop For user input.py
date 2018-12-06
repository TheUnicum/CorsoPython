#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   While LOOP    -

https://docs.python.org/2/reference/compound_stmts.html

#Syntax Example:

#--------While -----------------CASE A--------------
while (condition ALWAYS TRUE):
    indentedStatementBlock
    if conditionForExit:
        break
#---------------------------------------------------

"""

print "[Nota: questo script funziona solo in cmd.exe]\n"
while True:
    q = raw_input('Premi "q" per uscire : ')
    if q == 'q':
        break
    print "non e' stata premuto il taso 'q'"
