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

4.7.3. Arbitrary Argument Lists
Finally, the least frequently used option is to specify that a function can be called
with an arbitrary number of arguments. These arguments will be wrapped up in a tuple
(see Tuples and Sequences).
Before the variable number of arguments, zero or more normal arguments may occur.

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

"""  # noqa


def sum_2_numbers(n1, n2):
    return n1 + n2


def sum_3_numbers(n1, n2, n3):
    return n1 + n2 + n3


print 20 * '-', 'sum_2_numbers & sum_3_numbers'
print sum_2_numbers(2, 4)
print sum_3_numbers(2, 4, 6)


def sum_n_numbers_temp(*numbers):
    print numbers                       # *args return a tuple of arguments!!!!


print 20 * '-', 'sum_n_numbers_temp'
sum_n_numbers_temp(2, 4, 5, 2, 54, 3, 3)
sum_n_numbers_temp(2, 40, 5, 3)


def sum_n_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print 20 * '-', 'sum_n_numbers(*numbers)'
print sum_n_numbers(2, 4, 5, 2, 54, 3, 3)
print sum_n_numbers(54, 3)


def add_numbers(str_, *args):
    total = 0
    for num in args: total += num  # noqa
    print str_, total


print 20 * '-', 'add_numbers(str_,  *args)'
add_numbers('I am about to add all numbers :', 3, 4, 6, 3, 6, 8)
add_numbers('I am about to add all numbers :', 3)
