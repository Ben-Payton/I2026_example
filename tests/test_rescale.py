from src.my_test_bep.rescale import rescale as rescale
import numpy as np


def test_positive_from_zero():
    np.testing.assert_allclose(rescale(np.array([0,1,2])) ,np.array([0,.5,1]))

def test_negative_to_positive():
    np.testing.assert_allclose(rescale(np.array([-1,0,1])) ,np.array([0,.5,1]))

def test_positive_to_negative():
    np.testing.assert_allclose(rescale(np.array([1,0,-1])) ,np.array([1,.5,0]))