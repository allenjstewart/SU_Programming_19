#This code implements the single variable Newtons Method
#########################################################
#Newtons method is an algorithm for solving an equation f(x)=0
#For any function f(x)
#The algorithm is as follows
#Step one: choose a point (normally close to the actual solution) x_0
#Step two: Find the value of the derivative f'(x_0)
#Step three: Find the equation of the tangent line, y=f'(x_0)(x-x_0)+f(x_0)
#Step Four: Solve the linear equation, 0=f'(x_0)(x-x_0)+f(x_0)
#Solution- x_1=(f'(x_0)x_0-f(x_0))/f'(x_0)
#Step Five: Repeat steps two through four for x_1 and so on

#################################################################
#There are two big pieces; finding the derivative and the iterative loop
#Hopefully you can use your other code for the derivative in this code


#Import the appropriate libraries
import math as m
import sympy as sym


x = sym.symbols('x')

#Define the function of interest
def function(expr, a):

        #Evaluate the exression at x=a
	y = expr.subs(x, a)
	return y #Remember y is a local variable 

#Function for finding the derivative at x=a, f'(a)
def deriv(expr,a): #expr is the function and a is the value
        #Differentiate wrt x
        dy = sym.diff(expr, x)

        #Evaluate the derivative at x=a
        dy = dy.evalf(subs={x:a})
        
        return dy #Again, dy is local and so if dy is used elsewhere it needs to be defined again


def Newtons(f,x0,n): #here f is the function, x0 is the guess, and n is the number of loops

        x = x0
        for i in range(n): #Loop the Newton's Method algorithm described in the beginning comments
                x1 = (deriv(f, x)*x - function(f, x)) / deriv(f, x)
                x = x1
                
        sol = str(f) + ", Solution: " + str(x)
        return sol #Sol is the approximation to the solution to f(x)=0

########################################################

#Print out test of code for each equation

#x^2+x-1=0, Solutions: -1.61803, 0.618034

#e^x-2=0, Solutions: 0.693147

#e^x-2x-5, Solutions: -2.45716, 2.25164

#sin(pi*x+3)-1=0 Funamental solution: -0.95493
