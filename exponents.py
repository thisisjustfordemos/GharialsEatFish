def exponents(a):
	return a**10

def sqr(a, b):
	ans = 0
	while b < 0:
		b /= a
		ans+=1
	return ans
