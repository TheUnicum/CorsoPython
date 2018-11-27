# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   FUNCTIONs    -

Recursion!!!!

Functions calling itself until reach the BASE CASE!

"""


#------------------------------------------------------------------
def double(x):
    return x*2

def double_recur(x):
    if x == 0 : return 0
    return double_recur(x-1) +2

print '-'*20,'double'
print double(4), double_recur(4)

#------------------------------------------------------------------
# triangle number
#1,3,6,10,15,21

# n = 1 	1
# n = 2 	3
# n = 3 	6
# n = 4 	10
# n = 5 	15
# n = 6 	21

def triangle_number(x):
	if x == 0 : return 0
	return triangle_number(x-1) +x
print
print '-'*20,'triangle number'
for x in range(0,10):
    print x, triangle_number(x)

#------------------------------------------------------------------
# sum digit
# 2621   -> 11
# 111221 ->8

def sum_digit(n):
    if n == 0 : return 0
    return sum_digit(n/10) + n%10

print
print '-'*20,'sum digit'
n = 2621
print n, sum_digit(n)
n = 111221
print n, sum_digit(111221)

#------------------------------------------------------------------
# yyyxxyy -> 2
# yxxxyxy -> 4

def count_x(str_):
    if str_ == '': return 0
    if str_.startswith('x') :
        return count_x(str_[1:]) + 1
    else:
        return count_x(str_[1:])

def count_x_v2(str_):
    if not str_: return 0
    return count_x_v2(str_[1:]) + str_.startswith('x')

print
print '-'*20,'count x'
s = 'yyyxxyy'
print s, count_x(s), "Versione compatta v2: ", count_x_v2(s)
s = 'yxxxyxy'
print s, count_x(s), "Versione compatta v2: ", count_x_v2(s)

#------------------------------------------------------------------
# factorial
# n = 0! 	1
# n = 1! 	1
# n = 2! 	1 * 2
# n = 3! 	1 * 2 * 3
# n = 4! 	1 * 2 * 3 * 4
# n = 5! 	1 * 2 * 3 * 4 * 5
# n = 6! 	1 * 2 * 3 * 4 * *5 * 6

def factorial_NON_rec(x):
    if x == 0 : return 1
    total = 1
    for n in range(1,x+1):
        total *= n
    return total

def factorial(x):
    if x == 0 : return 1
    return factorial(x-1) * x

print
print '-'*20,'factorial'
for x in range(10):
    print x, factorial_NON_rec(x), factorial(x)

#------------------------------------------------------------------
# fibonacci
# n = 0     0
# n = 1     1
# n = 2     1
# n = 3     2
# n = 4     3
# n = 5     5
# n = 6     8

def fibonacci(x):
    if x in (0,1): return x
    return fibonacci(x-1) + fibonacci(x-2)

print
print '-'*20,'fibonacci'
for x in range(10):
    print x, fibonacci(x)
