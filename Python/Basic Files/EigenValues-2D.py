#This code finds the eigenvalues and eigenvectors for a 2x2 matrix, [[a,b],[c,d]]
#########################################################
#1. Solve the characteristic equation x^2-(a+d)x+(ad-bc)
#2. Solve the equation (A-lambda*I)x=0
    #Since A-lambda*I is not invertible this would normally be tricky
    #But since we are dealing with a 2x2 system, being non-invertible
    #Is equivalent to the columns of the matrix being multiples of each other
    #Thus we can assume that x=[1,a] for some constant a
#3. Normalize both of the eigenvectors, i.e. reduce them so they have norm equal to 1	
#################################################################
#One important thing to note here is that we might have complexe solutions
#This is fine we want to include them in our answer
#You'll need to figure out how to appropriately do this.


#Import the appropriate libraries



def EVal(A): # A is a 2x2 matrix

	#Create an If statement that will return an appropriate error if A is not 2x2

	#Solve the characteristic equation

	#Find a solution to (A-lambda*I)x=0 for both solutions

	#Normalize your solutions	   	 

	return sol #Return the solution in the form [lambda_1,v_1],[lambda_2,v_2]



########################################################

#Print out test of code for each equation

#A=[[1,2],[3,4], Solution: [5.37228,[0.415974, 0.909377]], [-0.372281,[-0.824565, 0.565767]]

#A=[[0,1],[-1,0],Solution: complex solutions [i,[- 0.707107i, 0.707107],[-i,[0.707107i, 0.707107]]

#A=[[4,5,13],[3,4,5],[5,6,7]], Should return an error
