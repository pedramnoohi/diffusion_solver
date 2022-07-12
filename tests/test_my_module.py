"""Tests for the solver.my_module module.
"""
import pytest

import solver.DiffusionEquation as de



#def uHist_check():
#    assert hello('nlesc') == 'Hello nlesc!'


def matrix():
    [thist, uHist] = de.CrankNicholson([0, 1], 3, 3, f, 1, 1).calculate()

    assert uHist==[[1.00000000e+00 ,1.22464680e-16, -1.00000000e+00],
                   [-6.92307692e-01 , 2.05085223e-15,  6.92307692e-01],
                    [ 4.79289941e-01,  2.67238156e-14 ,-4.79289941e-01],
                    [-3.31816113e-01 ,-1.49105394e-14,  3.31816113e-01]]


#@pytest.fixture
#def some_name():
    #return 'Jane Smith'


#def test_hello_with_fixture(some_name):
    #assert hello(some_name) == 'Hello Jane Smith!'
