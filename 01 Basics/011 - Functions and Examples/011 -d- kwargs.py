#-*- coding: utf-8 -*-

"""
Docs
https://docs.python.org/2/tutorial/controlflow.html#defining-functions

4.7.3. Arbitrary Argument Lists¶
Finally, the least frequently used option is to specify that a function can be called
with an arbitrary number of arguments. These arguments will be wrapped up in a tuple
(see Tuples and Sequences).
Before the variable number of arguments, zero or more normal arguments may occur.


def write_multiple_items( **Kwargs):
    pass

"""


def example_funct( **Kwargs):
    print Kwargs                       # *args return a dictionary of arguments!!!!

def people_information( **people_ages):
    average_age = 0
    for age in people_ages.values():
        average_age += age

    average_age /= float(len(people_ages))
    return average_age


example_funct(nicola = 33, andrea = 24, Luca = 21, Gianni = 56)
print people_information(nicola = 33, andrea = 24, Luca = 21, Gianni = 56)
