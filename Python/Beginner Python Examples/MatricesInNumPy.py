import numpy as np

#Create an array

A=np.array([[1,2,3],[3,4,5]])

#Create an array of complex numbers

A=np.array([[1,2,3],[3,4,5]], dtype=complex)

#Create an array of zeros

np.zeros((3,3))

#Create an array of ones

np.ones((3,3))

#Create an array of the first 12 nonnegative integers into a 2x6 matrix

np.arange(12).reshape(2,6)

#Some matrix operations in numpy can be done with arrays
#In some cases it can be more convienient to use the matrix class rather than array

A=np.array([[3,6,7],[5,-3,0]])
B=np.array([[1,1],[2,1],[3,-3]])

#Adding

C=A+A

#Multiplication

C=A.dot(B)

#Transpose

A.transpose()

#Accessing elements, rows, and columns

#Top left element
A[0][0]

#Bottom right element
A[-1][-1]

#Third row, second column
A[2][1]

#First row
A[0]

#Last Row
A[-1]

#First Column
A[:,0]

#Last Column
A[:,-1]

#In order to find an inverse of a matrix we need the linear algebra library

from numpy.linalg import inv

A=np.array([[1,2],[3,4]])
invA=inv(A)
