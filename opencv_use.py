import numpy as np
import cv2
import matplotlib.pyplot as plt

def plot_2d_object(object, title):
    object = np.vstack([object, object[0]])  # замикання фігури
    plt.plot(object[:, 0], object[:, 1], 'o-')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def rotate_lib(object, degrees):
    matrix = cv2.getRotationMatrix2D((0, 0), degrees, 1)
    rotated_object = cv2.transform(np.array([object]), matrix)[0]
    print("Rotated Object:")
    print(rotated_object)
    return rotated_object


def resize_lib(object, x, y):
    matrix = np.array([
        [x, 0, 0],
        [0, y, 0]
    ])
    resized_object = cv2.transform(np.array([object]), matrix)[0]
    print("Resized Object:")
    print(resized_object)
    return resized_object


def mirror_lib(object, axis):
    if axis == 'x':
        matrix = np.array([
            [1, 0, 0],
            [0, -1, 0]
        ])
    elif axis == 'y':
        matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0]
        ])
    elif axis == 'both':
        matrix = np.array([
            [-1, 0, 0],
            [0, -1, 0]
        ])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'origin'")
    mirrored_object = cv2.transform(np.array([object]), matrix)[0]
    print("Mirrored Object:")
    print(mirrored_object)
    return mirrored_object


def shear_lib(object, x, y):
    matrix = np.array([
        [1, x, 0],
        [y, 1, 0]
    ])
    sheared_object = cv2.transform(np.array([object]), matrix)[0]
    print("Sheared Object:")
    print(sheared_object)
    return sheared_object


def custom_transform_lib(object, matrix):
    transformed_object = cv2.transform(np.array([object]), matrix)[0]
    print("Custom Transformed Object:")
    print(transformed_object)
    return transformed_object


