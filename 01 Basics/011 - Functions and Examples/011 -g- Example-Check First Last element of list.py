#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   FUNCTIONs    -

    ->      Check first and last elements of a list        <-

"""


def same_start_end_lists(list1, list2):
    starts_match = list1[0] == list2[0]
    ends_match = list1[-1] == list2[-1]
    return starts_match and ends_match


print same_start_end_lists('ciao', 'canguro')
print same_start_end_lists([46, 5, 78, 2, 4], [46, 7358, 4])
print same_start_end_lists('settembre', 'ottobre')
