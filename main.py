import numpy as np
from rotate_resize import rotate, resize
from mirror import mirror
from shear_transform import shear, transform
from plot import plot_objects
from opencv_use import plot_2d_object, rotate_lib, resize_lib, mirror_lib, shear_lib, custom_transform_lib

object_1 = np.array([[0, 0], [1, 2], [2, 0], [0, 0]])  # Трикутник
object_2 = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])  # Бетмен


# Приклади трансформацій
rotated_object_1 = rotate(object_1, 90)
rotated_object_2 = rotate(object_2, 270)
resized_object_1 = resize(object_1, 1.5, 0.5)
resized_object_2 = resize(object_2, 1.5, 0.5)
mirror_object_1 = mirror(object_1, 'both')
mirror_object_2 = mirror(object_2, 'both')
sheared_object_1 = shear(object_1, 'x',  2, 0)
sheared_object_2 = shear(object_2, 'y', 0, 2)
custom_transformed_object_1 = transform(object_1, np.array([[1, 0], [0, 1]]))
custom_transformed_object_2 = transform(object_2, np.array([[1, 0], [0, 1/3]]))




# Візуалізація результатів трансформацій
# plot_objects(object_1, rotated_object_1, "Rotated Object 1")
# plot_objects(object_2, rotated_object_2, "Rotated Object 2")
# plot_objects(object_1, resized_object_1, "Resized Object 1")
# plot_objects(object_2, resized_object_2, "Resized Object 2")
# plot_objects(object_1, mirror_object_1, "Mirror Object 1")
# plot_objects(object_2, mirror_object_2, "Mirror Object 2")
# plot_objects(object_1, sheared_object_1, "Sheared Object 1")
# plot_objects(object_2, sheared_object_2, "Sheared Object 2")
# plot_objects(object_1, custom_transformed_object_1, "Custom Transformed Object 1")
# plot_objects(object_2, custom_transformed_object_2, "Custom Transformed Object 2")


# print("Original Square:")
# plot_2d_object(object_1, "Original Square")
#
# print("Original Triangle:")
# plot_2d_object(object_2, "Original Batman")

# rotated_object_3 = rotate_lib(object_1, 90)
# plot_2d_object(rotated_object_3, "Rotated Square by 90 degrees")

# resized_object_3 = resize_lib(object_1, 1.5, 0.5)
# plot_2d_object(resized_object_3, "Resized Square (sx=2, sy=0.5)")
#
# mirrored_object_3 = mirror_lib(object_1, 'x')
# plot_2d_object(mirrored_object_3, "Mirrored Square over X-axis")
#
# sheared_object_3 = shear_lib(object_1, 1, 0.5)
# plot_2d_object(sheared_object_3, "Sheared Square (shx=1, shy=0.5)")
#
# custom_matrix = np.array([
#     [1, 0.5, 0],
#     [0.5, 1, 0]
# ], dtype=np.float32)
#
# custom_transformed_object_3 = custom_transform_lib(object_1, custom_matrix)
# plot_2d_object(custom_transformed_object_1, "Custom Transformed Square")

