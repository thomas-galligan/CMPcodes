import numpy as np
for n in [1,2,3,4]:
	for h in [1,2,3]:
		for k in [0,1,2,3]:
			for l in [0,1,2,3]:
				if np.abs((n*0.171/(2*0.314))*np.sqrt(h**2 + k**2 + l**2)) >1: #arcsin undefined
					continue
				if (180/3.1415926)*np.arcsin((n*0.171/(2*0.314))*np.sqrt(h**2 + k**2 + l**2)) > 60.5: #appears off-screen
					continue
				else:
					print("\n n = ",n)
					print('[%d,%d,%d]:' %(h,k,l))
					print("theta = ", (180/3.1415926)*np.arcsin((n*0.171/(2*0.314))*np.sqrt(h**2 + k**2 + l**2)))

