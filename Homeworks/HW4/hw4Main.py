import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # f =lambda x: np.exp(3*x)-27*x**6 + 27*x**4 * np.exp(x)-9*x**2 * np.exp(2*x)
    # fp= lambda x: 3*np.exp(3*x)-162*x**5+108*x**3 * np.exp(x)+27*x**4 * np.exp(x)-18*x*np.exp(2*x)-18*x**2*np.exp(2*x)
    # fpp = lambda x: 9*np.exp(3*x) - 810*x**4 + 324*x**2*np.exp(x) + 108*x**3*np.exp(x) + 108*x**3*np.exp(x) + 27*x**4*np.exp(x) - 18*np.exp(2*x) - 36*x*np.exp(2*x) - 36*x*np.exp(2*x) - 36*x**2*np.exp(2*x)
    # x=np.arange(3,3.83,0.01)
    # plt.plot(x,f(x))
    # plt.show()
    # res1=newton(f,fp,4,10**-10,100)
    # iterations1=res1[1][res1[1]!=0]
    # print(iterations1)
    # speed1=convspeed(iterations1,1)
    # print(speed1)
    # res2=newtonMod1(f,fp,fpp,4,10**-8,100)
    # print(res2)
    f2= lambda x: x**6-x-1
    f2p=lambda x:6*x**5 -1
    resSec=secant(2,1,f2,10**-8,100)
    resNewt2=newton(f2,f2p,2,10**-8,100)
    # print(resSec)
    # print(resNewt2)
    accRes1=resSec[resSec!=0]
    r1=accRes1[-1]
    accRes2=resNewt2[1][resNewt2[1]!=0]
    r2=accRes2[-1]
    print(accRes1)
    print(accRes2)
    secErr=[abs(accRes1[i+1]-accRes1[i]) for i in range(len(accRes1)-1)]
    newtErr=[abs(accRes2[i+1]-accRes2[i]) for i in range(len(accRes2)-1)]
    df = pd.DataFrame({
    'Column1': pd.Series(secErr),
    'Column2': pd.Series(newtErr)})
    print(df)
    # 1. Define the "exact" root using the final Newton approximation
    alpha = accRes2[-1]

    # 2. Calculate the errors |x_k - alpha| for both methods
    # We drop the very last term [:-1] because the error is exactly 0, 
    # and taking the log of 0 will crash the plot.
    err_secant = np.abs(accRes1[:-1] - alpha)
    err_newton = np.abs(accRes2[:-1] - alpha)

    # 3. Create the x and y coordinates for the plot
    # x-axis is |x_k - alpha|, y-axis is |x_{k+1} - alpha|
    x_secant = err_secant[:-1]
    y_secant = err_secant[1:]

    x_newton = err_newton[:-1]
    y_newton = err_newton[1:]

    # 4. Create the log-log plot
    plt.figure(figsize=(8, 6))
    plt.loglog(x_newton, y_newton)
    plt.loglog(x_secant, y_secant)

    # 5. Format the plot
    # plt.xlabel('|x_k - alpha| (Current Error)')
    # plt.ylabel('|x_{k+1} - alpha| (Next Error)')
    # plt.title('Log-Log Plot of Convergence Errors')
    # plt.grid(True, which="both", linestyle="--", alpha=0.6)
    # plt.legend()
    plt.show()



def newton(f,fp,p0,tol,nMax):
    p=np.zeros(nMax+1)
    p[0]=p0
    for i in range(nMax):
        p1=p0- f(p0)/fp(p0)
        p[i+1]=p1
        if abs(p1-p0)<tol:
            pstar=p1
            return [p1,p]

        p0=p1

    print('max number it')
    return [p0,p]

def newtonMod1(f,fp,fpp,p0,tol,nMax):
    g= lambda x: f(x)/fp(x)
    gp=lambda x:((fp(x)**2)-f(x)*fpp(x))/(fp(x)**2)
    p=np.zeros(nMax+1)
    p[0]=p0
    for i in range(nMax):
        p1=p0- g(p0)/gp(p0)
        p[i+1]=p1
        if abs(p1-p0)<tol:
            pstar=p1
            return [p1,p]

        p0=p1

    print('max number it')
    return [p0,p]

def convspeed(iterations,speed):
    return abs(iterations[-2]-iterations[-1])/abs(iterations[-3]-iterations[-2])**speed

def secant(x1,x0,f,tol,nMax):
    res=np.zeros(nMax+2)
    res[0]=x0
    res[1]=x1
    fch=f(x1)
    fch2=f(x0)
    if fch==fch2:
        print('error')
        return (0)
    for i in range(nMax):
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        res[i+2]=x2
        if abs(x2-x1)<tol:
            return res
        x0=x1
        x1=x2

main()