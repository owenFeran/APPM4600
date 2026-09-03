import matplotlib.pyplot as plt 
import numpy as np

x=np.arange(1.92,2.08000001,0.001)
f1=x**9-18*x**8 +144*x**7-672*x**6 +2016*x**5 -4032*x**4 +5376*x**3 -4608*x**2 +2304*x-512
f2=(x-2)**9

plt.plot(x,f1)
plt.plot(x,f2)
plt.show()
