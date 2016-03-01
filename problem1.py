# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
target = 1000

for i in xrange(3,target):
	if not (i % 3):
		total += i
	elif not (i % 5):
		total += i

print total