import numpy as np

def mirror(object, axis):
    if axis == 'x':
        matrix = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        matrix = np.array([[-1, 0], [0, 1]])
    elif axis == 'both':
        matrix = np.array([[-1, 0], [0, -1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'both'")
    return np.dot(object, matrix)
