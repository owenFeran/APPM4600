import numpy as np
import matplotlib.pyplot as plt
import math


#problem 2
A=0.5*np.array([[1,1],[1+10**(-10),1-10**(-10)]])
#condnum=np.linalg.cond(A)
S=np.linalg.svd(A)[1]
condition=S[0]/S[1]
print(condition)

a=-0.5
b=0.5
mat1=np.array([[(1-10**10)*a*10**(-5)+10**10*b*10**(-5)],[(1+10**10)*a*10**(-5)-10**10*b*10**(-5)]])
normmat1=np.linalg.norm(mat1)
print(normmat1/np.sqrt(2))
#problem 6
x=np.linspace(-20,20)
f=x-4*np.sin(2*x)-3

plt.plot(x,f)
plt.plot(x,0*x)
plt.show()

f2= lambda x: (1/6)*x**2
x3=9.999999995000000*(10**-10)
f2(x3)

#4
f3= lambda x:2*x-1-np.sin(x)
x4=np.linspace(-10,10)
plt.plot(x4,f3(x4))
plt.show()

#6
f4= lambda x: 4*np.sin(2*x)+3
x4=np.linspace(-1,8,100)
plt.plot(x4,f4(x4))
plt.plot(x4,x4)
plt.show()

f5= lambda x: -np.sin(2*x)+5*x/4-3/4
accFunc= lambda x:abs(-2*np.cos(2*x)+5/4 -1)*10**(-10)


def fixedPtHw(f,Nmax,x0,accFunc):
    count=0
    while abs(x1-x0) > accFunc(x1):
        x1=f(x0)
        while count<=Nmax:
            x0=x1
            x1=f(x0)
            count+=1
        return (x1,count)
    print('Error, reached max number of iterations')
    return
    
res=fixedPtHw(f5,100,3.1,accFunc)
print(res)