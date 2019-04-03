import numpy as np


#Solving a linear Equation 

a=np.array([2])
b=np.array([3])

x=np.linalg.solve(a,b)

#Solving a Matrix Equation

A=np.array([[1,0,1],[2,-3,1],[4,5,6]])
b=np.array([9,8,1])

x=np.linalg.solve(A,b)

#In order to solve a nonlinear equation we will need to make use of a non-linear solver
#There are a few techniques used in numerical solving
#The SciPy library has at least 6 and other libraries have more for specific purposes
#The SciPy solvers are part of optimize

import scipy.optimize

#We are going to use Broyden's Method which is a numerical simplification of Newton's Method


#First we need to define a function for us to solve 

def F(x):
	return np.cos(x)-[1,2,3,4]

x=scipy.optimize.broyden1(F,[1,1,1,1],f_tol=1e-14)

#Check our solution
np.cos(x)-[1,2,3,4]
