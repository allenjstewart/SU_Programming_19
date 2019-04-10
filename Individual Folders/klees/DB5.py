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
	dy=y*t
	return dy

def euler(t0,y0,n,tfinal):
    dt=(tfinal-t0)/n
    y=[]
    t=[]
    y.insert(0,y0)
    t.insert(0,t0)
    for i in range (0,n):
        t.insert(0,(i+1)*dt)
        y.insert(0,y[i]+function(y[i],t[i])*dt)
    return plt.plot(t,y)
