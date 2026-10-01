import numpy as np
def bisection(a,b,tol,f):
    fa=f(a)
    fb=f(b)
    if fb*fa>0:
        return 'error'

    d= 0.5*(a+b)
    while abs(d-a)>tol:
        fd=f(d)
        if fd==0:
            return d
        if fa*fd>0:
            a=d
            fa=fd

        else:
            b=d

        d=0.5*(a+b)

    return d

