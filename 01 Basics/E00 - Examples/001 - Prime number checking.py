# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

def main():
    print "[Nota: questo script funziona solo in cmd.exe]\n"
    while True:
        number = input('Please enter a number to be checking as PRIME: ')
        if number <= 0 :break
        is_prime = True

        for factor in range(2,int(number**0.5)): #[2, sqr(number)]
            if number % factor == 0:
                is_prime = False
                break

        if is_prime == True:
            print '%s is a prime number!' %number
        else:
            print '%d is NOT a prime number' %number


if __name__ == '__main__':
            main()
