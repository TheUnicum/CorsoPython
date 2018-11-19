#-*- coding: utf-8 -*-

"""
    -   DICTIONARY    -

del()                       Removes element of dictionary dict
clear()         / {}        Removes all elements of dictionary dict
items()                     Returns a list of dict's (key, value) tuple pairs
keys()                      Returns list of dictionary dict's keys
values()                    Returns list of dicti
update(dict2)               Adds dictionary dict2's key-values pairs to dict


has_key(key)    / in         #Returns true if key in dictionary dict, false otherwise
get(key, default=None)


https://www.tutorialspoint.com/python/python_dictionary.htm

"""

lista =[4139,4127, 4098 ]
descrizione = 'Dipendente Parpas'
dizionario	 = {'Mattia': lista, 'Gabriele': descrizione, 'Steven': 4098}

elemento = dizionario.get('Mattia', "DEFAULT_TEXT")
print elemento

elemento = dizionario.get('KK', "DEFAULT_TEXT")
print elemento
