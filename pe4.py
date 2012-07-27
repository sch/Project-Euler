#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Adrian on 2010-10-06.
Copyright (c) 2010 __bullion__. All rights reserved.
"""

import sys
import os
import string

def isPalindrome(x):
    p = str(x)
    if p == p[::-1]:
		return True
    else:
        return False

def palindrome(n):
	n = str(n)
	return n == n[::-1]

def main():
	
	print max(map(lambda s: bool(s) and max(s) or 0, [(filter(lambda n: n == int(str(n)[::-1]), map(lambda n: i*n, range(999, 99, -1)))) for i in range(999, 99, -1)]))
	
	
	palindromes = []
	
	i = 999
	j = 999
	while (i > 100):
		i = 999
		while j > 100:
			result = i * j
			if isPalindrome(result) == True:
				palindromes.append(result)
			j = j - 1
		i = i - 1
	
	print palindromes
	
	



if __name__ == '__main__':
	main()

