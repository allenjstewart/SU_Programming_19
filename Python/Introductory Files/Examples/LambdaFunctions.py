#In python you can define functions

def square(x):
    return x**2

square(2)
square(0.5)    

#The method above requires a distinct definition and a name
#Somtimes it's nicer to be able to define quick anonymous functions
#Without giving the function an explicit name
#This is where lambda functions come into play

lambda_square = lambda x: x**2

#The variable lambda_square is now a lamda function 
#We can plug values in the way we would with any other function

lambda_square(2)
lambda_square(0.5)

