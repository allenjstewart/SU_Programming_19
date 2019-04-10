#Python supports complex numbers with j being the square root of -1

a=2+3j
type(a)

#Or you can also defined complex numbers via complex()

b=complex(2,1)

#Python supports arithmetic of complex numbers

a+b
a-b
a*b
a/b

#Python also has supporting functions for the complex type

a.real
a.imag
a.conjugate()

#The abs() function will calculate the modulus of a complex number
abs(a)

#The math library has a lot of common mathematical functions and constants

import math as m 

m.cos(m.pi/3)
m.log(2)

#But does not account for complex numbers
m.sqrt(-1)
m.cos(m.pi*j)

#The additional complex functions are in the cmath library

import cmath as cm

cm.pow(-1,.5)
cm.exp(m.pi*1j) #cmath uses 1j as the imaginary unit

