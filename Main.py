import sympy as sym
from sympy import * 
import numpy as np      
import matplotlib.pyplot as plt

def graph(a,b,c,x1,x2):

    x = np. linspace(x1,x2)

    y = a*x**2 + b*x + c

    z = x**2 + x + 10



    plt.plot(x,y, label = '1' )
    plt.plot(x,z, label = '2' )

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()



graph(1,1,2,10,-10)