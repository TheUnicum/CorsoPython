# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   Data Structures    -    LIST !

https://docs.python.org/2/tutorial/datastructures.html

Python "built in function" utili per operazioni su liste

- <len()>         lunghezza della lista


List/string functions:

-append     Add an item to the end of the list; equivalent to a[len(a):] = [x].
-extend     Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
-insert     Insert an item at a given position
-remove     Remove the first item from the list whose value is x. It is an error if there is no such item.
-pop        Remove the item at the given position in the list, and return it
-index      Return the index in the list of the first item whose value is x. Error if there is no item.
-count      Return the number of times x appears in the list.
-sort       Sort the items of the list in place
-reverce    Reverse the elements of the list, in place.

"""

lista_num = [1,2,3,4,5,66,548,25625626265562]
#numerone = 25625626265562
#print numerone, type(numerone)


print lista_num, type(lista_num)
print 'la lunghezza della lista è %d' % len(lista_num)
print

lista_str = ['inverno', 'primavera', 'estate' , 'autunno']

print lista_str
print 'la lunghezza della lista è %d' % len(lista_str)
print

print lista_str[2]
print lista_str.index('estate')
print lista_str[lista_str.index('estate')]
print

print lista_str
lista_str[2] = 'nuovo valore'
print lista_str
lista_str.append('Stg-added-all-fine')
print lista_str
lista_nuova = ['Stg-added-all-inizio']
lista_nuova.extend(lista_str)
print lista_nuova
lista_nuova.insert(3,'Stg-added-al_index_3')
print lista_nuova
lista_nuova.remove('inverno')
#lista_nuova.remove('inesistente') non funziona
print lista_nuova


print
print '-------- POP -------------'
lista_num = [1,2,3,4,5,6,7,8,9,10]
print lista_num
lista_num.pop()
print lista_num
lista_num.pop()
print lista_num
ultimo_elemento =  lista_num.pop()
print lista_num, ultimo_elemento
ultimo_elemento =  lista_num.pop()
print lista_num, ultimo_elemento
ultimo_elemento =  lista_num.pop(-1)
print lista_num, ultimo_elemento
ultimo_elemento =  lista_num.pop(0)
print lista_num, ultimo_elemento
ultimo_elemento =  lista_num.pop(2)
print lista_num, ultimo_elemento


print
print '-------- COUNT -----------'
lista = [1,2,3,4,2,3,4,2,3,2]
print 'il 2 compare nella lista %d volte ' %lista.count(2)
print 'il 7 compare nella lista %d volte ' %lista.count(7)
lista.sort()
print lista
