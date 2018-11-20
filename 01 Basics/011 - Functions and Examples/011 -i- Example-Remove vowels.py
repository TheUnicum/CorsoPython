#-*- coding: utf-8 -*-

"""

    ->      Remove vowels from strings      <-

"""


def remove_vowels(string):
		vowels = 'aeiou'
		new_string = ''

		for character in string:
			if character.lower() not in vowels:
				new_string += character

		return new_string

testo1 = 'Ciao io sono Mattia'
testo2 = 'Questo è la seconda stringa'

print remove_vowels(testo1)
print remove_vowels(testo2)