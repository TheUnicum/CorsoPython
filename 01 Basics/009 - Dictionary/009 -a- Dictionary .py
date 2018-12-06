#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   DICTIONARY    -

https://www.tutorialspoint.com/python/python_dictionary.htm

del()                       Removes element of dictionary dict
clear()         / {}        Removes all elements of dictionary dict
items()                     Returns a list of dict's (key, value) tuple pairs
keys()                      Returns list of dictionary dict's keys
values()                    Returns list of dicti
update(dict2)               Adds dictionary dict2's key-values pairs to dict


has_key(key)    / in         #Returns true if key in dictionary dict, false otherwise
get(key, default=None)

"""  # noqa


lista = [4139, 4127, 4098]
descrizione = 'Dipendente Parpas'
dizionario = {'Mattia': lista, 'Gabriele': descrizione, 'Steven': 4098}

print dizionario['Mattia']
print dizionario['Gabriele']

print
print 40 * '-' + 'items, keys, values'
print 'all dictionary ', dizionario
print 'items ', dizionario.items()
print 'keys  ', dizionario.keys()
print 'values', dizionario.values()

print
print 40 * '-' + 'DEL'
print dizionario
del dizionario['Mattia']
print dizionario

print
print 40 * '-' + 'Update'
print dizionario
dizionario.update({'Manuel': 123})
print dizionario

print
print 40 * '-' + 'has_key / in '
if dizionario.has_key('Manuel'):  # noqa
    print 'Exist'
if 'Manuel' in dizionario:
    print 'Exist'

print
print 40 * '-' + 'clear()'
dizionario.clear()
dizionario = {}
print dizionario
