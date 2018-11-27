# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   Basic type in Pyton    -

https://docs.python.org/2/tutorial/introduction.html

None        Nessuno o nullo, variabile che vale sempre 0 oppure False
boolean     Booleano : False/True oppure 0/1
integers    Interi positivi e negativi. Non esiste un particolare limite MAX, provare "print 56**5274"
floats      Numero frazionale con virgola.
strings     Stringhe o liste di caratteri. In python non esiste il tipo di variabile <char>

"""

num = 145635624

print
print 40*'-' + 'Esadecimali'
hex_ = 0x23        # Rappresentazione esadecimale = 35
print hex_, ' = 0x23'
hex_ = 0xFF
print hex_, ' = 0xFF'

print
print 40*'-' + 'binari'
num_binario = 0b1010
print 0b1010, ' = 0b1010'
num_binario = 0b011
print 0b011, ' = 0b011'

print
print 40*'-' + 'Esponente'
esponente = 1e2
print esponente, '= 1e2 = 10^2'
