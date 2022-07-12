"""Tests for the solver.DiffusionEquation class
"""
import pytest
import numpy as np
import math
import solver.DiffusionEquation as de



class TestClass():
    @pytest.fixture
    def matrix1(self):

        def f(x): return math.sin(2 * (math.pi) * x)
        f = np.vectorize(f)
        return f

    def test_matrix(self,matrix1):
        [thist, uHist] = de.CrankNicholson([0, 1], 3, 3, matrix1, 1, 1).calculate()


        assert np.linalg.norm(uHist,np.inf)==np.linalg.norm([[1.00000000e+00 ,1.22464680e-16, -1.00000000e+00],
                                                            [-6.92307692e-01 , 2.05085223e-15,  6.92307692e-01],
                                                            [ 4.79289941e-01,  2.67238156e-14 ,-4.79289941e-01],
                                                            [-3.31816113e-01 ,-1.49105394e-14,  3.31816113e-01]],np.inf)
    @pytest.fixture
    def boundary_conditions(self):
        return 1


    def test_boundary_condition(self,boundary_conditions,matrix1):
        D=de.CrankNicholson([0, 1], 3, 3, matrix1, 1, 1).second_der()
        assert D[0,2] == boundary_conditions
