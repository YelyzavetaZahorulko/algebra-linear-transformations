import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

tetrahedron = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
])


def rotate_y(object, theta_degrees):
    theta = np.radians(theta_degrees)
    Ry = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    rotated_object = np.dot(object, Ry)
    print("Rotated Object around y-axis:")
    print(rotated_object)
    return rotated_object


def shear(object, tx, ty, tz):
    T = np.array([tx, ty, tz])
    translated_object = object + T
    print("Translated Object:")
    print(translated_object)
    return translated_object


def plot_3d_object(object, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Перелік граней тетраедра
    verts = [
        [object[0], object[1], object[2]],
        [object[0], object[1], object[3]],
        [object[0], object[2], object[3]],
        [object[1], object[2], object[3]]
    ]

    ax.add_collection3d(Poly3DCollection(verts, alpha=.25, facecolor='cyan'))
    ax.scatter(object[:, 0], object[:, 1], object[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.show()


print("Original Tetrahedron:")
print(tetrahedron)

rotated_tetrahedron = rotate_y(tetrahedron, 45)
plot_3d_object(rotated_tetrahedron, "Rotated Tetrahedron around Y-axis")

sheared_tetrahedron = shear(tetrahedron, 1, 2, 3)
plot_3d_object(sheared_tetrahedron, "Translated Tetrahedron")
