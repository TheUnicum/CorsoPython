# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
9.9. operator — Standard operators as functions

https://docs.python.org/2/library/operator.html

+ somma
- sottrzione
* moltiplicazione
/ divisione

// double division , Parte intera della divisione
%  modulo , resto della divisione

**  esponente>

"""

print 20 + 3
print 20 - 3
print 20 * 3
print 20 / 3.0
print #questo scrive una riga vuota

print 20 // 3.0   #Parte intera della divisione
print 20 %  3.0   #resto della divisione  6-12-18 resto 2

print
print 2**4
print 6**78

print
print  3 + 4 , type(3 + 4)
print '3'+'4', type('3'+'4')

print '3'* 4
print 3 * '112233'
print 3 * '112233_ '
print '-'*40


"""
Full list form site python docs

Operation   Syntax  Function
Addition    a + b   add(a, b)
Concatenation   seq1 + seq2 concat(seq1, seq2)
Containment Test    obj in seq  contains(seq, obj)
Division    a / b   div(a, b) (without __future__.division)
Division    a / b   truediv(a, b) (with __future__.division)
Division    a // b  floordiv(a, b)
Bitwise And a & b   and_(a, b)
Bitwise Exclusive Or    a ^ b   xor(a, b)
Bitwise Inversion   ~ a invert(a)
Bitwise Or  a | b   or_(a, b)
Exponentiation  a ** b  pow(a, b)
Identity    a is b  is_(a, b)
Identity    a is not b  is_not(a, b)
Indexed Assignment  obj[k] = v  setitem(obj, k, v)
Indexed Deletion    del obj[k]  delitem(obj, k)
Indexing    obj[k]  getitem(obj, k)
Left Shift  a << b  lshift(a, b)
Modulo  a % b   mod(a, b)
Multiplication  a * b   mul(a, b)
Negation (Arithmetic)   - a neg(a)
Negation (Logical)  not a   not_(a)
Positive    + a pos(a)
Right Shift a >> b  rshift(a, b)
Sequence Repetition seq * i repeat(seq, i)
Slice Assignment    seq[i:j] = values   setitem(seq, slice(i, j), values)
Slice Deletion  del seq[i:j]    delitem(seq, slice(i, j))
Slicing seq[i:j]    getitem(seq, slice(i, j))
String Formatting   s % obj mod(s, obj)
Subtraction a - b   sub(a, b)
Truth Test  obj truth(obj)
Ordering    a < b   lt(a, b)
Ordering    a <= b  le(a, b)
Equality    a == b  eq(a, b)
Difference  a != b  ne(a, b)
Ordering    a >= b  ge(a, b)
Ordering    a > b   gt(a, b)
"""
