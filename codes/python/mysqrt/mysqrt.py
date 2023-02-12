x = 16.0
s = 1.0
kmax = 6
for k in range(kmax):
    print("Iteration number %s, s = %s" %(k,s))
    s = 0.5*(s + x/s)
print("After %s number of iteration ,s = %s" %(k+1,s))
