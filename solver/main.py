import DiffusionEquation as de
import math
import numpy as np
'''
Driver file meant to call to Solver.py.
'''
def f(x):return math.sin(2*(math.pi)*x)


f=np.vectorize(f)
de.CrankNicholson([0,1000],1000,30,f,1,0.0001).plot()
