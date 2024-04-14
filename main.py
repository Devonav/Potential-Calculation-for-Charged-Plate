from numpy import *
import numpy as np
from matplotlib import pyplot as plt

# This is a function which returns a list of exactly computed values for the potential
# difference measured at intervals dr away from a charged plate having charge density sigma
def V_exact(sigma,dr,rrange):
    #define permittivity of free space 
    eps_o=8.85e-12

    #initialize empty list to store values of potential v at various r locations
    v=[]

    #initialize list of r values that are equally spaced by interval dr
    rs=linspace(dr,rrange,num=int(rrange/dr))

    #iterate over r values and calculate potential at r; store in list
    for r in rs:
        v.append(-sigma*r/(2*eps_o))

    #cast list as numpy array for numeric operations later
    v=np.array(v)

    return v

# This is a function which returns a list of exactly computed values for the electric 
# field measured at intervals dr away from a charged plate having charge density sigma
def E_plate(sigma,dr,rrange):
  #define permittivity of free space 
    eps_o=8.85e-12

    #initialize empty list to store values of electric field E at various r locations
    E=[]

    #initialize list of r values that are equally spaced by interval dr
    rs=linspace(dr,rrange,num=int(rrange/dr))

    #iterate over r values and calculate electric field at r; store in list
    for r in rs:
        E.append(sigma/(2*eps_o))

  #cast list as numpy array for numeric operations later 
    E=np.array(E)
    return E

# This is a function which returns a list of approximate potential values which are 
# iteratively calculated by considering the first order finite difference definition of
# of the electric field
def V_first_order(sigma,dr,rrange):
  #initialize an exact list of electric field values to use for the approximation
    e=E_plate(sigma,dr,rrange)

    #initialize an exact list of potential values so the first value in the iterative
    #procedure is exact
    v=V_exact(sigma,dr,rrange)

    #initialize a list to store the iteratively calculated potential values
    potential=[0.]*len(v)
    #store the exact value in the first element of the list
    potential[0]=v[0]

    #iteratively calculate the next potential value based on a first order approximation
    for i in range(len(potential)-1):
        potential[i+1]=potential[i] - e[i]*dr

    #cast the list as a numpy array for numeric operations later
    potential=np.array(potential)
    return potential

# This is function which should return a list of approximate potential values which are 
# iteratively calculated by considering the second order finite difference definition.
# Please refer to the first order approximation for guidance on how to write the appropriate
# algorithm
def V_second_order(sigma, dr, rrange):
    # Define permittivity of free space
    eps_o = 8.85e-12

    # Calculate the electric field values, which are constant for a charged plate
    E = sigma / (2 * eps_o)

    # Initialize a list to store the potential values
    potential = [0] * int(rrange/dr)

    # Set the reference potential at the first point (arbitrary choice)
    potential[0] = 0  # For example, potential at infinity or at the surface

    # Calculate potential at each point using the trapezoidal rule for integration
    for i in range(1, len(potential)):
        # Using the trapezoidal rule: V_i = V_(i-1) + avg(E) * dr
        # Since E is constant, avg(E) = E
        potential[i] = potential[i-1] - E * dr  # Negative sign due to the definition of E

    # Convert the list to a numpy array for consistency
    potential = np.array(potential)
    return potential

# This is a function which plots the exact and approximate values of the potential
def plot_V(V_exact, V_finite_diff, V_finite_diff2, dr, rrange):
    fig, ax = plt.subplots()
    r = np.linspace(dr, rrange, num=int(rrange/dr))
    ax.plot(r/0.01, V_exact, '-o', lw=1, label='Exact Potential')
    ax.plot(r/0.01, V_finite_diff, 'x', lw=3, label='Potential fin. diff. method 1')
    if (len(V_finite_diff2) != 0):
        ax.plot(r/0.01, V_finite_diff2, 'x', lw=3, label='Potential fin. diff. method 2')
    plt.legend(fontsize=12)
    plt.ylabel("Potential (V)", fontsize=16)
    plt.xlabel("Distance from charged plate (cm)", fontsize=16)
    plt.tight_layout()
    plt.show()
    return


# This is a function which plots the absolute difference between the exact and
# approximate values of the potential. This function does not need to be modified
def plot_abs_error(E_exact,E_finite_diff,E_finite_diff2,dr,rrange):
    fig,ax=plt.subplots()
    r=linspace(dr,rrange,num=int(rrange/dr))
    err=[]
    for i in range(len(E_exact)-1):
        err.append(abs(E_exact[i]-E_finite_diff[i]))

    err=np.array(err)


    err2=[]
    if (len(E_finite_diff2)!=0):
        for i in range(len(E_exact)-1):
            err2.append(abs(E_exact[i]-E_finite_diff2[i]))

        err2=np.array(err2)

    ax.plot(r[:len(r)-1]/0.01,err,'--',lw=2,label='Absolute error in fin. diff. method 1')
    if (len(err2)!=0):
        ax.plot(r[:len(r)-1]/0.01,err2,'x',lw=2,label='Absolute error in fin. diff. method 2')

    plt.legend(fontsize=12)
    plt.yscale('log')
    plt.ylabel("Absolute error",fontsize=16)
    plt.xlabel("Distance from charged plate (cm)", fontsize=16)
    plt.tight_layout()
    plt.show()


# This section is treated as the MAIN part of the code, calling and running the various 
# function defined above

#parameters of charge density and dr for the computation
dr=0.001
rrange=0.2
sigma=1e-9

V1=V_exact(sigma,dr,rrange)
V2=V_first_order(sigma,dr,rrange)
V3=V_second_order(sigma,dr,rrange)
plot_V(V1,V2,V3,dr,rrange)
plot_abs_error(V1,V2,V3,dr,rrange)