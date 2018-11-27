# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   Data Structures    -    raw_input  / input

https://docs.python.org/2/library/functions.html
https://docs.python.org/2/library/stdtypes.html

List/tuple/string some other operations:

-raw_input  reads a line from input, converts it to a string (stripping a trailing newline), and returns that
-input      Equivalent to eval(raw_input(prompt)).newline

input(proint)   <-[IS EQUIVALENT TO]->  eval(raw_input(prompt)).

"""

print
print '-'*40
print 'raw_input, input - : USER INPUT'
print "[Nota: questo script funziona solo in cmd.exe]\n"

user_input = raw_input("Scrivi qualcosa: ")
print 'user input is <%s>' % user_input

user_input = input("Prova a scrivere qualcosa che possa essere validato con 'eval' (es: 5 + 7): ")
print 'user input is <%s>' % user_input
