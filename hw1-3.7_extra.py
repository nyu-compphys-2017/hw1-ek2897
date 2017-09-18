#HW1 Problem 3.7 (color plot)
from __future__ import division,print_function

import matplotlib.pyplot as plt
import numpy as np

#specify N
N = 5001
#create a grid of NxN
xgrid = np.linspace(-2,2,N)
ygrid = np.linspace(-2,2,N)

#create an empty list to store the number of iterations (100 if in the set)
a = []

#check each point in the grid
for y in ygrid:
	for x in xgrid:
		c = x + y*1j
		#check if c is in Mandelbrot set 
		#100 iteration
		it = 100
		#start with z = 0
		z = 0+0j
		#store number of iteration
		numit = 100
		for i in range(it):
			z = z**2 + c
			if np.absolute(z) > 2:
				numit = i
				break
		#add numit to the list
		a.append(numit)

		
#transform a list to an array of size NxN
numitarray = np.asarray(a).reshape((N,N))
#try log scale
#plt.pcolor(xgrid, ygrid, numitarray, cmap=plt.cm.YlGnBu)
plt.pcolor(xgrid, ygrid, numitarray, cmap=plt.cm.jet)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Mandelbrot Set')
plt.colorbar()
plt.show()



