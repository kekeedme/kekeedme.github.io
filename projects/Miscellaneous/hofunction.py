"""This file will contain the ground state harmonic oscillator function, and the
creation operator to generate higher states of the oscillator. We will graph them"""
import numpy as np
import scipy.constants as constant
import matplotlib.pyplot as plt
from useful_math_functions import nderivative
def groundsateho(h_bar: float,omega:float,mass:float,x: list):
    """this function is the ground state harmonic oscillator in 1-D.
    It takes the following
    :param: h_bar which is the reduced planck constant
    :param: omega which is the frequency of oscillation
    :param: mass of the particle
    :param: x is the list of positions"""

    return ((mass*omega)/(np.pi*h_bar))**(1/4)*np.exp(-(mass*omega*x**2)/(2*h_bar))

def momentum(function,x:list,h):
    """This is the momentum operator. It returns the first derivative times -ihbar
    It takes
    :param: function to be differentiated
    param: the domain of the function
    param: the stepsixe"""
    return -1j* constant.hbar* nderivative(function,1,x,h)
