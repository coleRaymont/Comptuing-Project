import sympy as sym
from sympy import * 
import numpy as np      
import matplotlib.pyplot as plt

x = Symbol('x')

a = sym.diff(x**5)


def graph(a,b,c,x1,x2):


    p = np. linspace(x1,x2)

    y = a*p**2 + b*p + c



    plt.plot(p,y, label = '1' )
    
    
    

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.show()

def diff(y):
    x = Symbol('x')
    eq = sym.diff(y)

    print(eq) 


    
    


graph(1,1,2,10,-10)
diff(1,1,2)