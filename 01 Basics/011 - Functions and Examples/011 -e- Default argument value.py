#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   FUNCTIONs    -

Docs
https://docs.python.org/2/tutorial/controlflow.html#defining-functions

4.7.1. Default Argument Values
The most useful form is to specify a default value for one or more arguments.
This creates a function that can be called with fewer arguments than it is defined to allow.
For example:

"""  # noqa


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

# Only in pront cmd dos
# ask_ok('Press Yes or no, please!')


def address_book_No_default(name, gender, age, has_cell, has_pc):
    pass


def address_book_default(name, gender, age, has_cell=True, has_pc=True):
    pass


address_book_No_default('Claudio', 'M', 22, True, True)
try:
    address_book_No_default('Claudio', 'M', 22,)
except Exception as e:
    print "Exception Error: <{}>".format(e)
    print "-----address_book_No_default MUST be called with exactly 5 arguments-----\n"  # noqa


address_book_default('Claudio', 'M', 22)
address_book_default('Claudio', 'M', 22, has_pc=False)
