#-*- coding: utf-8 -*-

"""
Docs
https://docs.python.org/2/tutorial/controlflow.html#defining-functions

4.6. Defining Functions


    >-	global GLOBAL_VARIABLE	-<


inside functions the 'other-variable' are 'READ-ONLY'

IF i need to access at these variables I need to use 'global' keyword

"""


# ESAMPLE A

var_global = 'GLOBAL'

def change_global():
    var_global = 'LOCAL'
    print 'var_global in FUNC= ', var_global

def change_global_correct():
    global var_global                           # <--- GLOBAL
    var_global = 'LOCAL'
    print 'var_global in FUNC= ', var_global


print 30 * '-','Example A-1 - [NO globlal]'
change_global()
print 'var_global in MAIN= ', var_global

print 30 * '-','Example A-2 - [globlal]'
change_global_correct()
print 'var_global in MAIN= ', var_global



# ESAMPLE B

max_number = 0

def set_max_number(list_):
    largest = list_[0]

    for number in list_:
        if number > largest:
            largest = number

    max_number =  largest # here I create a new local variable with same name
    print 'max_number in FUNC= ', max_number

def set_max_number_with_global(list_):
    global max_number                            # <--- GLOBAL
    largest = list_[0]

    for number in list_:
        if number > largest:
            largest = number

    max_number =  largest
    print 'max_number in FUNC= ', max_number


print
print 30 * '-','Example B-1 - [NO globlal]'
set_max_number([3,4,643,3245,5,22])
print 'max_number in MAIN= ', max_number

print 30 * '-','Example B-2 - [globlal]'
set_max_number_with_global([3,4,643,3245,5,22])
print 'max_number in MAIN= ', max_number


# strange:
# max_number inside function is 3245
# max_number outside function si 0
