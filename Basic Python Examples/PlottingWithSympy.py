import sympy as sp
from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
graph=plot(sp.sin(3.14/x), title='Plot', xlabel='x', ylabel='y')
