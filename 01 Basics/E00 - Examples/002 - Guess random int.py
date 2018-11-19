# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

import random

def main():
    num = random.randint(1,100)
    print num
    while True :

        val  = raw_input('Ciao, Indovina il numera tra [1:100] un valore :')
        if val == 'quit' or val == 'q': break

        val_int = int(val)

        if num < val_int :
            print 'Il numero da indovinare e\' minore'
        elif num > val_int :
            print 'Il numero da indovinare e\' maggiore'
        else:
            print 'Indovinato, il numero era : %d' %num
            print '\n'*2
            num = random.randint(0,100)

if __name__ == '__main__':
    main()