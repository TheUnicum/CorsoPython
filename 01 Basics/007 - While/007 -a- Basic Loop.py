# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   While LOOP    -

https://docs.python.org/2/reference/compound_stmts.html

#Syntax Example:

#--------While -----------------CASE A--------------
while condition :
    indentedStatementBlock
#---------------------------------------------------

From python doc site
7.2. The while statement¶
The while statement is used for repeated execution as long as an expression is true:

while_stmt ::=  "while" expression ":" suite
                ["else" ":" suite]

"""

print
print '-'*40+'Example 1'
numero = 0
while numero <10:
	print numero
	numero += 1

# Must avoid infinite Loop
#while True:
#	print 'Hello'

print
print '-'*40+'Example 2'
str_ = ''
while len(str_) < 10:
	str_ = str_ + 'x'
	print str_
