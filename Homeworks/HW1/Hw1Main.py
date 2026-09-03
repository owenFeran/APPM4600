import matplotlib.pyplot as plt 
import numpy as np

x=np.arange(1.92,2.08000001,0.001)
f1=x**9-18*x**8 +144*x**7-672*x**6 +2016*x**5 -4032*x**4 +5376*x**3 -4608*x**2 +2304*x-512
f2=(x-2)**9

plt.plot(x,f1)
plt.plot(x,f2)
plt.show()


p =np.arange(-16,1,1)
eps=10.**(p)
print(2)

x1=np.pi
x2=10**6

f1=np.cos(x1+eps)-np.cos(x1)
f2=-2*np.sin(0.5*(2*x1+eps))*np.sin(0.5*eps)
res1=abs(f1-f2)
print(res1)
plt.plot(np.arange(0,17,1),res1)
plt.show()

f3=np.cos(x2+eps)-np.cos(x2)
f4=-2*np.sin(0.5*(2*x2+eps))*np.sin(0.5*eps)
res2=abs(f3-f4)
print(res2)
plt.plot(np.arange(0,17,1),res2)
plt.show()

f5=-eps*np.sin(x1)-0.5*eps**2*np.cos(x1)
f6=-eps*np.sin(x2)-0.5*eps**2*np.cos(x2)
res3=abs(f5-f1)
print(res3)
plt.plot(range(0,len(eps)),res3)
plt.show()
res4=abs(f6-f2)
plt.plot(range(0,len(eps)),res3)
plt.show()

plt.semilogx(eps,res3)
plt.show()

