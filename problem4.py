# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
	n_copy = n
	rev = 0
	while (n_copy > 0):
		rev = rev*10 + n_copy % 10
		n_copy /= 10
	return (rev == n)

n1 = 999
maxpal = 0

while (n1 >= 100):
	n2 = n1
	while (n2 >= 100):
		if (is_palindrome(n2*n1)):
			maxpal = max(n2*n1, maxpal)
		n2 -= 1
	n1 -= 1

print maxpal