import math

def ncr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
def helper(p, n):
	if(n == 0):
		return pow(1 - p,100)
	else:
		return helper(p,n-1) + ncr(100,n)*pow(p,n)*pow(1-p,100-n)


if __name__ == '__main__':
 	print(helper(0.2,20))
