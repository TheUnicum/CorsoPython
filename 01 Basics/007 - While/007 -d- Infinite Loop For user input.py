# -*- coding: utf-8 -*-

'''
" While LOOP ""


#Syntax Example:

#--------While -----------------CASE A--------------
while (condition ALWAYS TRUE):
	indentedStatementBlock
	if conditionForExit:
		break
#---------------------------------------------------

'''



while True:
    q = raw_input('Premi "q" per uscire : ')
    if q == 'q':
        break
    print "non e' stata premuto il taso 'q'"