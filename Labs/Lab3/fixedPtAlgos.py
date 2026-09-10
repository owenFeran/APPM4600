# import libraries
import numpy as np

def driver():
# test functions
    f1=lambda x: np.sqrt(10/(x+4))
    Nmax = 100
    tol = 1e-15
    # test f1 '''
    x0 = 1.5
    resTup=fixedptList(f1,x0,tol,Nmax)
    print(resTup)
    print(convspeed(resTup[0],'linear'))
    aitkenRes=aitkenSeq(f1,resTup[0],tol,Nmax)
    print(aitkenRes)
    print(convspeed(aitkenRes[0],'linear'))
    


   
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
            return (np.array(lis),count)
        x0 = x1

    xstar = x1
    ier = 1
    return np.array(lis)

def aitkenSeq(f,seq,tol,Nmax):
    length=len(seq)
    res=[]
    count=0
    while count<=Nmax:
        for i in range(length-2):
            entry=seq[i]-(seq[i+1]-seq[i])**2/(seq[i+2]-2*seq[i+1]+seq[i])
            res.append(entry)
            count+=1
            if count>=2 and abs(res[-1]-f(res[-2]))<tol:
                return (np.array(res),count)
    print('Reached max number of iterations')
    return (np.array(res),count)

def convspeed(iterations,speed):
    length=len(iterations)
    if speed=='linear':
        return abs(iterations[-2]-iterations[-1])/abs(iterations[-3]-iterations[-1])
    elif speed=='quadratic':
        return abs(iterations[-2]-iterations[-1])/abs(iterations[-3]-iterations[-1])**2
    else:
        print('Uh oh, pick quadratic or linear speed.')
        return
    
    





driver()