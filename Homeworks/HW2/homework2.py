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
