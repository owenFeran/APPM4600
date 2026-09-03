import numpy as np

x=[1,2,3]
print(x*3)

y=np.array(x)
print(y*3)

import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,100)
Ya=np.cos(x)
Yb=np.sin(x)

plt.plot(x,Ya)
plt.plot(x,Yb)
plt.show()

X=np.linspace(0,10,100)
Y=np.arange(0,10.1,0.1)
print('the first 3 entries of x are ', X[:3])
print(Y)

w = 10**(-np.linspace(1,10,10))
x=np.arange(1,len(w)+1)

plt.plot(x,np.log10(w))
plt.xlabel('x')
plt.ylabel('log10(w) and s')

s=3*w
plt.plot(x,s)
plt.show()

#4 start
