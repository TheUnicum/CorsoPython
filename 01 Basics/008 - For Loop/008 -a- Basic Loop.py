#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   For LOOP    -

https://docs.python.org/2/reference/compound_stmts.html

#Syntax Example:

#--------FOR -----------------CASE A--------------
"for" target_list "in" expression_list:
    indentedStatementBlock
#---------------------------------------------------

From python doc site
7.3. The for statement
The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object:

for_stmt ::=  "for" target_list "in" expression_list ":" suite
              ["else" ":" suite]

"""

lista_stagioni = ['inverno', 'primavera', 'estate' , 'autunno']
lista_num_range = [0, 11, 2, 32, 4, 5, 62, 7, 8, 9]

print
print '-'*40+'Example 1'
for target_list in lista_stagioni:
    print target_list

print
print '-'*40+'Example 2'
for num in lista_num_range:
    print num


print
print '-'*40+'Example 3'
for char in 'For loop is looping also in strings, cause strings are sequesnces':
    print char
    if char == 's': break

import math
print
print '-'*40+'Example 4'
for char in str(math.pi): #3.14159....
    print char
    if char == 's': break
