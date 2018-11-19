#-*- coding: utf-8 -*-

"""
len , lunghezza della lista


list_operation
SLICING   Example lista [1:4:6]
TUPLE = liste non modificabili   , sintassi = in parentesi tonde()

"""

a = [1,2,3]
b = [11,22,33]
c = [44]
d = ['|']
e ='|'

c= a + b
print c
a.extend(b)
print a

print
print b, " * 4"
print b * 4

print
print d
print d * 4
print e * 4

print
print '-'*40 , 'SLICES'

lista = [11,22,33,44,55,66,77,88,99]

print lista[3]
print lista[3:4]

print lista[3:6]
print '[3:999999] Still Works',lista[3:999999]
print '[3:len(lista)]        ',lista[3:len(lista)]
print '[3:] Metodo corretto  ',lista[3:len(lista)]
print lista[-1]
print lista[-2]
print lista[-3:-1]
print lista[+1:-2], '[+1:-2] '

print lista[:],'tutta la lista'


print
print 'Even'
print lista[::2]

print
print 'odd'
print lista[1::2]

print
print 'reverse'
print lista[::-1]


print
print '-'*40 , 'List Vs Tupla'
lista = [1,2,3]
tupla = (1,2,3)

print lista, type(lista)
print tupla, type(tupla)

lista[2]= 33
#tupla[2]= 33   #non puo essere cambiata
print lista