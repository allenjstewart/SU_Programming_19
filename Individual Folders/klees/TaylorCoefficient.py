#This code implements an algorithm for finding the nth Taylor coefficient
#########################################################
#The nth Taylor coefficient of a function f(x)
#Centered around x=a is given by
#T_n=f^(n)(a)/n!
#It works best if f is infinitely differentiable at x=a.

#################################################################
#This code is all about finding the nth derivative of a function
#Import the appropriate libraries

import sympy as sp
from sympy.abc import x
import math as m

#Define the function of interest
def function(x):
    y=m.sin(x)
    return y #Remember y is a local variable

#I am going to write this bit of code for you to use in the program
#It will output the nth derivative of a function as a lambda function
#This will allow you to plug in values
def deriv(expr,n): #expr is a sympy function of x
    symb_deriv=sp.diff(expr,'x',n)
    num_deriv=sp.lambdify(x,symb_deriv)
    return num_deriv

#Tests of the deriv function
print(deriv(x**2+2*x,2)(3))#This should return 2
print(deriv(sp.exp(2*x),1)(1))#This should return 14.7781

################################################
def Taylor_coeff(f,a,n): #here f is the function, a is the center of the series, and n is the term we want
    #You will need to make use of the function I coded, deriv
    derivative=deriv(f,n)(a)
    factorial=m.factorial(n)
    coefficient=derivative/factorial
    return coefficient  #return the value of the Taylor coefficient

print(Taylor_coeff(sp.sin(x),0,7))
#Tests of the deriv function
print(deriv(x**2+2*x,2)(3))#This should return 2
print(deriv(sp.exp(2*x),1)(1))#This should return 14.7781

################################################
def Taylor_coeff(f,a,n): #here f is the function, a is the center of the series, and n is the term we want
    #You will need to make use of the function I coded, deriv
    derivative=deriv(f,n)(a)
    factorial=m.factorial(n)
    coefficient=derivative/factorial
    return coefficient  #return the value of the Taylor coefficient

print(Taylor_coeff(sp.sin(x),0,7))
