def exponents(a):
	return a*a*3
def sqr(a, b):
	ans = 0
	while b < 0:
		b /= a
		ans+=1
	return ans
