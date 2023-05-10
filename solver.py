""" A solver for 1D diffusion equation """
#! /usr/bin/python
import numpy as np

#set print options to look nice-- allows us to see diffusion btwn 'cells'
np.set_printoptions(formatter={"float": "{: 5.1f}".format})

def solver1d(C, dx, dt, k):
    """ method for solving diffusion: 
        params - concentration, grid spacing, timestep, diffusivity 
    """
    print("solving for 1d diffusion...")
    
    # equation for flux
    q = -k * np.diff(C) / dx 
    C[1:-1] -= dt * np.diff(q) / dx
    
    # minus-equal operator (-=) -- see variable on both sides of =
    # np.diff() returns a DataFrame with the difference between the values 
    # for each row and, by default, the previous row.
    return C
    # return is related to concept 'pass by reference' 

# function runs solver1D for 1 iteration with the following param values
def Param_Example1(): 
    k = 100 # diffusivity
    Lx = 10 # length
    dx = 0.5
    C1 = 500 # left boundary condition
    C2 = 0 # right boundary condition
    C = np.empty(Lx) # empty array
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / k / 2.1
    print("initial concentration:",C)
    
    solver1d(C, dx, dt, k)
    print("concentration diffused:",C)

# function runs solver1D for 4 iterations with the following param values
def Param_Example2(): 
    k = 100 # diffusivity
    Lx = 10 # length
    dx = 0.5
    C1 = 500 # left boundary condition
    C2 = 0 # right boundary condition
    C = np.empty(Lx) # empty array
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / k / 2.1
    print("initial concentration:",C)
    
    for _ in range(1,5): # iterate 4 times
        C = solver1d(C, dx, dt, k)
        print("concentration diffused ", _, " : ", C)
    

# example of simple 'unit test' 

# if the name of the module is main, run if statement
if __name__ == "__main__": # __name__ is a global variable
   Param_Example2() # pass parameters into solve1d()