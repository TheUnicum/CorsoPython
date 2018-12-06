#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   Escape Sequences    -

https://docs.python.org/2/reference/lexical_analysis.html

\newline	Ignored
\\			Backslash (\)
\'			Single quote (')
\"			Double quote (")
\a			ASCII Bell (BEL)
\b			ASCII Backspace (BS)
\f			ASCII Formfeed (FF)
\n			ASCII Linefeed (LF)
\N{name}	Character named name in the Unicode database (Unicode only)
\r			ASCII Carriage Return (CR)
\t			ASCII Horizontal Tab (TAB)
\uxxxx		Character with 16-bit hex value xxxx (Unicode only)	(1)
\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)	(2)
\v			ASCII Vertical Tab (VT)
\ooo		Character with octal value ooo	(3,5)
\ xhh		Character with hex value hh	(4,5)

"""

print 'Hello\nWorld'
print
print 'Hello\'World\''
print
print "----- Caratteri speciali ------"
print "ASCII Bell (BEL)     : \a"
print "ASCII Backspace (BS) : \b"
print "ASCII Formfeed (FF)  : \f"
print "ASCII Linefeed (LF)  : \n"
