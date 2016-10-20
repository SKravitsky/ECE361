#Steven Kravitsky
#12586350
#Assignment 4
#Problem 1

import math

def nCr(n,k):
	f = math.factorial
	return f(n) / f(k) / f(n-k)

if __name__ == '__main__':
	n = 99
	p = (1.0/3.0)
	sum = 0

	for k in range(41,100):
		total = nCr(n,k) * math.pow(p,k) * math.pow((1-p),(n-k))
		sum = sum + total 

	print sum
