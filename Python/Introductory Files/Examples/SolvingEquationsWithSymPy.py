#SymPy is a symbolic manipulator for Python
#It can be useful when we want to find an exact solution
#Rather than a numerical approximation
#However, there are a lot of functions in SymPy that play fast and loose
#With general programming rules 
#In particular there are some function calls that run their own python 
#Subprograms on your computer
#This means that a maliciuous piece of code can be inputed 
#And then be given access to your computer
#It's important to be aware of these things


#solve is one of four solvers in SymPy
#All expressions are assumed to be equal to zero
from sympy.solvers import solve

#SymPy uses a class called symbol for symbolic manipulation
from sympy import Symbol

x = Symbol('x')
solve(x**2+x-1,x)
