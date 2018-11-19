#-*- coding: utf-8 -*-

"""

dict.keys()				iterate through keys
dict.values()			iterate through values
dict.items()			iterate through items


https://www.tutorialspoint.com/python/python_dictionary.htm

"""



lista =[4139,4127, 4098 ]
descrizione = 'Dipendente Parpas'
dizionario	 = {'Mattia': lista, 'Gabriele': descrizione, 'Steven': 4098}

print
print 40*'-'+'dict.keys()'
for key in dizionario.keys():
	print key# dizionario[key]

print
print 40*'-'+'dict.values()'
for key in dizionario.values():
	print key

print
print 40*'-'+'dict.items()'
for key in dizionario.items():
	print key