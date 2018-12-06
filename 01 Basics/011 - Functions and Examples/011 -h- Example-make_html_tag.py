#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   FUNCTIONs    -

    ->      make html tag        <-

"""


def make_html_tag(text, tag):
    return '<%s>%s</%s>' % (tag, text, tag)


print make_html_tag('il mio testo per il titolo', 'title')
print make_html_tag('riga in grossetto', 'bold')
