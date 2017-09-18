#HW1 Problem 3.7
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np
#specify N
N = 1001
#create a grid of NxN
xgrid = np.linspace(-2,2,N)
ygrid = np.linspace(-2,2,N)
#create 2 sets of (x,y) to store points inside and outside Mandelbrot set 
xinMan = []
yinMan = []
xoutMan = []
youtMan = []

#check each point in the grid
for x in xgrid:
	for y in ygrid:
		c = x + y*1j
		#check if c is in Mandelbrot set 
		#100 iteration
		it = 100
		#start with z = 0
		z = 0
		for i in range(it):
			z = z*z + c
		if np.absolute(z) < 2:
			#if c is in Mandelbrot set, add to inMan
			xinMan.append(x)
			yinMan.append(y)
		else:
			#if c is NOT in Mandelbrot set, add to outMan
			xoutMan.append(x)
			youtMan.append(y)

plt.plot(xinMan,yinMan,"ko")
plt.plot(xoutMan,youtMan,"wo")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Mandelbrot Set')
plt.show()


