#-*- coding: utf-8 -*-

"""
raw_input, input


https://docs.python.org/2/library/stdtypes.html

input(proint)   <-[IS EQUIVALENT TO]->  eval(raw_input(prompt)).

"""


print
print '-'*40
print 'raw_input, input - : USER INPUT'

user_input = raw_input("Scivi qualcosa: ")
print 'user input is <%s>' % user_input

user_input = input("Scivi qualcosa che puo essere validato con 'eval' (es: 5 + 7): ")
print 'user input is <%s>' % user_input