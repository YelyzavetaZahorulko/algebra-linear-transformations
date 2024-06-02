import numpy as np
from rotate_resize import rotate, resize
from plot import plot_objects

object_1 = np.array([[0, 0], [1, 2], [2, 0], [0, 0]])  # Трикутник
object_2 = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])  # Бетмен


# Приклади трансформацій
rotated_object_1 = rotate(object_1, 180)
rotated_object_2 = rotate(object_2, 270)
resized_object_1 = resize(object_1, 1.5, 0.5)
resized_object_2 = resize(object_2, 1.5, 0.5)


# Візуалізація результатів трансформацій
plot_objects(object_1, rotated_object_1, "Rotated Object 1")
plot_objects(object_2, rotated_object_2, "Rotated Object 2")
plot_objects(object_1, resized_object_1, "Resized Object 1")
plot_objects(object_2, resized_object_2, "Resized Object 2")
