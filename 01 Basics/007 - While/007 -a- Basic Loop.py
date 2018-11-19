# -*- coding: utf-8 -*-

"""
" While LOOP ""

https://docs.python.org/2/reference/compound_stmts.html#grammar-token-for_stmt


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

