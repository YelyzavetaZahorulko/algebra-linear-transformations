import numpy as np


def shear(object, axis, x, y):
    matrix = np.array([[1, x], [y, 1]])
    if axis == 'x':
        matrix = np.array([[1, x], [0, 1]])
    elif axis == 'y':
        matrix = np.array([[1, 0], [y, 1]])
    elif axis == 'both':
        matrix = np.array([[1, x], [y, 1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'both'")
    print(np.dot(object, matrix))
    return np.dot(object, matrix)


def transform(object, matrix):
    print(np.dot(object, matrix))
    return np.dot(object, matrix)