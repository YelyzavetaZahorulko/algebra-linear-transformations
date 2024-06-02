import numpy as np


def rotate(object, theta_degrees):
    theta = np.radians(theta_degrees)
    matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return np.dot(object, matrix)


def resize(object, sx, sy):
    matrix = np.array([[sx, 0], [0, sy]])
    return np.dot(object, matrix)