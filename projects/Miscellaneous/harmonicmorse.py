"""within this file, we will plot a harmonic oscillator potential on top of a morse
potential"""

import numpy as np
import matplotlib.pyplot as plt

def harmonicosc(k:int ,x_0: float,x: list) -> list :
    """ this function calculates the harmonic oscillator potential
     for a series of displacement x about the equilibrium point x_0
     It takes
     :param: x a list of displacements
     :param: k an integer :spring constant
     :param: x_0 equilibrium position"""
    return (0.5* k * (x-x_0)**2)

def morse(D_e:float ,x_0: float,b:float,x: list) -> list:
    """ this function calculates the morse potential
         for a series of displacement x about the equilibrium point x_0
         It takes
         :param: x a list of displacements
         :param: D_e a float :potential energy for bond formation (well depth)
         :param: x_0 equilibrium position
         :param: b beta is the exponential terms which controls the width of the potential"""
    return D_e*(1-np.exp(-b*(x-x_0)))**2

if __name__ =="__main__":
    # defining the values
    x_0=0
    xvals=np.linspace(-5,9,500)
    D_e=3.5
    b=.9
    k=6.3 #obtained from the Taylor expansion of the Morse potential around zero
    harmonicpotential=harmonicosc(k,x_0,xvals)
    morsepotential=morse(D_e,x_0,b,xvals)
    asymptopt=[3.5 for _ in xvals] #to show the dissociation treshold

    # creating figure object and subplot to add to the figure
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    ax.plot(xvals,harmonicpotential,"r",label="Harmonic potential")
    ax.plot(xvals,morsepotential,"b",label="Morse potential")
    ax.plot(xvals,asymptopt,"g-")
    ax.set(xlim=[-1.3,7.5],ylim=[0,3.8])
    ax.set_xlabel("displacement")
    ax.set_ylabel("Potential energy")
    ax.legend()
    plt.show()
