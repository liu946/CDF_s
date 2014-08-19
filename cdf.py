import math

PRECISION = 1e-6
DELTA = 1e-5

def testfoo(x):
	return math.exp(-abs(x))/2

def cdf(foo,sta):
	sum = 0
	x=sta
	while(foo(x)>PRECISION):
		sum+=(foo(x)*DELTA)
		x-=DELTA

	return sum
	

