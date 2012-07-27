#!/usr/bin/env python
# encoding: utf-8
"""
pe5.py
Created by Adrian Schaedle

2520 is the smallest number that can be divided by each of the numbers from
	 1 to 10 without any remainder. What is the smallest positive number that
	 is evenly divisible by all of the numbers from 1 to 20?


"""

import sys
import os

through = 20

def main():
	result = through
	while indivisibleByRange(result):
		result = result + through
	print result

def indivisibleByRange(num):
	i = through
	while i != 0:
		if num%i != 0:
			return True
		i = i - 1
	return False




if __name__ == '__main__':
	main()



