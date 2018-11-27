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

#--------While Break-Continue-ELSE-------CASE B--------------
while (condition expression):
    indentedStatementBlock
    break      ->  terminates the loop (without executing the else)
    continue   ->  skips the rest of the suite and goes back to testing the expression.
else:
    indentedStatementBlock at end of While loop if no 'Break'
#-----------------------------------------------------------

"""

print
print '-'*40+'Example 1'
i = 0
while i < 10 :
    i += 1
    print i
else:
    print 'Terminato senza errori'


print
print '-'*40+'Example 2'
i = 0
while i < 10 :
    i += 1
    if i == 5 :continue
    if i == 8 :break
    print i
else:
    print 'Terminato senza errori' #Non viene eseguito perche c'è il Break

print
print '-'*40+'Example 3'
caratteri = ''
while len(caratteri) <=10:
    #print caratteri

    #odd
    if (len(caratteri) % 2) ==0: print caratteri,'PARI'

    caratteri += 'X'
