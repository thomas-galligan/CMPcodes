import numpy as np
import matplotlib.pyplot as plt
pi = 3.14159265359
k = 1.38064852e-23
N = 6.022e23 #assume we're working with one mole
T = [0.1,1.0,5,8,10,15,20]
C = [8.5e-7, 8.6e-4, 1.2e-1, 5.9e-1, 1.1, 2.8, 6.3]
logC = np.log(C) #take the log
logT = np.log(T)
logTlin = np.log(np.linspace(0.1,20,100)) #create a linspace to plot the fit againsts
z = np.polyfit(logT,logC,1) #perform fit 
poly = np.poly1d(z)
print(z)
print("T_Debye = ", (12*(pi**4)*k*N/(5*np.exp(z[1])))**(1/3))
print()
plt.plot(logT,logC,label="data")
plt.plot(logTlin,poly(logTlin),label="fit")
plt.legend()
plt.show()