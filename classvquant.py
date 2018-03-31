import numpy as np
from matplotlib import pyplot as plt

hv = 6.62607004e-34*1e13
k = 1.38064852e-23
N = 6.022e23
T_init = [2,20,200,2000] #initialize temperatures for first part of question 
E_cinit = np.zeros(4)
E_qinit = np.zeros(4)

for i in range(4):
	E_cinit[i] = 3*k*T_init[i] #compute classical mean energy
	E_qinit[i] = 3*hv/(np.exp(hv/(k*T_init[i]))-1)

print("Classical: ", E_cinit)
print("Quantum: ", E_qinit)

T = np.linspace(1,5000,1000) #define temperature axis
E_c = np.zeros(np.size(T))
E_q = np.zeros(np.size(T)) #initialize arrays

for i in range(np.size(T)):
	E_c[i] = 3*k*T[i]
	E_q[i] = 3*hv/(np.exp(hv/(k*T[i]))-1) + 3*hv/2
fig, ax1 = plt.subplots()

ax1.plot(T,E_c,label="Classical")
ax1.plot(T,E_q,label="Quantum")
#ax1.plot(T,E_q-E_c, label="Difference")
ax1.legend(loc = 1)
plt.ylabel("Mean energy(J)")
plt.xlabel("Temperature (K)")
ax2 = ax1.twinx()
ax2.semilogy(T,(np.abs(E_q-E_c)/E_q),'k-', label="Error")
#fig.tight_layout()
ax2.yaxis.set_label_position("right")
plt.ylabel("Error")
plt.legend(loc = 2)
plt.suptitle("Classical vs Quantum mean energies, with zero point motion")
plt.show()