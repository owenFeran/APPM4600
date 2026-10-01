
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def fixedptList(f,x0,tol,Nmax):
    lis=[x0]
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

def convspeed(iterations,speed):
    length=len(iterations)
    if speed=='linear':
        return abs(iterations[-2]-iterations[-1])/abs(iterations[-3]-iterations[-2])
    elif speed=='quadratic':
        return abs(iterations[-2]-iterations[-1])/abs(iterations[-3]-iterations[-2])**2
    else:
        print('Uh oh, pick quadratic or linear speed.')
        return

def bisection(a,b,tol,nMax,f):
    fa=f(a)
    fb=f(b)
    ier=0

    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier]

    if(fa==0):
        astar=a
        return [astar, ier]
    if(fb==0):
        astar=b
        return [astar, ier]

    count=0
    d=0.5*(a+b)
    while abs(d-a)>tol and count<nMax:
        fd=f(d)
        if fd==0:
            astar=d
            return [astar,ier]

        if (fa*fd<0):
            b=d
        else:
            a=d
            fa=fd

        d=0.5*(a+b)
        count+=1

    astar=d
    return [astar,ier,count]

def newton(f,fp,x0,tol,nMax):
    p=np.zeros(nMax+1)
    p0=x0
    p[0]=x0

    ier=0   
    for i in range(nMax):
        p1=p0-f(p0)/fp(p0)
        p[i+1]=p1
        if abs(p1-p0)<tol:
            pstar=p1
            return [pstar,ier,i+1]

        p0=p1
    ier=1
    pstar=p1
    return [pstar,ier,i+1]

        

def main():

    f1= lambda x: -16+6*x +12/x
    iter1=fixedptList(f1,1.8,10**-8, 100)
    f2= lambda x:(2/3)*x + 1/(x**2)
    iter2=fixedptList(f2,1.3,10**-8, 100)
    print(iter2)
    speed=convspeed(iter2[0],'quadratic')
    print('speed is:',speed)
    f3=lambda x: (12)/(1+x)
    iter3=fixedptList(f3,2.5,10**-5,100)
    speed2=convspeed(iter3[0], 'linear')
    print(speed2)

    #Problem 2
    alphT=60**3 * 24 *0.138*10**(-6)

    f4= lambda x: 35*sp.special.erf(x/(2*np.sqrt(alphT)))-15
    x=np.arange(0.7,10,0.1)
    plt.plot(x,f4(x))
    plt.show()

    err=10**(-13)
    bis=bisection(0,0.7,err,100,f4)
    print(bis)
    f4p= lambda x:70/np.sqrt(np.pi)*np.exp(-(x/(2*np.sqrt(alphT)))**2)/(2*np.sqrt(alphT))
    newt=newton(f4,f4p,0.01,err,100)
    newt2=newton(f4,f4p,0.7,err,100)
    print(newt)
    print(newt2)

    # f5= lambda x: x-(x**5 - 7)/x**2
    # fix5=fixedptList(f5,1,10**-10,100)
    # print(fix5)
    f6= lambda x: x-(x**5-7)/12
    fix6=fixedptList(f6,1,10**-10,100)
    print(fix6)




    
    

main()

    