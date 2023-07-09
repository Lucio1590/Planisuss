import numpy as np
# import matplotlib.pyplot as plt

def normalize_matrix(data):
    """ Rescale a matrix in [0, 1] """
    return (data-np.nanmin(data))/(np.nanmax(data)-np.nanmin(data))