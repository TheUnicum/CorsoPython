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

4.6. Defining Functions

--------------------------------------------CASE A--------------
def function_name(arguments):
    indentedStatementBlock
    ...
    return (Resul)
------------------------------------------------------------------

Functions are repeatable statement of code

"""


from math import pi


def say_hello_world():
    print 'Hello World!'


def say_n_hello_world(n):  # parameter
    for x in range(n):
        print 'Hello World!'


def circle_area(radius):
    return pi * (radius ** 2)


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
    print       # \n after list


# Now call the function we just defined:
print '-' * 40
say_n_hello_world(3)

print '-' * 40
print circle_area(4)

print '-' * 40
fib(2000)

print '-' * 40
print fib
