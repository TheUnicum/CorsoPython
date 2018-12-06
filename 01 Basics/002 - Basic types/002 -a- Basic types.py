#!/usr/local/bin/python
# -*- coding: utf-8 -*-
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

""" # noqa

Variabile_Nulla = None
Variabile_booleana_Vera = True
Variabile_booleana_Falsa = False
Variabile_numerica_intera = 25
Variabile_numerica_reale = 5.4
Variabile_stringa = 'venticinque'

# print ('La variabile numerica vale ' + Variabile_numerica_intera)
# Questo comando non puo essere eseguito
# Per visualizzare il valore devo trasformare l'intero 25 in una stringa '25'
print ('La variabile numerica vale :' + str(Variabile_numerica_intera))

#                      ->  Formatting strings  <-
# Composizione di stringe con gli operatori:
# %d    (decimale)
# %f    (float)
# %s    (string)
# è possibile comporre stringhe e numeri assieme piu facilemnte
print

# sintassi
testo_di_Esempio = "Testo qualsiasi con all'interno le chiavi speciali %%d %%f %%s \n\
%%d viene sostituito da un intero \n\
%%f viene sostituito da un float \n\
%%s viene sostituito da una stringa \n\
Al termine della stringa deve esseci la lista delle variabili da sostituire \
alle chiavi :  \
d1=%d, f2=%f, d3=%d, d4=%d, s5=%s" % (10, 1.5546, 30, 40, 'ULTIMO')
#                                    (d1,   f2  , d3 ,d4 ,   s5   )

testo_di_Esempio_2 = "NOTE:  \n\
%% è un carattere speciale come anche \n\
\\n è un carattere speciale e significa 'VAi a capo riga' \n\
Come è possibile vedere direttamente in questo testo, \
se ho bisogno di utilizzare questi caratteri speciali \n\
come semplici caratteri ASCII e non come comandi PYTHON  \
occorre digitare i caratteri 2 volte consecutivamente\n"

print testo_di_Esempio
print  # riga vuota
print testo_di_Esempio_2

print
print 'intero = %d,  float= %f,  stringa= %s'\
    % (Variabile_numerica_intera, Variabile_numerica_reale, Variabile_stringa)

print ('La "Variabile_booleana_Vera"   vale %s      ed è di tipo %s'
       % (Variabile_booleana_Vera, type(Variabile_booleana_Vera)))
print ('La \'Variabile_numerica_intera\' vale %d        ed è di tipo %s'
       % (Variabile_numerica_intera, type(Variabile_numerica_intera)))
print ('La "Variabile_numerica_reale" vale %f   ed è di tipo %s'
       % (Variabile_numerica_reale, type(Variabile_numerica_reale)))
print ('La "Variabile_numerica_reale" vale %4.2f       ed è di tipo %s'
       % (Variabile_numerica_reale, type(Variabile_numerica_reale)))
print ('La "Variabile_stringa" vale (%s)    ed è di tipo %s'
       % (Variabile_stringa, type(Variabile_stringa)))
print

print '7 + 3.4          =', 7 + 3.4
print 'int (7 + 3.4)    =', int(7 + 3.4)
print '10 / 3           =', 10 / 3, '                     ATTENZIONE operazioni tra variabili entrambe intere restituisce un intero '# noqa
print '10 / 3.0         =', 10 / 3.0, '         basta trasformarne almeno una in un float' # noqa
print '10.0 / 3         =', 10.0 / 3
print 'float (10/3)     =', (float(10 / 3)), '                   ATTENZIONE a non fare il "cast" della variabile sul risultato finale'# noqa
print 'float(10)  /3    =', (float(10) / 3)

print
print 'TRY' + (40 * '-')
try:
    print '3' + 4  # non puo essere eseguita
except:  # noqa
    pass
    print ("Sto eseguendo questa parte di codice ,\
        perche la precedente da errore : \
        print '3' + 4  #non puo essere eseguita")

print
print (40 * '-')
print "int('3') + 4     =", int('3') + 4
print "'3' + str(4)     =", '3' + str(4), 'Attenzione che con print sembra un intero ma è "34"'# noqa
