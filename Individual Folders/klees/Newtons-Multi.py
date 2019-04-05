#This code implements a multi-variable Newton's Method
#The algorithm is about the same, except it is applied to a system of  equations,
#which amounts to finding the zeroes of functions, f_k(x)=0
#The key difference is the use of the  Jacobian matrix
#This is the matrix of derivatives associated to each variable.
#The Jacobian replaces the f'(a) from the single variable Newton's
#For the equations [x^2+y,xy-y^2-y] the Jacobian would be the matrix
#[[2x,y],[1,x-2y-1]]

#########################################################
#This code is already finished. You don't need to code anything at all.
#Your assignment here is to figure out what the code is doing
#And add comments accordingly
#Reading someone elses code isn't easy, but I think that getting a good look
#At some code that works will demonstrate how to use some of the functions
#That are commonly used in python
#There are some functions that you might need to look up in the documentation
#len, syp.diff, np.zeros, syp.sympify, syp.subs, np.dot, np.linalg.inv

#Feel free to mess around, hack, and break this code as much as you want.

#################################################################



import sympy as syp
import numpy as np
import math as math

def NewSolve(f,var,point,steps):
	J=[]
	for i in range(0,len(f)):
		J.append([])
	for m in range(0,len(f)):
		for n in range(0,len(var)):
			J[m].append(syp.diff(f[m],var[n]))
	Jpoint=np.zeros([len(f),len(var)])
	varpoint=[]
	numpoint=point
	fnumpoint=point
	for _ in range(0,steps):
		for k in range(0,len(point)):
			varpoint.append((var[k],numpoint[k]))
		if (len(varpoint)>len(point)):
			varpoint=varpoint[len(point):2*len(point)]
		for k in range(0, len(point)):
			fnumpoint[k]=syp.sympify(f[k]).subs(varpoint)
		for m in range(0,len(f)):
			for n in range(0,len(var)):
				Jpoint[m][n]=J[m][n].subs(varpoint)
		numpoint=numpoint-np.dot(np.linalg.inv(Jpoint),fnumpoint)
	return numpoint

#A test of the algorithm with the system of equations from the initial comment block
print(NewSolve(['x^2+y','x*y-y^2-y'],['x','y'],[1.5,1.5],10))

#Test the code on a couple of different systems of equations.
