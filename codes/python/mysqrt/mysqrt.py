'''
A python module for calculating square root using the Newton's method implemented in ME522.
'''


def sqrtNT(x):
	'''
	The actual sqrtNT function
	Takes one input x: the number whose square root is to be calculated 
	'''
	s = 1.0
	kmax = 100
	tol = 1.0e-14
	for k in range(kmax):
    		print("Iteration number %s, s = %20.15f" %(k,s))
    		s0 = s
    		s = 0.5*(s + x/s)
    		delta_s = s - s0
    		if (abs(delta_s)/x)<tol:
    				break
	print("After %s number of iteration ,s = %20.15f" %(k+1,s))
