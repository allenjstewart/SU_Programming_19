#This code implement solves an equation Ax=b iteratively where A is 3x3.
#########################################################
#An iterative solver means that we first guess a solution
#Then proceed through a number of steps to more accurately approximate the solution
#Newton's Method is an iterative solver.
##############################################################
#Here is the process we will use
#First we solve and get x,y,and z in terms of the other variables
#For instance if A=[[1,2,1],[3,4,5],[-1,0,2]] and b=[3,7,10]
#Then x=3-2y-z, y=(7-3x-5z)/3, and z=10+x
#Then we plug in our guess and iterate 
#x_(k+1)=3-2y_k-z_k, y_(k+1)=(7-3x_k-5z_k)/3, and z_(k+1)=10+x_k
#
#We loop as many times until we have a desired accuracy |[x_(k+1),y_(k+1),z_(k+1)]-[x_k,y_k,z_k]|<e
#################################################################


#Import the appropriate libraries



def LinearSolveIt(A,b): # A is a 3x3 matrix, b is a vector

	#Create an If statement that will return an appropriate error if det(A)=0

	#Create an If statement that will return an appropriate error if the dimensions of A and b don't align

	#Create a guess that will be used. This way the user doesn't have to input one

	#Define an appropriate error for the solution

	#Create a while loop that runs the iteration while |[x_(k+1),y_(k+1),z_(k+1)]-[x_k,y_k,z_k]|<e
	    #You should create a break statement in your while loop. This will prevent the loop from running forever


	return sol #Return the solution vector 



########################################################

#Print out test of code for each equation

#A=[[1,2,3],[4,5,6],[7,8,9]], b=[10,11,12] Solution: This will return an error, det(A)=0

#A=[[4,5,7],[3,4,5],[5,6,7]], b=[3,4,5,-1,3] Solution: This will return an error, A and b are different sizes

#A=[[4,5,13],[3,4,5],[5,6,7]], b=[1,2,3] Solution: [-0.214286, 0.928571, -0.214286]
