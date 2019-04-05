######################################
#Below is code that is supposed to compute the Eulers method
#I have purposely introduced an error(s) into the code
#The Purpose of this code is to practice debugging some common errors
#I would like you to find the error and correct it
#Be sure to commit any corrections into your own personal folder

import math as m
import numpy as np
import matplotlib.pyplot as plt

#Euler's Method

def function(y,t):
	dy=y*t
	return dy

def euler(t0,y0,n,tfinal):
	dt=(tfinal-t0)/n
	y=np.array([])
	t=np.array([])
	y = np.append(y,y0)
	t = np.append(t,t0)
	for i in range (0,n):
		t = np.append(t,(i+1)*dt)
		y = np.append(y,y[i]+function(y[i],t[i])*dt)
	plt.plot(t,y)
	plt.show()
    #return plt.plot(t,y)


def main():
	euler(2,3,10,5)

if __name__ == '__main__':
	main()
