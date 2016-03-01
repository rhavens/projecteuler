# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

div_arr = [11,12,13,14,15,16,17,18,19,20]

# primes up to 20
product_of_primes = 2*3*5*7*11*13*17*19
cur = product_of_primes

while (1):
	success_flag = 1
	for i in div_arr:
		if (cur % i):
			success_flag = 0
			break;
	if (success_flag):
		print cur
		break;
	cur += product_of_primes