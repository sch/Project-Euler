#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Adrian on 2010-09-29.
Copyright (c) 2010 __bullion__. All rights reserved.
"""

import sys
import os

# find prime factors of a number
def primefactors(x):
    factorlist = []
    loop = 2
    while loop <= x:
        if x%loop == 0:
            x/=loop
            factorlist.append(loop)
        else:
            loop += 1
    return factorlist

def factorizer( n ):
	left = 2
	while n%left != 0:
		right = n/left
		left = left + 1
		

def main():
	
	print primefactors(600851475143)
	


if __name__ == '__main__':
	main()

