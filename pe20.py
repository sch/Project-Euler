#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Adrian Schaedle
"""

import sys
import os
import math

# other versions
# reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])


def main():
	bignum = math.factorial(100)
	print bignum
	numstring = str(bignum)

	print "type of numstring", type(numstring)

	answer = 0
	for i in range(len(numstring)):
		digit = int(numstring[i])
		answer = answer + digit
	print answer


if __name__ == '__main__':
	main()




