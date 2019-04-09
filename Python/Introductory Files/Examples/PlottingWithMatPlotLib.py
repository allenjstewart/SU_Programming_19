#MatPlotLib is a numerical plotting library for Python
#It has tremendous functionality and a large amount of documentation
#You should be able to plot anything you want with MatPlotLib

import matplotlib.pyplot as plt

#Since MatPlotLib is a numerical plotter it is nice to have use of arrays
import numpy as np

#We create a set of inputs on our desired interval
#In this case, 100 points between 0 and 2

x=np.linspace(0,2,100)

#Each successive plot will plot on the same axes
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubic')

#Label the Axes
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

#The plot won't be displayed unless you add the show function
plt.show()