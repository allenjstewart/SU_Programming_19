######################################
#Below is code that is supposed to compute the Eulers method 
#I have purposely introduced an error(s) into the code
#The Purpose of this code is to practice debugging some common errors
#I would like you to find the error and correct it
#Be sure to commit an corrections into your own personal folder

import math as m
import numpy as np
import matplotlib.pyplot as plt

#Euler's Method

def function(y,t):
	dy=yt
	return dy

def euler(t0,y0n,tfinal):
    dt=(tfinal-t0)/n
    y=[]
    t=[]]
    y.append(y0)
    t.append(t0)
    for i in range (0,n):
        t.append((i+1))*dt)
        y.append(y[i]+function(yi,t[i])*dt)
    return plt.plot(t,y)