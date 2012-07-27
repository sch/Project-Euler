#!/usr/bin/env python
# encoding: utf-8
"""
pe1.py

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Exactly! This was another one that I solved without code, also. 

First of all, stop thinking on the number 1000 and turn your 
attention to the number 990 instead. If you solve the problem 
for 990 you just have to add 993, 995, 996 & 999 to it for 
the final answer. This sum is (a)=3983 

Count all the #s divisible by 3: From 3... to 990 there are 
330 terms. The sum is 330(990+3)/2 (b)=163845 
Count all the #s divisible by 5: From 5... to 990 there are 
198 terms. The sum is 198(990+5)/2 (c)=98505 

Now, the GCD (greatest common divisor) of 3 & 5 is 1 so the 
LCM (least common multiple) should be 3x5 15. 
This means every number that divides by 15 was counted twice 
and it should be done only once. Because of this, you have an 
extra set of numbers started with 15 all the way to 990 that 
has to be removed from (b)&(c). 
Then, from 15... to 990 there are 66 terms and the sum is 
66(990+15)/2 (d)=33165 

The answer for the problem is: (a)+(b)+(c)-(d) = 233168 

Simple but very fun problem.




"""

import sys
import os
import math


def main():
	x = math.floor( 999/3 )
	y = math.floor( 999/5 )
	z = math.floor( 999/15 )
	print x, y, z
	
	three = []
	x = 3
	while (x < 1000):
		three.append(x)
		x = x + 3
	print three
	
	five = []
	y = 5
	while (y < 1000):
		five.append(y)
		y = y + 5
	print five
	
	fifteen = []
	z = 15
	while (z < 1000):
		fifteen.append(z)
		z = z + 15
	print fifteen
	
	for i in five:
		for j in fifteen:
			if i == j:
				five.remove(i)
	print five
	
	sumfive = sum(five)
	sumthree = sum(three)
	print (sumfive + sumthree)
	
	#CORRECT!
	
	result = 0
	for i in range(1,1000):
	    if i % 3 == 0 or i % 5 == 0:
	        result = result + i
	print str(result)
	
	print sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])
	
	print reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(1000)))
	
	print sum(set(range(0,1000,3))|set(range(0,1000,5)))
	
	x = 0
	for y in range(1000):
		if (y % 5 == 0 or y % 3 == 0):
			x += y
	print x

if __name__ == '__main__':
	main()