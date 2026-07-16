import numpy as np

def rescale(input_array:np.array) -> np.array:
    """rescales a numpy array from 0-1"""
    lower = input_array.min()
    upper = input_array.max()
    return (input_array-lower) / (upper-lower)