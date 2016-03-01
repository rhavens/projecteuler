# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

to_factor = 600851475143
maxfactor = int(sqrt(to_factor)) + 1

for i in xrange(maxfactor, 1, -1):
	if not (to_factor % i):
		factor_maxfactor = int(sqrt(i)) + 1
		prime_flag = 1
		for j in xrange(4, max(5,factor_maxfactor)):
			if not (i % j):
				prime_flag = 0
				break;
		if (prime_flag):
			print i
			break