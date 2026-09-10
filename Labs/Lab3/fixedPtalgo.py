# import libraries
import numpy as np

def driver():
# test functions
    f1=lambda x: 1+0.5*np.sin(x)
    Nmax = 100
    tol = 1e-6
    # test f1 '''
    x0 = 0.0
    print(fixedptList(f1,x0,tol,Nmax))
    #print('the root finding iterations are' , {res})
    #test f2 '''

   
# define routines
def fixedptList(f,x0,tol,Nmax):
    lis=[x0]
    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    count = 0
    while (count <Nmax):
        count = count +1
        x1 = f(x0)
        lis.append(x1)
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return np.array(lis)
        x0 = x1

    xstar = x1
    ier = 1
    return np.array(lis)


driver()