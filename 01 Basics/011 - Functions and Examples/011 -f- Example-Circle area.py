#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   FUNCTIONs    -

Calculate the area of a circle with radius input by user

    ->  run on pront command    <-

Note : -1 to EXIT!

"""


from math import pi


def circle_area(radius):
    return pi * (radius ** 2)


while True:
    user_radius = input("Enter a radius: ")
    if user_radius < 0: break  # noqa
    print circle_area(user_radius)
