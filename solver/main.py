import DiffusionEquation as de
import math
import numpy as np
'''
Driver file meant to call to Solver.py.
'''
def f(x):return math.sin(2*(math.pi)*x)


f=np.vectorize(f)
[thist,uHist]=de.CrankNicholson([0,1],3,3,f,1,1).calculate()
print(uHist)

