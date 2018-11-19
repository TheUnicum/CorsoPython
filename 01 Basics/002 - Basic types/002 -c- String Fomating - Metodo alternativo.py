# -*- coding: utf-8 -*-


# Basic type in Pyton
"""
https://docs.python.org/2/library/string.html
"""

val_stringa = 'Testo di prova'
val_num = 1221

print "\n" + "-" * 40
print 'Metodo "classico python Heidenhain"'
print 'La striga vale = %s , mentre il numero vale = %d' % (val_stringa, val_num)

print "\n" + "-" * 40
print 'METODO ALTERNATIVO CON ".format"'
print "consiglio di utilizzare questo modo che risulta essere molto piu dinamico e parametrizzabile"
print
print 'La striga vale = {} , mentre il numero vale = {}'.format(val_stringa, val_num)
print 'La striga vale = {0} , mentre il numero vale = {1}'.format(val_stringa, val_num)
print 'La striga vale = {1} , mentre il numero vale = {0}'.format(val_stringa, val_num)


print "\n" + "-" * 40
print "Formatting float digits:"
a=13.946324
print("{0:.2f}".format(a))
print("{0:.2f}".format(round(a,2)))
print("{0:.15f}".format(round(a,2)))
print("{0:8.2f}".format(a))             #<--- IMPORTANT FORMAT


print "\n" + "-" * 40
print "altri esempi..."
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print '{:%Y-%m-%d %H:%M:%S}'.format(d)


octets = [192, 168, 0, 1]
print '{:02X}{:02X}{:02X}{:02X}'.format(*octets)