#!/usr/bin/env python
# encoding: utf-8
"""
pe7.py

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Created by Adrian on 2010-10-27.
Copyright (c) 2010 __bullion__. All rights reserved.
"""

import sys
import os

def isPrime():
	if ( n = 1 ):
		return False
	else if ( n < 4 ):
		return True			#cuz 2 and 3 are prime
	else if ( n%2 == 0):
		return False
	else if ( n < 9 ):
		return True			#2(2), 2(3), and 2(2(2)) have been eliminated
	else if (n%3 == 0):
		return False
	else if 

def iter_primes ():
        # handle trivial case
        yield 2
        val = 1
        primesq_pairs = []
        while True:
                curr = None
                while (curr is None):
                        val += 2
                        curr = val
                        for prime, square in primesq_pairs:
                                if (curr < square):
                                        break
                                if (curr % prime == 0):
                                        curr = None
                                        break
                primesq_pairs.append ((curr, curr**2))
                yield curr


primer_gen = iter_primes()
for x in xrange (10001):
        result = primer_gen.next()
print result

def main():
	primer_gen = iter_primes()
	for x in xrange (10001):
	        result = primer_gen.next()
	print result


if __name__ == '__main__':
	main()

