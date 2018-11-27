# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""

" While Vs FOr LOOP ""

"""

mail = {'mattiab' : 'mattia.benedetti@parpas.com', 'mattiaf' : 'mattia.fortin@parpasa.com', 'gabriele': 'gabriele.rizzo.com', 'teven' :'steven.freschet@parpas.com'}
stagioni = ['inverno', 'primavera', 'estate' , 'autunno']
colori = ['bianco', 'verde', 'giallo', 'rosso']

print
print '----------While Loop----------'
i=0
while i < len(stagioni):
    print stagioni[i]
    i = i+1

#Better in looping to a sequence/list
print
print '----------For Loop----------'
for element in stagioni:
    print element
