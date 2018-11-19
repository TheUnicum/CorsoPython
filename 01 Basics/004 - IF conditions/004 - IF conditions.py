# -*- coding: utf-8 -*-

"""
" If Statements ""

https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html


#Syntax Example:

#--------Simple if Statements-----------------CASE A--------------
if condition :
	indentedStatementBlock
#------------------------------------------------------------------



#--------if-else Statements--------------------CASE B--------------
if condition :
	indentedStatementBlockForTrueCondition
else:
	indentedStatementBlockForFalseCondition
#------------------------------------------------------------------



#--------if-elif-else Statements---------------CASE C--------------
if condition_1 :
	indentedStatementBlockForTrueCondition_1
elif condition_2 :
	indentedStatementBlockForTrueCondition_2
elif condition_3 :
	indentedStatementBlockForTrueCondition_3
....
else:
	indentedStatementBlockForFalseCondition
#------------------------------------------------------------------


Bool Conditional Expressions

#    and     or    not
"""


print '-'*40  + 'Bool Conditional Expressions'  # '-------------'
print True and True, ' <- True (and) True'
print True and False, ' <- True (and) False'
print False or True, ' <- False (or) True'
print not(True) , ' <- not(True)'


'''
[Bool Int Float]
More Conditional Expressions
Meaning					Math Symbol		Python Symbols

Less than					<					<
Greater than				>					>
Less than or equal			≤					<=
Greater than or equal		≥					>=
Equals						=					==
Not equal					≠					!=

'''

print '-'*40  + 'More Conditional Expressions'  # '-------------'
print 'Il risultato di 2 > 6 vale :', 2 > 6
print 'Il risultato di 2 < 6 vale :', 2 < 6
print '2 != 3 :' ,2 != 3
print  'type(2) == type(45) :'  ,type(2) == type(45)
print  'type(2) == type(45.0):' ,type(2) == type(45.0)
print  '2 == 2.0:' ,2 == 2.0, '   NB!!!!! uguaglianza come valore delle variabili'
print  'type(2) == type(2.0):' ,type(2) == type(45.0), 'NB!!!!! uguaglianza come TIPO delle variabili'
print


'''
[string List]
Some  Conditional Expressions Examples  *for STRINGS and LIST*

in  /   not in
	item in sequence
	item not in sequence


len (lenth)

'''
print '-'*40  + 'Strings'  # '-------------'
if 's' in 'listacaratteri':
	print 's è in "listacaratteri" '

if 'z' in 'listacaratteri':
	print 'z è in "listacaratteri" '
else:
	print 'z |NON| è in "listacaratteri" '

if 'caratte' in 'listacaratteri':
	print "'caratte' è all'interno di 'listacaratteri'"





print
print
print '-'*40    # '----------------------------------------'
print '-'*15 , 'SOME IF EXAMPLE','-'*15
print '-'*40
numero  = 105
print 'Il numero introdotto è = %d ' % numero
print
if numero > 100:
	print 'Il numero introdotto è maggiore di 100'
else:
	print 'Il numero introdotto NON è maggiore di 100'

print
if numero == 111:
	print 'Il numero introdotto è 111'
elif numero == 222:
	print 'Il numero introdotto è 222'
elif numero == 333:
	print 'Il numero introdotto è 333'
else:
	print 'Il numero introdotto NON è uno di questi 111,222,333'




print
if numero > 100:
	print 'Il numero introdotto è maggiore di 100'
if numero > 200:
	print 'Il numero introdotto è maggiore anche di 200'
if numero > 300:
	print 'Il numero introdotto è maggiore anche di 300'

print
if numero >= 100:
	if numero <= 110:
		print 'Il numero introdotto è tra 100 e 110'


if numero >= 100 and numero <= 110:
		print 'Il numero introdotto è tra 100 e 110'


if 100 <= numero <= 110:
		print 'Il numero introdotto è tra 100 e 110'




