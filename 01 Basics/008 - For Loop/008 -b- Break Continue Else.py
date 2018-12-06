#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   For LOOP    -

https://docs.python.org/2/reference/compound_stmts.html

#Syntax Example:

#--------FOR -----------------CASE B--------------
"for" target_list "in" expression_list:
    indentedStatementBlock
    break      ->  terminates the loop (without executing the else)
    continue   ->  skips the rest of the suite and goes back to next element.
else:
    indentedStatementBlock at end of FOR loop if no 'Break'
#---------------------------------------------------

From python doc site
7.3. The for statement
The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object:

for_stmt ::=  "for" target_list "in" expression_list ":" suite
              ["else" ":" suite]

""" # noqa

print '-' * 40 + 'Example 1'
for x in range(10):
    print x
else:
    print 'Terminato senza errori'


print
print '-' * 40 + 'Example 2'
for x in range(10):
    if x == 5: break  # noqa
    print x
else:
    print 'Terminato senza errori'


print
print '-' * 40 + 'Example 3'
for x in range(10):
    if x in (3, 6, 9): continue  # noqa
    print x
else:
    print 'Terminato senza errori'
