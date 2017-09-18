#HW1 Problem 3.8
from __future__ import division,print_function

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("millikan.txt",float)
x = data[:,0]
y = data[:,1]

#calculate Ex, Ey, Exx, Exy
Ex = sum(x)/len(x)
Ey = sum(y)/len(y)
Exx = sum(x**2)/len(x)
Exy = sum(x*y)/len(x)
#calculate m and c
m = (Exy-Ex*Ey)/(Exx-Ex**2)
c = (Exx*Ey-Exy*Ex)/(Exx-Ex**2)

#create a new list to store y_fit
yfit = []
#go through each point and calculate y_i = m*x_i+c from fitting
for x_i in x:
	y_i = m*x_i + c
	yfit.append(y_i) 

#calculate Plank's constant
h_fit = m*1.602e-19
#compare with actual h
h = 6.62607004081e-34
h_err = abs(h_fit - h)/h*100
print("m = ", m, " and c = ", c)
print("Planck's constant is " ,h_fit, " which is within", h_err, \
	" percent of the accepted value.")

#plot data
plt.plot(x,y,".")
#plot best fit line
plt.plot(x,yfit,"-", label= "best fitted line")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Photoelectric Effect')
plt.show()
