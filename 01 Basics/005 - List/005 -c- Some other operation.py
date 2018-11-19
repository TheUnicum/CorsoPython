#-*- coding: utf-8 -*-

"""
list , tuple, string

some other operation
split, replace, find, upper, lower, startswith, endwith

join

https://docs.python.org/2/library/stdtypes.html

"""

print
print '-'*40, 'List Vs string---Same slicing operations'
print [1,2,3,4,5,6]
print [1,2,3,4,5,6][2:5]
print [1,2,3,4,5,6][::-1]

print
print 'Hello World!'
print 'Hello \'World!\''
print 'Hello World!'[2:5]
print 'Hello World!'[::-1]


print
print '-'*40, 'SPLIT'
stringa = 'Questa e una frase qualsiasi'
print stringa
split_s = stringa.split()
print split_s

print
stringa = 'Questa-è-una-frase-qualsiasi'
print stringa, "[split '-']"
split_s_by_char = stringa.split('-')
print split_s_by_char

print
stringa = 'Questa è una frase qualsiasi'
print stringa, "[split 'a']"
split_s_by_char_A = stringa.split('a')
print split_s_by_char_A

print
stringa = 'Questa è una frase qualsiasi'
print stringa, "[split 'a è una frase qu']"
split_s_by_str = stringa.split('a è una frase qu')
print split_s_by_str


print
print '-'*40, 'REPLACE'
stringa = 'Questa è una frase qualsiasi'
print stringa
split_s = stringa.replace('Questa','XXXX')
print split_s


print
print '-'*40, 'FIND'
#          01234567890123
stringa = 'Questa e una frase qualsiasi'
print stringa
index = stringa.find('frase')  #il primo trovato
print index
index = stringa.find('a caso')
print index


print
print '-'*40, 'upper & lower'
stringa = 'Questa è una frase qualsiasi'
print stringa
split_all_Maiuscola = stringa.upper()
print split_all_Maiuscola
split_all_minuscola = stringa.lower()
print split_all_minuscola


print
print '-'*40, 'startswith, endwith'
stringa = 'Questa è una frase qualsiasi'
print stringa
print 'La frase comincia con i caratteri "Ques"?, la risposta è', stringa.startswith('Ques')
print 'La frase termina con "qualsiasi"' , stringa.endswith('qualsiasi')
print 'La frase non termina con "fine"' , stringa.endswith('fine')


print
print '-'*40, 'JOIN'
lista = ['computer', 'mouse', 'tastiera', 'monitor']
print lista
print ''.join(lista)
print ' '.join(lista)
print '-'.join(lista)